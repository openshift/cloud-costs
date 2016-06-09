#!/usr/bin/env python

import logging
import os
import re
import sys
import transaction

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from gcloud import storage
from oauth2client.client import GoogleCredentials

from sqlalchemy import engine_from_config 
from sqlalchemy.sql import functions

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    Base,
    GcpLineItem
    )

from ..util.fileloader import load_json, save_json

COMMIT_THRESHOLD = 100000

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def update_file_cache():
    ''' download JSON files from GCP Storage bucket, returns a list of the
    files that were downloaded/changed '''
    etags = load_json(cache_dir+'/etags.json')

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = settings['creds.dir'] + '/os302gce-b5af6b64b402.json'
    credentials = GoogleCredentials.get_application_default()
    client = storage.Client(project='corded-cable-672', credentials=credentials)
    bucket = client.get_bucket('exported-billing')

    changed = []
    for obj in bucket.list_blobs():
        fn = cache_dir+'/'+obj.name
        if not os.path.exists(fn) or fn not in etags or obj.etag != etags[fn]:
            log.debug('fetching: %s' % obj.name)
            obj.download_to_filename(fn)
            etags[fn] = obj.etag
            changed.append(os.path.basename(fn))
    save_json(cache_dir+'/etags.json', etags)
    log.debug("changed: %s" % changed)
    return changed

def filename_to_date(filename):
    """ parses a json filename for individual component metadata.
    """
    rgx = re.compile(r'gcp-billing-(\d{4})-(\d{2})-(\d{2})\.json')
    year,month,day = rgx.match(filename).groups()
    return datetime(year=int(year),month=int(month),day=int(day))

def insert_data(filename):
    log.debug('inserting data: %s' % filename)
    objects = []
    jsonfile = load_json(cache_dir+'/'+filename)
    for item in jsonfile:
        if len(objects) > COMMIT_THRESHOLD:
            transaction.commit()
            del objects[:]

        if 'projectName' in item.keys():
            project_name = item['projectName']
        else:
            project_name = None

        line = GcpLineItem(
                        project_name = project_name,
                        line_description = item['description'],
                        line_id = item['lineItemId'],
                        start_time = item['startTime'],
                        end_time = item['endTime'],
                        measured_amount = item['measurements'][0]['sum'],
                        measured_unit = item['measurements'][0]['unit'],
                        cost_amount = item['cost']['amount'],
                        cost_currency = item['cost']['currency'],
                    )
        objects.append(line)
    log.debug("saving...")
    DBSession.add_all(objects)
    transaction.commit()

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)

    config_uri = argv[1]
    options = parse_vars(argv[2:])

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    global settings
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    global cache_dir
    cache_dir = settings['cache.dir'] + "/gcp"

    changed = update_file_cache()
    # check last insert date, then do import here.
    last_insert, = DBSession.query(functions.max(GcpLineItem.end_time)).one()
    if not last_insert:
        # only import the last 6 months of data, maximum.
        last_insert = datetime.today() - relativedelta(months=7)
    log.debug("last insert: %s" % last_insert)

    for fn in os.listdir(cache_dir):
        if fn == 'etags.json':
            continue

        file_date = filename_to_date(fn)
        if file_date > last_insert:
            insert_data(fn)
            if fn in changed:
                changed.pop(changed.index(fn))

    for fn in changed:
        fndate = filename_to_date(fn)
        next_day = datetime.today() + relativedelta(days=1)

        # clear out partial data, then re-insert
        DBSession.query(GcpLineItem).filter(
                GcpLineItem.start_time.between(fndate, next_day),
                GcpLineItem.end_time.between(fndate, next_day),
            ).delete()
        insert_data(fn)

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
