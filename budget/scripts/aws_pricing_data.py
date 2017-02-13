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

from pyramid.paster import (get_appsettings,
                            setup_logging)

from pyramid.scripts.common import parse_vars

from ..models import (DBSession,
                      AwsProduct,
                      AwsPrice)

from ..util.fileloader import load_json, save_json
from ..util.queries.util import insert_or_update

AWS_API_ENDPOINT = 'https://pricing.us-east-1.amazonaws.com'
AWS_PRICING_INDEX = AWS_API_ENDPOINT+'/offers/v1.0/aws/index.json'
PRICE_INDEX = 'index.json'

# How many records to commit in a single transaction.
COMMIT_THRESHOLD = 10000

def usage():
    ''' how to call this program '''
    print "Usage: %s <config_uri> [option=value]" % sys.argv[0]
    sys.exit()

def collect_data():
    ''' fetch pricing data from aws api endpoint '''

    url = urllib2.urlopen(AWS_PRICING_INDEX)
    if not check_etags(PRICE_INDEX, url.headers['ETag']):
        log.debug('fetching %s from %s', PRICE_INDEX, AWS_PRICING_INDEX)
        urllib.urlretrieve(AWS_PRICING_INDEX, cache_dir+PRICE_INDEX)

    index_file = load_json(cache_dir+PRICE_INDEX)

    for offer in index_file['offers']:
        location = index_file['offers'][offer]['currentVersionUrl']
        filename = offer+'.json'

        url = urllib2.urlopen(AWS_API_ENDPOINT+location)
        if not check_etags(filename, url.headers['ETag']):
            log.debug('fetching %s from %s',
                      filename,
                      AWS_API_ENDPOINT+location)
            urllib.urlretrieve(AWS_API_ENDPOINT+location, cache_dir+filename)

def check_etags(filename, etag):
    ''' compare etags retrieved from api endpoint with cached etags
        param: filename of json etag cache
        param: etag to be compared
        return: boolean
    '''
    etag_file = load_json(cache_dir+"/etags.json")

    if filename in etag_file.keys():
        if etag == etag_file[filename]:
            log.debug('%s: etags match!', filename)
            return True

    log.debug('%s: etags do NOT match!', filename)
    etag_file[filename] = etag
    save_json(cache_dir+"etags.json", etag_file)
    return False

def load_products():
    ''' insert product objects into DB '''
    ec2_pricing = load_json(cache_dir+"AmazonEC2.json")

    objects = []
    for product in ec2_pricing['products']:
        if len(objects) > COMMIT_THRESHOLD:
            log.debug("bulk saving...")
            for obj in objects:
                DBSession.merge(obj)
            del objects[:]

        prod = ec2_pricing['products'][product]
        prod_attr = prod['attributes']

        if 'productFamily' not in prod:
            log.debug(prod)
            continue
        if prod['productFamily'] != 'Compute Instance':
            log.debug(prod['productFamily'])
            continue

        kwargs = {'location':prod_attr['location'],
                  'instance_type':prod_attr['instanceType'],
                  'tenancy':prod_attr['tenancy'],
                  'usage_type':prod_attr['usagetype'],
                  'operation':prod_attr['operation'],
                  'operating_system':prod_attr['operatingSystem'],
                  'json':json.dumps(prod)}
        if 'currentGeneration' in prod_attr and \
                prod_attr['currentGeneration'] == 'Yes':
            kwargs['current_generation'] = True
        else:
            kwargs['current_generation'] = False
        obj = insert_or_update(DBSession,
                               AwsProduct,
                               defaults={'sku':prod['sku']},
                               **kwargs)
        objects.append(obj)
    log.debug("saving...")
    for obj in objects:
        DBSession.merge(obj)
    transaction.commit()

def load_prices():
    ''' insert pricing objects into DB '''
    ec2_pricing = load_json(cache_dir+"AmazonEC2.json")

    objects = []
    for pricing in ec2_pricing['terms']:
        for sku in ec2_pricing['terms'][pricing]:
            for term in ec2_pricing['terms'][pricing][sku]:
                if len(objects) > COMMIT_THRESHOLD:
                    log.debug("bulk saving...")
                    for obj in objects:
                        DBSession.merge(obj)
                    del objects[:]

                terms = ec2_pricing['terms'][pricing][sku][term]

                price_dimensions = terms['priceDimensions']
                term_attributes = terms['termAttributes']
                kwargs = {'offer_term_code':terms['offerTermCode'],
                          'price_dimensions':json.dumps(price_dimensions),
                          'term_attributes':json.dumps(term_attributes),
                          'json':json.dumps(term)}
                obj = insert_or_update(DBSession,
                                       AwsPrice,
                                       defaults={'sku':terms['sku']},
                                       **kwargs)
                objects.append(obj)

    log.debug("saving...")
    for obj in objects:
        DBSession.merge(obj)
    transaction.commit()

def main():
    ''' main entry point '''
    if len(sys.argv) < 2:
        usage()
    config_uri = sys.argv[1]
    options = parse_vars(sys.argv[2:])

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    global cache_dir
    cache_dir = settings['cache.dir'] + "/aws_pricing/"

    try:
        delta = datetime.now() - datetime.fromtimestamp(os.path.getmtime(\
                                                    cache_dir+PRICE_INDEX))
        if delta.days > 1 or os.path.getsize(cache_dir+PRICE_INDEX) == 0:
            collect_data()
        else:
            log.error('Data has been downloaded recently. Skipping download...')

        load_products()
        load_prices()
    except OSError as exc:
        log.error(exc.message)

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
