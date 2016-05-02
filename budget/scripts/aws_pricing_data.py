#!/usr/bin/env python

import json
import logging
import os
import sys
import transaction
import urllib
import urllib2

from datetime import datetime

from sqlalchemy import engine_from_config
from sqlalchemy.sql import functions

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
                        DBSession,
                        AwsProduct,
                        AwsPrice,
                        Base,
                    )

from ..util.fileloader import load_json, save_json

aws_api_endpoint = 'https://pricing.us-east-1.amazonaws.com'
aws_pricing_index = aws_api_endpoint+'/offers/v1.0/aws/index.json'
price_index = 'index.json'

# How many records to commit in a single transaction.
COMMIT_THRESHOLD = 10000

def collect_data():
    url = urllib2.urlopen(aws_pricing_index)
    if not check_etags(price_index, url.headers['ETag']):
        log.debug('fetching %s from %s' % (price_index, aws_pricing_index))
        urllib.urlretrieve(aws_pricing_index, cache_dir+price_index)

    index_file = load_json(cache_dir+price_index)

    for offer in index_file['offers']:
        location = index_file['offers'][offer]['currentVersionUrl']
        filename = offer+'.json'

        url = urllib2.urlopen(aws_api_endpoint+location)
        if not check_etags(filename, url.headers['ETag']):
            log.debug('fetching %s from %s' % (filename, aws_api_endpoint+location))
            urllib.urlretrieve(aws_api_endpoint+location, cache_dir+filename)

def check_etags(filename, etag):
    etag_file = load_json(cache_dir+"/etags.json")

    if filename in etag_file.keys():
        if etag == etag_file[filename]:
            log.debug('etags match!')
            return True

    log.debug('etags do NOT match!')
    etag_file[filename] = etag
    save_json(cache_dir+"etags.json", etag_file)
    return False

def load_products():
    ec2_pricing = load_json(cache_dir+"AmazonEC2.json")

    objects = []
    for product in ec2_pricing['products']:
        if len(objects) > COMMIT_THRESHOLD:
            log.debug("bulk saving...")
            DBSession.add_all(objects)
            transaction.commit()
            del objects[:]

        prod = ec2_pricing['products'][product]
        prod_attr = prod['attributes']

        if 'productFamily' not in prod:
            log.debug(prod)
            continue
        if prod['productFamily'] != 'Compute Instance':
            log.debug(prod['productFamily'])
            continue

        line_item = AwsProduct(
                        sku = prod['sku'],
                        location = prod_attr['location'],
                        instance_type = prod_attr['instanceType'],
                        tenancy = prod_attr['tenancy'],
                        usage_type = prod_attr['usagetype'],
                        operation = prod_attr['operation'],
                        operating_system = prod_attr['operatingSystem'],
                        json = json.dumps(prod)
                    )
        if 'currentGeneration' in prod_attr and prod_attr['currentGeneration'] == 'Yes':
            line_item.current_generation = True
        else:
            line_item.current_generation = False
        objects.append(line_item)
    log.debug("saving...")
    DBSession.add_all(objects)
    transaction.commit()

def load_prices():
    ec2_pricing = load_json(cache_dir+"AmazonEC2.json")

    objects = []
    for pricing in ec2_pricing['terms']:
        for sku in ec2_pricing['terms'][pricing]:
            for term in ec2_pricing['terms'][pricing][sku]:
                if len(objects) > COMMIT_THRESHOLD:
                    log.debug("bulk saving...")
                    DBSession.add_all(objects)
                    transaction.commit()
                    del objects[:]

                terms = ec2_pricing['terms'][pricing][sku][term]

                price_dimensions = terms['priceDimensions']
                term_attributes = terms['termAttributes']
                line_item = AwsPrice(
                                        sku = terms['sku'],
                                        offer_term_code = terms['offerTermCode'],
                                        price_dimensions = json.dumps(price_dimensions),
                                        term_attributes = json.dumps(term_attributes),
                                        json = json.dumps(term)
                                    )
                objects.append(line_item)
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

    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    global cache_dir
    cache_dir = settings['cache.dir'] + "/aws_pricing/"

    try:
        delta = datetime.now() - datetime.fromtimestamp(os.path.getmtime(cache_dir+price_index))
        if delta.days > 1 or os.path.getsize(cache_dir+price_index) == 0:
            collect_data()
        else:
            log.error('Data has been downloaded recently. Skipping download...')

        load_products()
        load_prices()
    except OSError as e:
        log.error(e.message)

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
