#!/usr/bin/python
""" This script processes yaml stats files collected from openshift clusters """

import logging
import os
import re
import sys
import tarfile
import transaction
import yaml

from datetime import datetime

import sqlalchemy.orm.exc

from sqlalchemy import engine_from_config, distinct

from pyramid.paster import (get_appsettings,
                            setup_logging)

from pyramid.scripts.common import parse_vars

from budget.models import (DBSession,
                           Base,
                           Openshift3Node,
                           Openshift3Pod,
                           Openshift3Project,
                           Openshift3User)

from ..util.fileloader import load_yaml, save_yaml
from ..util.addset import addset
from ..util.queries.util import insert_or_update

def usage():
    ''' how to call this program '''
    print "Usage: %s <config_uri> [statsfile-YYYY-MM-DD.tar.bz2]" % sys.argv[0]
    sys.exit()

def update(session, table, yml, yaml_info):
    ''' update node inventory based on supplied yaml

        return a list of node uids
    '''
    uidlist = []
    for item in yml['items']:
        meta = item['metadata']
        uid = item['metadata']['uid']
        uidlist.append(uid)

        defaults = {'collection_date' : yaml_info['collection_date'],
                    'create_date' : item['metadata']['creationTimestamp'],
                    'end_date' : None,
                    'meta' : yaml.dump(meta)}

        kwargs = {'uid' : uid,
                  'cluster_id' : yaml_info['cluster_id']}

        if table != Openshift3User:
            status = item['status']
            defaults['status'] = yaml.dump(status)

        obj = insert_or_update(session, table, defaults=defaults, **kwargs)
        DBSession.merge(obj)
    transaction.commit()
    return uidlist

def expire(session, table, uidlist):
    ''' any uids that aren't included in the current stats files is marked
        as terminated
    '''
# XXX: when we update inventory, we get a list of distinct uids. then, when we
# parse the latest inventory files, if a uid isn't in our list, it's marked as
# deleted. As an error-handling mechanism, if a uid exists in a future list, we
# can compare region/sizing/IP and, if matches are found, we can null out the
# end_date field.

    dbuids = session.query(table.uid.distinct()).all()
    dbuids = [u for u, in dbuids]

    for uid in dbuids:
        if uid in uidlist:
            dbuids.remove(uid)

    for uid in dbuids:
        end, = session.query(table.end_date).filter( \
                    table.uid == uid).one()

        if not end:
            defaults = {'end_date' : datetime.now()}
            kwargs = {'uid' : uid}
            obj = insert_or_update(DBSession,
                                   Openshift3Node,
                                   defaults=defaults,
                                   **kwargs)
            DBSession.merge(obj)
    transaction.commit()

def select_latest():
    ''' examines filename for YYYY-MM-DD portion of filename, returns latest '''

    # os.walk returns (dirpath, dirnames, filenames)
    # we only use the filenames.
    bz2_files = []
    for (_, _, filenames) in os.walk(cache_dir):
        bz2_files.extend([f for f in filenames if re.search(r'\.bz2$', f)])

    regex = r'^v3stats-(\d{4}-\d{2}-\d{2})\.tar\.bz2$'
    latest = max([re.search(regex, f).groups()[0] for f in bz2_files \
                                                  if re.search(regex, f)])

    return '%s/v3stats-%s.tar.bz2' % (cache_dir, latest)

def parse_filename(filename):
    ''' parse information from filename '''
    rgx = re.compile(r'([a-zA-Z]+)-([\w\-]+)-master-(\w+)-(\d{4}-\d{2}-\d{2}).yaml')
    groups = rgx.search(filename).groups()
    return {'type' : groups[0],
            'cluster_id' : groups[1],
            'collection_date' : groups[3]}

def main(args):
    ''' entry point '''

    if len(args) < 1:
        usage()

    selected = None
    if len(args) > 2:
        selected = args[2]
        if not os.path.exists(selected):
            usage()

    config_uri = args[1]
    options = parse_vars(args[3:])

    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    global cache_dir
    cache_dir = settings['cache.dir'] + "/v3stats"

    if not selected:
        selected = select_latest()

    log.info('processing %s.', selected)

    tar = tarfile.open(selected, 'r:bz2')
    member_list = tar.getmembers()
    # skip the directory entry in the tar file
    member_list.pop(0)

    uidlist = {}
    typemap = {'nodes'    : Openshift3Node,
               'pods'     : Openshift3Pod,
               'projects' : Openshift3Project,
               'users'    : Openshift3User}

    for member in member_list:
        log.info('processing %s.', member)
        yml = load_yaml(tar.extractfile(member))

        parsed_name = parse_filename(member.name.split('/')[-1])
        if parsed_name['type'] not in uidlist:
            uidlist[parsed_name['type']] = []

        uids = update(DBSession, typemap[parsed_name['type']], yml, parsed_name)
        uidlist[parsed_name['type']].extend(uids)

    for type_ in uidlist:
        expire(DBSession, typemap[type_], uidlist[type_])

if '__main__' in __name__:
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print "Ctrl-C detected. Exiting."
        sys.exit()
