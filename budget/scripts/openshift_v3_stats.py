#!/usr/bin/python
""" This script processes yaml stats files collected from openshift clusters """

import logging
import os
import re
import shutil
import sys
import tarfile
import tempfile
import transaction
import yaml

from datetime import datetime
from multiprocessing import Pool, cpu_count

import sqlalchemy.orm.exc

from sqlalchemy import engine_from_config, distinct
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.exc import IntegrityError
from zope.sqlalchemy import ZopeTransactionExtension

from pyramid.paster import (get_appsettings,
                            setup_logging)

from pyramid.scripts.common import parse_vars

from budget.models import (DBSession,
                           Openshift3Node,
                           Openshift3Pod,
                           Openshift3Project,
                           Openshift3User)

from ..util.fileloader import load_yaml
from ..util.queries.util import insert_or_update

def usage():
    ''' how to call this program '''
    print "Usage: %s <config_uri> [statsfile-YYYY-MM-DD.tar.bz2]" % sys.argv[0]
    sys.exit()

def read_stats(statspath, filename):
    ''' update node inventory based on supplied yaml

        param: a directory
        param: a yaml filename
        return: an unholy mess
    '''
    log.info('processing %s.', filename)

    uidlist = set()
    rows = []

    info = parse_filename(filename)
    tablemap = {'nodes'    : Openshift3Node,
                'pods'     : Openshift3Pod,
                'projects' : Openshift3Project,
                'users'    : Openshift3User}

    yml = load_yaml(statspath+'/'+filename)
    for item in yml['items']:
        meta = item['metadata']
        uid = item['metadata']['uid']
        uidlist.add(uid)

        defaults = {'collection_date' : info['collection_date'],
                    'create_date'     : item['metadata']['creationTimestamp'],
                    'end_date'        : None,
                    'cluster_id'      : info['cluster_id'],
                    'meta'            : yaml.dump(meta)}

        kwargs = {'uid' : uid}

        if tablemap[info['type']] != Openshift3User:
            status = item['status']
            if 'images' in status.keys():
                # the images list in lengthy and doesn't have much useful info
                del status['images']

            defaults['status'] = yaml.dump(status)

        rows.append((tablemap[info['type']], defaults, kwargs))
    return (uidlist, rows)

def expire(session, table, uidlist, expiredate):
    ''' any uids that aren't included in the current stats files is marked
        as terminated

        Param: a sqlalchemy session object
        Param: a sqlalchemy table class reference
        Param: an iterable (set or list) containing uid strings
    '''
    dbuids = session.query(table.uid.distinct()).all()
    dbuids = [u for u, in dbuids]

    diff = list(set(dbuids)-set(uidlist))

    for uid in diff:
        obj = session.query(table
                           ).filter(table.uid == uid,
                                    table.end_date == None,
                                   ).update({'end_date':expiredate})
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
    rgx = re.compile(\
            r'([a-zA-Z]+)-([\w\-]+)-master-(\w+)-(\d{4}-\d{2}-\d{2}).yaml')
    groups = rgx.search(filename).groups()
    return {'type' : groups[0],
            'cluster_id' : groups[1],
            'collection_date' : groups[3]}

def extract_tarbz2(filename):
    ''' extract a tarball to a temp dir.

        param: filename.tar.bz2
        returns: path string to a tempdir containing tarball contents
    '''
    tempdir = tempfile.mkdtemp()

    log.info('extracting %s to %s ', filename, tempdir)

    tar = tarfile.open(filename, 'r:bz2')
    member_list = tar.getmembers()

    for member in member_list:
        tar.extract(member, path=tempdir)

    return tempdir

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

    # global to enable us to handle KeyboardInterrupts without leaving zombies around.
    global pool
    pool = Pool(processes=cpu_count()*2)


    if not selected:
        selected = select_latest()

    objects = []
    pids = []

    stats_path = extract_tarbz2(selected)
    for filename in os.listdir(stats_path+'/stats'):
        try:
            run = pool.apply_async(read_stats,
                                   (stats_path+'/stats', filename),
                                   callback=objects.append)
            pids.append(run)
        except Exception as exc:
            print exc
            log.debug(exc)
            raise

    # get the output of all our processes
    for pid in pids:
        pid.get()

    # ensure the sqlalchemy objects aren't garbage-collected before we commit them.
    # see: http://docs.sqlalchemy.org/en/latest/orm/session_state_management.html#session-referencing-behavior
    merged = []
    uidlist = {}
    for uids, arglist in objects:
        for table, defaults, kwargs in arglist:
            if table in uidlist.keys():
                uidlist[table].update(uids)
            else:
                uidlist[table] = uids
            obj = insert_or_update(DBSession, table, defaults=defaults, **kwargs)
            merged.append(DBSession.merge(obj))
    try:
        transaction.commit()
    except IntegrityError as exc:
        DBSession.rollback()
        log.error(exc)

    pool.close()
    pool.join()

    for table in uidlist:
        rgx = re.compile(r'v3stats-(\d{4}-\d{2}-\d{2}).tar.bz2')
        scandate, = rgx.search(selected).groups()
        expire(DBSession,
               table,
               uidlist[table],
               scandate)

    shutil.rmtree(stats_path)

if '__main__' in __name__:
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print "Ctrl-C detected. Exiting."
        pool.terminate()
        sys.exit()
