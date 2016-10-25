#!/usr/bin/env python
''' Script to ingest GCP billing data into a DB '''

import logging
import os
import re
import sys
import transaction

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse as parse_date

from gcloud import storage
from oauth2client.client import GoogleCredentials

from sqlalchemy import engine_from_config
from sqlalchemy.sql import functions

from pyramid.paster import get_appsettings, setup_logging

from pyramid.scripts.common import parse_vars

from ..models import (DBSession,
                      GcpLineItem)

from ..util.fileloader import load_json, save_json

LOG = logging.getLogger(__name__)
COMMIT_THRESHOLD = 10000

def usage(argv):
    ''' cli usage '''
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [rundate=YYYY-MM-DD]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def update_file_cache(settings):
    ''' download JSON files from GCP Storage bucket, returns a list of the
    files that were downloaded/changed '''
    etags = load_json(settings['cache.dir']+'/gcp/etags.json')

    #FIXME
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = settings['creds.dir'] + \
                                                   "/" + \
                                                   settings['creds.gcp.json']
    credentials = GoogleCredentials.get_application_default()
    client = storage.Client(project=settings['creds.gcp.project'],
                            credentials=credentials)
    bucket = client.get_bucket('exported-billing')

    LOG.debug("Checking for new/changed files.")
    changed = []
    for obj in bucket.list_blobs():
        filename = settings['cache.dir']+'/gcp/'+obj.name
        if not os.path.exists(filename) or \
                filename not in etags or \
                obj.etag != etags[filename]:

            try:
                LOG.debug("Etags for %s: %s == %s",
                          obj.name,
                          obj.etag,
                          etags[filename])
            except KeyError:
                LOG.debug("Etag missing: %s", obj.name)

            LOG.info("Downloading: %s", obj.name)
            obj.download_to_filename(filename)
            etags[filename] = obj.etag
            changed.append(os.path.basename(filename))
    save_json(settings['cache.dir']+'/gcp/etags.json', etags)
    return changed

def filename_to_date(filename):
    """ parses a json filename for individual component metadata.
    """
    rgx = re.compile(r'gcp-billing-(\d{4})-(\d{2})-(\d{2})\.json')
    year, month, day = rgx.match(filename).groups()
    return datetime(year=int(year), month=int(month), day=int(day))

def date_to_filename(filedate):
    """ uses a date to select a json filename.
        Param: a datetime object
    """
    return "gcp-billing-%04i-%02i-%02i.json" % (filedate.year,
                                                filedate.month,
                                                filedate.day)

def insert_data(filename, cache_dir, rundate=None):
    ''' insert gcp data into DB
        param: String, a filename containing json-formatted GCP billing data
        param: Datetime to insert only data points with a start or end date
               matching the provided datetime's year, month, and day
               (ignores hour, minute, second, and tzinfo).
    '''
    objects = []
    jsonfile = load_json(cache_dir+'/'+filename)
    LOG.debug("Inserting data from: %s", filename)
    for item in jsonfile:
        if len(objects) > COMMIT_THRESHOLD:
            transaction.commit()
            del objects[:]

        if rundate:
            # If the data points are on the same day, load 'em.
            start = parse_date(item['startTime']).replace(hour=0,
                                                          minute=0,
                                                          second=0,
                                                          tzinfo=None)
            end = parse_date(item['endTime']).replace(hour=0,
                                                      minute=0,
                                                      second=0,
                                                      tzinfo=None)
            if start == rundate or end == rundate:
                pass
            else:
                continue

        if 'projectName' in item.keys():
            project_name = item['projectName']
        else:
            project_name = None

        line = GcpLineItem(project_name=project_name,
                           line_description=item['description'],
                           line_id=item['lineItemId'],
                           start_time=parse_date(item['startTime']),
                           end_time=parse_date(item['endTime']),
                           measured_amount=item['measurements'][0]['sum'],
                           measured_unit=item['measurements'][0]['unit'],
                           cost_amount=item['cost']['amount'],
                           cost_currency=item['cost']['currency'])
        objects.append(line)
    DBSession.add_all(objects)
    transaction.commit()

def run(settings, options):
    ''' run data ingestion process for a maximum of the last 6 months of data.

        Param: datetime object or None. If None, ingestion runs on latest
               available file in cache_dir. If present, ingestion runs on
               file with the provided YYYY-MM-DD in its filename.

    '''
    cache_dir = settings['cache.dir'] + "/gcp"
    changed = []
    if 'nocacheupdate' not in options:
        changed = update_file_cache(settings)

    if 'rundate' in options:
        # GCP puts data for a given date inside of files labeled for
        # $date, # $date - $1-day and $date + $1-day.
        # So, we scan all three files for relevant data needing to be reset.

        rundate = datetime.strptime(options['rundate'], '%Y-%m-%d')
        runafter = rundate + relativedelta(days=1)
        runbefore = rundate - relativedelta(days=1)
        filename = date_to_filename(rundate)
        filebefore = date_to_filename(runbefore)
        fileafter = date_to_filename(runafter)

        LOG.info("Deleting records with start-date: %s", options['rundate'])
        # delete any existing records and re-ingest
        DBSession.query(GcpLineItem
                       ).filter(GcpLineItem.start_time == options['rundate']
                               ).delete()
        LOG.info("Deleting records with end-date: %s", options['rundate'])
        # delete any existing records and re-ingest
        DBSession.query(GcpLineItem
                       ).filter(GcpLineItem.end_time == options['rundate']
                               ).delete()
        insert_data(filebefore, cache_dir, rundate=rundate)
        insert_data(filename, cache_dir, rundate=rundate)
        insert_data(fileafter, cache_dir, rundate=rundate)
    else:
        # check last insert date, then do import here.
        last_insert, = DBSession.query(functions.max(GcpLineItem.end_time
                                                    )).one()
        if not last_insert:
            # only import the last 6 months of data, maximum.
            last_insert = datetime.today() - relativedelta(months=7)

        LOG.debug("Last insert: %s", last_insert)

        for filename in os.listdir(cache_dir):
            if filename == 'etags.json':
                continue

            file_date = filename_to_date(filename)
            if file_date > last_insert:
                insert_data(filename, cache_dir)
                # don't insert the same data twice.
                if filename in changed:
                    changed.pop(changed.index(filename))

        for filename in changed:
            fndate = filename_to_date(filename)
            next_day = datetime.today() + relativedelta(days=1)

            # clear out partial data, then re-insert
            DBSession.query(GcpLineItem
                           ).filter(GcpLineItem.start_time.between(fndate,
                                                                   next_day),
                                    GcpLineItem.end_time.between(fndate,
                                                                 next_day)
                                   ).delete(synchronize_session='fetch')
            insert_data(filename, cache_dir)

def main(argv):
    ''' main script entry point '''
    if len(argv) < 2:
        usage(argv)

    config_uri = argv[1]
    options = parse_vars(argv[2:])

    setup_logging(config_uri)

    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    run(settings, options)

if '__main__' in __name__:
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
