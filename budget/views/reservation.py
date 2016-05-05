# This file Copyright 2012 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Owner:   Brett Lentz
# Created: 2015 Jun
# Purpose: Report statistics on allocation of reserved instances
#

import boto.ec2
import csv
import dateutil.parser
import json
import locale
import logging
import re
import os
import sys
import yaml

from collections import defaultdict
from datetime import datetime, timedelta
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config

from ..util.fileloader import load_json, load_yaml
from ..models import *

ONE_YEAR = 31536000 # 1 year, in seconds
THREE_YEAR = ONE_YEAR * 3

# This is the number of days left in an RI.
#
# If the RI is about to expire, we don't count it as an active RI for purposes
# of making purchasing decisions.
#
# TODO: update the templates and html to enable passing in user-defined values.
DEFAULT_EXPIRATION_THRESHOLD = 60 # days

log = logging.getLogger(__name__)

# adjust boto's logging level.
#logging.getLogger('boto').setLevel(logging.ERROR)

# set Decimal precision
getcontext().prec = 3

# set locale
locale.setlocale(locale.LC_ALL, "en_US")

@view_config(route_name='reservation', match_param='loc=list', renderer='budget:templates/reservation.pt')
def reservation(request):
    log.debug(request.params)

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)
    # send the account-names to the UI for querying
    return { 'results' : sorted(awscreds.keys()) }

#FIXME
@view_config(route_name='reservation', match_param='loc=csv', renderer='budget:templates/reservation_csv.pt')
def reservation_csv(request):
    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)
    header = [ 'Account', 'Zone', 'Type', 'Running', 'Reserved',
                'Delta', 'Hourly', 'Up Front', 'Subtotal', 'Purchase' ]

    data = [ ",".join(header) ]
    for account in awscreds:
        log.debug('fetching reservations for %s' % account)
        results = get_current_reservations(
                    awscreds[account]['access_key'],
                    awscreds[account]['secret_key'] )

        for key in results:
            for item in results[key]:
                item_string = "%s," % account
                for el in item:
                    item_string += "%s," % (el)
                data.append(item_string)

    log.debug(data)
    return { 'results' : data }

@view_config(route_name='reservation',  match_param='loc=data', renderer='json')
def reservation_data(request):
    log.debug(request.params)

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)
    account = request.POST['id']
    access_key = awscreds[account]['access_key']
    secret_key = awscreds[account]['secret_key']

    global cache_dir
    cache_dir = request.registry.settings['cache.dir']

    log.debug('fetching reservations for %s' % account)

    data = []

    regions = boto.ec2.regions()
    for region in regions:
        # skip restricted access regions
        if region.name in [ 'us-gov-west-1', 'cn-north-1' ]:
            continue

        log.debug('checking %s' % region.name)
        ec2 = boto.ec2.connect_to_region(region.name,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)

        reservations = get_reservations(ec2)
        instances = get_instances(ec2)
        stats = calculate_reservation_stats(reservations, instances)
        costs = calculate_costs(stats)
        expirations = get_expirations(reservations)

        #TODO: add detail with number of days remaining on each RI.

        data.append(layout_data(reservations,
                                instances,
                                stats,
                                costs,
                                expirations))

    # flatten data
    data = [x for items in data for x in items]

    # data formatted for jQuery DataTable
    return {
                'draw' : 1,
                'recordsTotal' : len(data),
                'recordsFiltered' : len(data),
                'data' : data
            }

@view_config(route_name='reservation',  match_param='loc=instances', renderer='json')
def reservation_instances(request):
    log.debug(request.params)

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)
    account = request.POST['account']
    access_key = awscreds[account]['access_key']
    secret_key = awscreds[account]['secret_key']

    az = request.POST['availability-zone']
    size = request.POST['instance-type']
    ec2 = boto.ec2.connect_to_region(az[:-1],
                                    aws_access_key_id=access_key,
                                    aws_secret_access_key=secret_key)
    instances = get_instances(ec2, filters={
                                            'instance-state-name':'running',
                                            'instance-type':size,
                                            'availability-zone':az
                                            })

    data = []
    for i in instances:
        if 'Name' in i.tags:
            name = i.tags['Name']
        else:
            name = 'No Name'

        if 'environment' in i.tags:
            env = i.tags['environment']
        else:
            env = 'No Environment'

        data.append({'id':i.id,'name':name,'env':env})

    # data formatted for jQuery DataTable
    return {
                'draw' : 1,
                'recordsTotal' : len(data),
                'recordsFiltered' : len(data),
                'data' : data
            }

#FIXME
@view_config(route_name='reservation',  match_param='loc=purchase', renderer='budget:templates/reservation_purchase.pt')
def reservation_purchase(request):
    log.debug(request.POST)

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)

    data = request.POST
    account = data['account']
    region = data['az'][:-1]

    ec2conn = boto.ec2.connect_to_region(region,
                        aws_access_key_id=awscreds[account]['access_key'],
                        aws_secret_access_key=awscreds[account]['secret_key'])

    offerings = get_reserved_offerings(ec2conn,
                                        target_az=data['az'],
                                        instance_type=data['type'])

    if offerings:
        log.debug("would have called: offerings.purchase(instance_count="+str(data['num'])+", dry_run=True)")
        # See: # https://github.com/boto/boto/blob/develop/boto/ec2/connection.py#3660
        #
        #reservation = offerings.purchase(instance_count=str(data['num']), dry_run=True)
        #log.debug(reservation)
        return { 'results' : 'FAILURE', 'errors' : None }
    else:
        # TODO: alter the return HTTP code to be 500
        request.response.status = 500
        return { 'results' : 'FAILURE', 'errors' : 'FAILURE' }

def get_reservations(ec2conn, filters={'state':'active'}):
    ''' fetch a list of reservations, default is active reservations '''
    results = []

    try:
        results = ec2conn.get_all_reserved_instances(filters=filters)
    except boto.exception.EC2ResponseError as e:
        log.debug("Error communicating with AWS: %s\n\n" % e.message)

    return results

def get_instances(ec2conn, filters={'instance-state-name':'running'}):
    ''' fetch a list of instances, default is running instances '''
    results = []

    try:
        results = ec2conn.get_only_instances(filters=filters)
    except boto.exception.EC2ResponseError as e:
        log.debug("Error communicating with AWS: %s\n\n" % e.message)
    except SSLError  as e:
        log.debug("Error communicating with AWS: %s\n\n" % e.message)

    return results

def calculate_reservation_stats(reservations, instances):
    totals = {}
    running_instances = {}
    reserved_instances = {}

    for inst in instances:
        az   = inst.placement
        size = inst.instance_type

        if (size,az) not in totals.keys():
            totals[(size,az)] = defaultdict(lambda: 0)

        # do a count of each type/az combination
        running_instances[(size,az)] = running_instances.get((size,az),0)+1
        totals[(size,az)]['running'] = totals[(size,az)].get('running',0)+1

    for ri in reservations:
        az   = ri.availability_zone
        size = ri.instance_type

        if (size,az) not in totals.keys():
            totals[(size,az)] = defaultdict(lambda: 0)

        reserved_instances[(size,az)] = reserved_instances.get((size,az),0)+ri.instance_count
        totals[(size,az)]['reserved'] = totals[(size,az)].get('reserved',0)+ri.instance_count


    # for each type/az combination, the diff will be
    # - postive if we have unused reservations
    # - negative if there are on-demand instances
    diff = dict([(x,reserved_instances[x]-running_instances.get(x,0)) for x in reserved_instances])

    # diff only has keys present in reserved_instances.
    # now we add the keys from running_instances
    for placement in running_instances:
        if not placement in reserved_instances:
            diff[placement] = -running_instances[placement]

    return { "delta" : diff, "totals" : totals }

def calculate_costs(stats):
    cost = {}

    for (size,az) in stats['totals']:
        if (size,az) not in cost:
            cost[(size,az)] = {}

        delta = stats['delta'][(size,az)]

        if delta < 0:
            ri = get_price(instance_type=size,
                        region=az[:-1],
                        pricing='Reserved',
                        lease_contract_length='1yr',
                        purchase_option='Partial Upfront')
            cost[(size,az)]['up-front'] = ri['Quantity'] * -delta
        else:
            cost[(size,az)]['up-front'] = 0

            # calc savings of reserved over on-demand.
        if stats['delta'][(size,az)] != 0:
            savings = calculate_monthly_savings(size, az[:-1]) * -delta
            cost[(size,az)]['savings'] = savings
        else:
            cost[(size,az)]['savings'] = 0

    return cost

def calculate_monthly_savings(instance_type, region):
    od_price = get_price(instance_type=instance_type, region=region)
    ri_price = get_price(instance_type=instance_type,
                        region=region,
                        pricing='Reserved',
                        lease_contract_length='1yr',
                        purchase_option='Partial Upfront')

    monthly_on_demand = od_price['Hrs'] * 24 * 30
    monthly_ri_amortized = (ri_price['Hrs'] * 24 * 30) + \
                            (ri_price['Quantity'] / 12)
    return (monthly_on_demand - monthly_ri_amortized)

def get_price(instance_type='t1.micro', region='us-east-1', tenancy='Shared',
        pricing='OnDemand', **kwargs):
    ''' Digs through a massive nest of json data to extract the on demand
    pricing for AWS instances.

    See also:
    https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html

    Params:

    instance_type: any valid AWS instance size. (e.g. 'm4.xlarge')
    region: an AWS region endpoint name. (e.g. 'us-east-1')
    tenancy: 'Shared' or 'Dedicated'
    pricing: 'OnDemand' or 'Reserved'
    lease_contract_length: '1yr' or '3yr'
    purchase_option: 'No Upfront' or 'Partial Upfront' or 'Full Upfront'

    Returns:

    dict: key - 'Hrs' or 'Quantity'
          value - Decimal
    '''

    region_name = region_lookup(region)

    products = DBSession.query(
                    AwsPrice.price_dimensions,
                    AwsPrice.term_attributes
              ).filter(
                    AwsProduct.instance_type == instance_type,
                    AwsProduct.location == region_name,
                    AwsProduct.tenancy == tenancy,
                    AwsProduct.operating_system == 'Linux',
                    AwsPrice.sku == AwsProduct.sku
              ).all()

    log.debug('%s, %s, %s - %s results returned' % (instance_type, region,
                                                    pricing, len(products)))
    costs = {}
    for (d, t) in products:
        price_dimensions = json.loads(d)
        term_attributes = json.loads(t)

        if pricing == 'OnDemand':
            rgx = re.compile(r'On Demand Linux %s' % instance_type)
            costs = _find_cost(rgx, price_dimensions)
        elif pricing == 'Reserved':
            # On-Demand has no term_attributes
            if term_attributes == {}:
                continue

            if term_attributes['LeaseContractLength'] == kwargs['lease_contract_length'] and \
                    term_attributes['PurchaseOption'] == kwargs['purchase_option']:
                rgx = re.compile(r'Linux/UNIX.*%s' % instance_type)
                costs = _find_cost(rgx, price_dimensions)

        if costs != {}:
            return costs
    return costs

def _find_cost(regex, price_dimensions):
    costs = {}
    matched = False
    for dim in price_dimensions:
        rate = price_dimensions[dim]['pricePerUnit']['USD']
        units = price_dimensions[dim]['unit']
        costs[units] = Decimal(rate)

        desc = price_dimensions[dim]['description']
        if regex.search(desc):
            matched = True
    if matched:
        return costs
    return {}

def region_lookup(region='us-east-1'):
    ''' AWS doesn't provide a mapping between the "location" name they use in
    the pricing files and the "region" name used everywhere else in the API.

    So, I've crafted a JSON mapping file based on this table:
    https://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region

    Nothing can ever be easy...  >_<
    '''
    ec2_region_map = load_json(cache_dir+"/aws_pricing/ec2_region_map.json")

    for x in ec2_region_map:
        if x['region'] == region:
            return x['region_name']
    return None

def calculate_days_left(reserved_instance):
    start_date = dateutil.parser.parse(reserved_instance.start)
    end_date   = start_date + timedelta(0,reserved_instance.duration)
    today      = datetime.now(dateutil.tz.tzlocal())
    return (end_date - today).days

def get_expirations(reservations):
    ''' given a list of ReservedInstances, return their expiration dates and
    number of instances expiring '''

    data = defaultdict(lambda: [])
    for reservation in reservations:
        az = reservation.availability_zone
        size = reservation.instance_type

        data_dict = {
                'end_date' : dateutil.parser.parse(reservation.end).strftime("%Y-%m-%d %H:%M:%S"),
                'count' : reservation.instance_count,
                'days_left' : calculate_days_left(reservation)
            }
        data[(size,az)].append(data_dict)
    return data

def layout_data(reservations, instances, stats, costs, expirations):
    ''' format the data in the way expected by the dataTable '''
    data = []

    for (size, az) in stats['totals']:
        data.append({
            'zone' : str(az),
            'type' : str(size),
            'running' : stats['totals'][(size,az)]['running'],
            'reserved' : stats['totals'][(size,az)]['reserved'],
            'delta' : stats['delta'][(size,az)],
            'upfront' : locale.currency(costs[(size,az)]['up-front'],
                                        grouping=True),
            'savings' : locale.currency(costs[(size,az)]['savings'],
                                        grouping=True),
            'expiration' : expirations[(size,az)]
        })

    return data
