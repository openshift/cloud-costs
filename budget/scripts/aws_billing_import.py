#!/usr/bin/env python

import boto
import csv
import json
import logging
import os
import re
import sys
import transaction
import zipfile
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from sqlalchemy import engine_from_config 
from sqlalchemy.sql import functions

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    AwsDetailedLineItem,
    AwsInvoiceLineItem,
    AwsCostAllocation,
    Base,
    )

s3_bucket_name = 'primary_billing_bucket'
checksum_filename = 'checksums.json'

# connect to AWS
# look up S3 Bucket
# list files
# get ETags / md5 checksums
# compare etags / checksums with file cache
# download new/changed files
# unzip detailed-billing-with-tags CSV
# process each CSV line
# insert into aws_detailed_line_item table
# TODO: insert invoice totals lines into aws_invoice_line_item table

def get_s3_bucket():
    log.debug("Connecting to S3...")
    try:
        access_key = os.environ['AWS_ACCESS_KEY_ID']
        secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
    except KeyError:
        log.error("No Access Key or Secret Key found. Is your environment set up?")
        return None
    conn = boto.connect_s3(access_key, secret_key)
    log.debug("Fetching bucket...")
    return conn.get_bucket(s3_bucket_name)

def retrieve_files(bucket):
    chksum_file = load_checksums()

    keys = bucket.list()
    for key in bucket.list():
        if re.search('logs\/', key.name):
            today = (date.today() - relativedelta(months=1)).strftime('%Y-%m-%d')
            if key.name[5:15] < today:
                log.debug('Deleting %s' % key.name)
                key.delete()
            continue

        #check etags/md5
        if key.name in chksum_file.keys() and key.etag == chksum_file[key.name]:
            continue
        else:
            log.info("checksums do not match. retrieving %s from s3..." % key.name)
            chksum_file[key.name] = key.etag

            try:
                key.get_contents_to_filename(cache_dir+'/'+key.name)
            except e:
                log.error(key.name+": "+e.message)
    save_checksums(chksum_file)


def load_checksums():
    try:
        chksum = json.load(open(checksum_filename, 'r+'))
    except IOError:
        chksum = json.loads('{}')
    return chksum

def save_checksums(chksums):
    try:
        json.dump(chksums, open(checksum_filename, 'w+'))
    except IOError:
        raise

def load_detailed_line_items(begin=datetime(2000,01,01)):
    lastdate, = DBSession.query(
                functions.max(AwsDetailedLineItem.usage_end_date)
            ).one()

    for fn in os.listdir(cache_dir):
        match = re.search('aws-billing-detailed-line-items-with-resources-and-tags-(\d{4})-(\d{2}).csv.zip', fn)
        if match:
            year, month = match.groups()
            filedate = datetime(int(year), int(month), 1)

            if lastdate is None or (filedate > lastdate and filedate > begin):
                log.debug("newer data found: %s" % filedate)
                import_detailed_line_items(fn, filedate)

def load_cost_allocation(begin=datetime(2000,01,01)):
    lastdate, = DBSession.query(
                functions.max(AwsCostAllocation.billing_period_end_date)
            ).one()

    for fn in os.listdir(cache_dir):
        match = re.search('aws-billing-cost-allocation-(\d{4})-(\d{2}).csv.zip', fn)
        if match:
            year, month = match.groups()
            filedate = datetime(int(year), int(month), 1)

            if lastdate is None or (filedate > lastdate and filedate > begin):
                log.debug("newer data found: %s" % filedate)
                import_cost_allocation(fn, filedate)

# Detailed Line Items w/ resources & tags
# "InvoiceID","PayerAccountId","LinkedAccountId","RecordType","RecordId","ProductName","RateId","SubscriptionId","PricingPlanId","UsageType","Operation","AvailabilityZone","ReservedInstance","ItemDescription","UsageStartDate","UsageEndDate","UsageQuantity","BlendedRate","BlendedCost","UnBlendedRate","UnBlendedCost","ResourceId"

def import_detailed_line_items(zipfilename, filedate):
    objects = []

    zfile = zipfile.ZipFile(cache_dir+'/'+zipfilename, 'r')
    zinfo, = zfile.infolist()
    with zfile.open(zinfo) as zf:
        csvfile = csv.reader(zf)
        csvfile.next() # pop the header

        # todo - figure out how to deal with incomplete month data.
        #
        # there's a running monthly total for each account that needs to be deleted/updated
        #
        # we need to store/cache the timestamp of the last lineitem we see
        # and/or develop a query to suss it out of the database on start-up
        for row in csvfile:
            if len(objects) > 1000:
                log.debug("bulk saving...")
                DBSession.add_all(objects)
                transaction.commit()
                del objects[:]

            line_item = AwsDetailedLineItem(
                invoice_id        = row[0],
                payer_account_id  = row[1],
                linked_account_id = row[2],
                record_type       = row[3],
                record_id         = row[4],
                product_name      = row[5],
                rate_id           = row[6],
                subscription_id   = row[7],
                pricing_plan_id   = row[8],
                usage_type        = row[9],
                operation         = row[10],
                availability_zone = row[11],
                reserved_instance = row[12],
                item_description  = row[13],
                usage_start_date  = process_date(row[14], filedate),
                usage_end_date    = process_date(row[15], filedate),
                usage_quantity    = row[16],
                blended_rate      = row[17],
                blended_cost      = row[18],
                unblended_rate    = row[19],
                unblended_cost    = row[20],
                resource_id       = row[21],
            )
            if len(row) == 23:
                line_item.user_environment  = row[22]
            if len(row) == 24:
                line_item.user_node         = row[23]

            objects.append(line_item)
        log.debug("saving...")
        DBSession.add_all(objects)
        transaction.commit()

# Cost Allocation
# "InvoiceID","PayerAccountId","LinkedAccountId","RecordType","RecordID","BillingPeriodStartDate","BillingPeriodEndDate","InvoiceDate","PayerAccountName","LinkedAccountName","TaxationAddress","PayerPONumber","ProductCode","ProductName","SellerOfRecord","UsageType","Operation","AvailabilityZone","RateId","ItemDescription","UsageStartDate","UsageEndDate","UsageQuantity","BlendedRate","CurrencyCode","CostBeforeTax","Credits","TaxAmount","TaxType","TotalCost","user:environment","user:node"

def import_cost_allocation(zipfilename, filedate):
    objects = []

    zfile = zipfile.ZipFile(cache_dir+'/'+zipfilename, 'r')
    zinfo, = zfile.infolist()
    with zfile.open(zinfo) as zf:
        csvfile = csv.reader(zf)
        csvfile.next() # pop the header

        # todo - figure out how to deal with incomplete month data.
        #
        # there's a running monthly total for each account that needs to be deleted/updated
        #
        # we need to store/cache the timestamp of the last lineitem we see
        # and/or develop a query to suss it out of the database on start-up
        for row in csvfile:
            if len(objects) > 1000:
                log.debug("bulk saving...")
                DBSession.add_all(objects)
                transaction.commit()
                del objects[:]

            line_item = AwsCostAllocation(
                invoice_id                = row[0],
                payer_account_id          = row[1],
                linked_account_id         = row[2],
                record_type               = row[3],
                record_id                 = row[4],
                billing_period_start_date = process_date(row[5], filedate),
                billing_period_end_date   = process_date(row[6], filedate),
                invoice_date              = process_date(row[7], filedate),
                payer_account_name        = row[8],
                linked_account_name       = row[9],
                taxation_address          = row[10],
                payer_po_number           = row[11],
                product_code              = row[12],
                product_name              = row[13],
                seller_of_record          = row[14],
                usage_type                = row[15],
                operation                 = row[16],
                availability_zone         = row[17],
                rate_id                   = row[18],
                item_description          = row[19],
                usage_start_date          = process_date(row[20], filedate),
                usage_end_date            = process_date(row[21], filedate),
                usage_quantity            = row[22],
                blended_rate              = row[23],
                currency_code             = row[24],
                cost_before_tax           = row[25],
                credits                   = row[26],
                tax_amount                = row[27],
                tax_type                  = row[28],
                total_cost                = row[29],
            )
            if len(row) == 31:
                line_item.user_environment  = row[30]
            if len(row) == 32:
                line_item.user_node         = row[31]

            objects.append(line_item)
        log.debug("saving...")
        DBSession.add_all(objects)
        transaction.commit()

def process_date(datestr, default=datetime(1970,01,01,0,0,0)):
    if datestr:
        return datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")
    else:
        return default
    return None

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)

    config_uri = argv[1]
    options = parse_vars(argv[2:])

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    global cache_dir
    cache_dir = settings['cache.dir'] + "/aws"

    bucket = get_s3_bucket()
    if bucket:
        retrieve_files(bucket)

    # only import the last 6 months of data, maximum.
    min_import_date = datetime.date.today() - relativedelta(months=6)
    load_detailed_line_items(min_import_date)
    load_cost_allocation(min_import_date)

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
