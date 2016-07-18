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

import boto
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

from ..util.nvd3js.charts.discretebar import DiscreteBarChart
from ..util.fileloader import load_json, load_yaml
from ..util.addset import addset
from ..models import *

# TODO: move this to config file.
PURCHASE_DRY_RUN = True

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

class DataHolder(object):
    ''' object for storing data. it's a glorified struct '''
    def __init__(self, **kwargs):
        self.put(**kwargs)

    def __repr__(self):
        return "%s: %s" % (self.__class__, self.__dict__)

    def put(self, **kwargs):
        ''' assign arbitrary data to instance variables '''
        for key, value in kwargs.items():
            setattr(self, key, value)

@view_config(route_name='reservation', match_param='loc=list', renderer='budget:templates/reservation.pt')
def reservation(request):
    # empty pass-through to facilitate loading the page while sourcing the real
    # data through an ajax call.
    return {}

@view_config(route_name='reservation', match_param='loc=csv', renderer='csv')
def reservation_csv(request):
    log.debug(request.params)

    global cache_dir
    cache_dir = request.registry.settings['cache.dir']

    # override attributes of response
    filename = 'ri-report.csv'
    request.response.content_disposition = 'attachment;filename=' + filename

    header = [ 'Zone', 'Type', 'Running', 'Reserved', 'Delta', 'Up Front' ]

    rows = compile_data(request)
    rows = layout_data_for_csv(rows)
    log.debug(rows)
    return { 'header': header, 'rows': rows }

@view_config(route_name='reservation',  match_param='loc=data', renderer='json')
def reservation_data(request):
    log.debug(request.params)

    global cache_dir
    cache_dir = request.registry.settings['cache.dir']

    data = compile_data(request)

    # data formatted for jQuery DataTable
    return {
                'draw' : 1,
                'recordsTotal' : len(data),
                'recordsFiltered' : len(data),
                'data' : layout_data_for_web(data)
            }

@view_config(route_name='reservation',  match_param='loc=instances', renderer='json')
def reservation_instances(request):
    log.debug(request.params)

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    accounts = sorted(load_yaml(creds_file).keys())

    az = request.POST['availability-zone']
    size = request.POST['instance-type']

    data = []
    for account in accounts:
        num = get_account_number(account, request.registry.settings)
        inst = get_instances(num)
        for i in inst:
            if i.availability_zone == az and i.instance_type == size:
                data.append({'account' : account,
                         'id' : i.instance_id,
                        'name' : i.name,
                        'env' : i.environment})

    # data formatted for jQuery DataTable
    return {
                'draw' : 1,
                'recordsTotal' : len(data),
                'recordsFiltered' : len(data),
                'data' : data
            }

@view_config(route_name='reservation',  match_param='loc=purchase', renderer='json')
def reservation_purchase(request):
    log.debug(request.POST)

    data = request.POST
    account = data['account']
    region = data['availability_zone'][:-1]

    access_key, secret_key = get_creds(account, request.registry.settings)

    ec2conn = boto.ec2.connect_to_region(region,
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key)

    offerings = get_reservation_offerings(ec2conn,
                                        availability_zone=data['availability_zone'],
                                        instance_type=data['instance_type'])

    if len(offerings) == 1:
        log.debug(offerings[0].describe())
        # See: # https://github.com/boto/boto/blob/develop/boto/ec2/connection.py#3660
        #
        try:
            reservation = offerings[0].purchase(instance_count=str(data['amount']), dry_run=PURCHASE_DRY_RUN)
            log.debug(reservation)
        except boto.exception.EC2ResponseError as e:
            request.response.status = 500
            log.error(e.message)
            return { 'results' : 'FAIL', 'errors' : e.message }
        return { 'results' : 'SUCCESS', 'errors' : None }
    else:
        request.response.status = 500
        log.error('reservation purchase failed: %s' % offerings)
        return { 'results' : 'FAIL', 'errors' : offerings }

@view_config(route_name='reservation', match_param='loc=expiration-graph', renderer='budget:templates/structure.pt')
def reservation_expiration_graph(request):
    log.debug(request.params)

    expirations = None
    data = {}

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    accounts = sorted(load_yaml(creds_file).keys())
    for account in accounts:

        num = get_account_number(account, request.registry.settings)
        res = get_reservations(num)

        for r in res:
            tup = (r.instance_type, r.availability_zone)

            if tup not in data.keys():
                dh = DataHolder(
                            instance_type=r.instance_type,
                            availability_zone=r.availability_zone,
                            instances={},
                            reservations={}
                        )
                data[tup] = dh
            if account in data[tup].reservations.keys():
                data[tup].reservations[account].append(r)
            else:
                data[tup].reservations[account] = [r]


    g_data = {}
    for tup, dh in data.items():
        dh = get_expirations(dh)

        for ri in dh.ri_expirations[tup]:
            addset(g_data, ri['end_date'], ri['count'])

    if not data:
        log.info('no graph data')
        return { 'data' : 'No graph to show' }

    graph_data = []
    for key in sorted(g_data.keys()):
        graph_data.append({ 'label': key,
                            'value': int(g_data[key])})

    graph = DiscreteBarChart(stagger_labels='true')
    graph.data = [{ 'key' : 'reservations', 'values' : graph_data}]

    return { 'data' : graph }

#########################################################
# Helper methods
#########################################################

def get_creds(account, settings):
    ''' quick helper function to return account creds when given an account name
    '''
    creds_file = settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)
    access_key = awscreds[account]['access_key']
    secret_key = awscreds[account]['secret_key']
    return (access_key, secret_key)

def get_account_number(name, settings):
    ''' quick helper function to return an account number when given an account name
    '''
    creds_file = settings['creds.dir'] + "/creds.yaml"
    return load_yaml(creds_file)[name]['account']

def get_reservations(account):
    ''' fetch a list of active reservations from the DB '''
    results = DBSession.query(AwsReservationInventory).filter(
                    AwsReservationInventory.account == account,
                    AwsReservationInventory.expiration_date >= datetime.now(),
                    AwsReservationInventory.purchase_date <= datetime.now()
                ).all()
    return results

def get_reservation_offerings(ec2conn,
                            instance_type=None,
                            availability_zone=None,
                            product_description='Linux/UNIX (Amazon VPC)',
                            offering_type='Partial Upfront',
                            instance_tenancy='default',
                            min_duration=0,
                            max_duration=ONE_YEAR,
                            filters={}):
    ''' fetch a list of reserved instance offerings from AWS '''
    results = []

    try:
        results = ec2conn.get_all_reserved_instances_offerings(
                        instance_type=instance_type,
                        availability_zone=availability_zone,
                        product_description=product_description,
                        offering_type=offering_type,
                        instance_tenancy=instance_tenancy,
                        min_duration=min_duration,
                        max_duration=max_duration,
                        filters=filters
                    )
    except boto.exception.EC2ResponseError as e:
        log.error("Error communicating with AWS: %s\n\n" % e.message)

    return results

def get_instances(account):
    ''' fetch a list of running instances from the DB '''
    results = DBSession.query(AwsInstanceInventory).filter(
                    AwsInstanceInventory.status == 'running',
                    AwsInstanceInventory.account == account,
                ).all()
    return results

def calculate_reservation_stats(data_holder):
    ''' caclculate the differences between running and reserved instances.
        reports on totals and deltas by returning an updated DataHolder object.
    '''
    totals = {}
    running_instances = {}
    reserved_instances = {}

    for account, inst_list in data_holder.instances.items():
        for inst in inst_list:
            az   = inst.availability_zone
            size = inst.instance_type

            if (size,az) not in totals.keys():
                totals[(size,az)] = defaultdict(lambda: 0)

            # do a count of each type/az combination
            running_instances[(size,az)] = running_instances.get((size,az),0)+1
            totals[(size,az)]['running'] = totals[(size,az)].get('running',0)+1

    for account, ri_list in data_holder.reservations.items():
        for ri in ri_list:
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

    data_holder.put(ri_delta=diff, ri_totals=totals)
    return data_holder

def calculate_costs(data_holder, cache={}):
    ''' calculate the cost differences between On-Demand and Reserved Instance
        pricing.

        Each DataHolder has a list of instances and reservations that need to
        be calculated against. Each combination of instance-size and
        availability-zone is considered individually, because prices differ based
        on these two variables. As a result, an in-memory cache of size/AZ
        prices is built to reduce the number of DB queries required to
        calculate cost differences for all data in the data_holder.
    '''
    cost = {}

    for (size,az) in data_holder.ri_totals:
        if (size,az) not in cost:
            cost[(size,az)] = {}

        delta = data_holder.ri_delta[(size,az)]

        r_kwargs = { 'instance_type' : size,
                        'region' : az[:-1],
                        'pricing' : 'Reserved',
                        'lease_contract_length' : '1yr',
                        'purchase_option' : 'Partial Upfront' }
        od_params = (size, az[:-1], 'On-Demand')
        r_params = (size, az[:-1], 'Reserved')

        if delta < 0:
            if r_params in cache.keys():
                ri = cache[r_params]
            else:
                ri = get_price(**r_kwargs)
                cache[r_params] = ri
            cost[(size,az)]['up-front'] = ri['Quantity'] * -delta
        else:
            cost[(size,az)]['up-front'] = 0

        if data_holder.ri_delta[(size,az)] != 0:
            # calc savings of reserved over on-demand.
            if od_params in cache.keys():
                od_price = cache[od_params]
            else:
                od_price = get_price(instance_type=size, region=az[:-1])
                cache[od_params] = od_price

            if r_params in cache.keys():
                ri_price = cache[r_params]
            else:
                ri_price = get_price(**r_kwargs)
                cache[r_params] = ri_price

            monthly_on_demand = od_price['Hrs'] * 24 * 30
            monthly_ri_amortized = (ri_price['Hrs'] * 24 * 30) + \
                                    (ri_price['Quantity'] / 12)
            savings = (monthly_on_demand - monthly_ri_amortized) * -delta
            cost[(size,az)]['savings'] = savings
        else:
            cost[(size,az)]['savings'] = 0

    data_holder.put(ri_costs=cost)
    return (data_holder, cache)

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

        dict: key   - 'Hrs' or 'Quantity'
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
    ''' the price dimension portion of the AWS Pricing data is deeply nested.
        this method extracts the elements of that data we care about.
    '''
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

        This method interprets a JSON mapping file based on this table:
        https://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region
    '''
    ec2_region_map = load_json(cache_dir+"/aws_pricing/ec2_region_map.json")

    for x in ec2_region_map:
        if x['region'] == region:
            return x['region_name']
    return None

def get_expirations(data_holder):
    ''' given a list of ReservedInstances, return their expiration dates and
        the number of instances expiring
    '''

    data = defaultdict(lambda: [])
    for account, ri_list in data_holder.reservations.items():
        for reservation in ri_list:
            az = reservation.availability_zone
            size = reservation.instance_type

            data_dict = {
                    'account' : account,
                    'end_date' : reservation.expiration_date.strftime("%Y-%m-%d"),
                    'count' : reservation.instance_count,
                    'days_left' : (reservation.expiration_date - datetime.now()).days
                    }
            data[(size,az)].append(data_dict)
    data_holder.put(ri_expirations=data)
    return data_holder

def layout_data_for_web(data):
    ''' format the data in the way expected by the DataTable '''

    # each table row has these fields:
    # Expiration Details | AZ | Type | Running | Reserved | Delta | Up-Front | Savings
    table_rows = []

    for tup, dh in data.items():
        row = {
                'zone' : tup[1],
                'type' : tup[0],
                'running' : dh.ri_totals[tup]['running'],
                'reserved' : dh.ri_totals[tup]['reserved'],
                'delta' : dh.ri_delta[tup],
                'upfront' : locale.currency(dh.ri_costs[tup]['up-front'], grouping=True),
                'savings' : locale.currency(dh.ri_costs[tup]['savings'], grouping=True),
                'expiration' : dh.ri_expirations[tup],
            }
        table_rows.append(row)
    return table_rows

def layout_data_for_csv(data):
    ''' format the data for consumption as a CSV  '''

    # each table row has these fields:
    #  AZ | Type | Running | Reserved | Delta | Up-Front
    table_rows = []

    for tup, dh in data.items():
        row = [
                tup[1], # zone
                tup[0], # type
                dh.ri_totals[tup]['running'], # running
                dh.ri_totals[tup]['reserved'], # reserved
                dh.ri_delta[tup], # delta
                dh.ri_costs[tup]['up-front'], # up-front
            ]
        table_rows.append(row)
    return table_rows

def compile_data(request):
    ''' compile instance and RI information into a collection of DataHolder
        objects that can be manipulated into the desired presentation layout
    '''
    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    accounts = sorted(load_yaml(creds_file).keys())

    data = {}
    for account in accounts:

        num = get_account_number(account, request.registry.settings)
        res = get_reservations(num)
        inst = get_instances(num)

        for i in inst:
            tup = (i.instance_type, i.availability_zone)

            if tup not in data.keys():
                dh = DataHolder(
                            instance_type=i.instance_type,
                            availability_zone=i.availability_zone,
                            instances={},
                            reservations={}
                        )
                data[tup] = dh

            if account in data[tup].instances.keys():
                data[tup].instances[account].append(i)
            else:
                data[tup].instances[account] = [i]

        for r in res:
            tup = (r.instance_type, r.availability_zone)

            if tup not in data.keys():
                dh = DataHolder(
                            instance_type=r.instance_type,
                            availability_zone=r.availability_zone,
                            instances={},
                            reservations={}
                        )
                data[tup] = dh
            if account in data[tup].reservations.keys():
                data[tup].reservations[account].append(r)
            else:
                data[tup].reservations[account] = [r]

    query_cache = {}
    for tup, dh in data.items():
        dh = calculate_reservation_stats(dh)
        dh, query_cache = calculate_costs(dh, query_cache)
        dh = get_expirations(dh)
        data[tup] = dh

    return data

