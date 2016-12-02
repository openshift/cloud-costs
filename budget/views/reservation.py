''' A view that tabulates AWS reserved instances against the inventory of
    running instances.
'''

import boto3
import json
import locale
import logging
import re

from collections import defaultdict
from datetime import datetime
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config

from budget.util.nvd3js import *
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

@view_config(route_name='reservation',
             match_param='loc=list',
             renderer='budget:templates/reservation.pt')
def reservation(request):
    ''' empty pass-through to facilitate loading the page while sourcing the
        real data through an ajax call.
    '''
    return {}

@view_config(route_name='reservation', match_param='loc=csv', renderer='csv')
def reservation_csv(request):
    ''' Output reservation data as CSV '''
    log.debug(request.params)

    # override attributes of response
    filename = 'ri-report.csv'
    request.response.content_disposition = 'attachment;filename=' + filename

    header = ['Zone', 'Type', 'Running', 'Reserved', 'Delta', 'Up Front']

    rows = compile_data(request)
    rows = layout_data_for_csv(rows)
    log.debug(rows)
    return {'header': header, 'rows': rows}

@view_config(route_name='reservation', match_param='loc=data', renderer='json')
def reservation_data(request):
    ''' Deliver compiled data to the View as JSON. Called by AJAX query. '''
    log.debug(request.params)

    data = compile_data(request)

    # data formatted for jQuery DataTable
    return {'draw' : 1,
            'recordsTotal' : len(data),
            'recordsFiltered' : len(data),
            'data' : layout_data_for_web(data)}

@view_config(route_name='reservation',
             match_param='loc=instances',
             renderer='json')
def reservation_instances(request):
    ''' Deliver instance data to the View as JSON. Called by AJAX query. '''
    log.debug(request.params)

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    accounts = sorted(load_yaml(creds_file).keys())

    zone = request.POST['availability-zone']
    size = request.POST['instance-type']

    data = []
    for account in accounts:
        num = get_account_number(account, request.registry.settings)
        inst = get_instances(num)
        for i in inst:
            if i.availability_zone == zone and i.instance_type == size:
                data.append({'account' : account,
                             'id' : i.instance_id,
                             'name' : i.name,
                             'env' : i.environment})

    # data formatted for jQuery DataTable
    return {'draw' : 1,
            'recordsTotal' : len(data),
            'recordsFiltered' : len(data),
            'data' : data}

@view_config(route_name='reservation',
             match_param='loc=search_offerings',
             renderer='json')
def reservation_search(request):
    ''' search for reservation offerings using the supplied POST params '''
    log.debug(request.POST)
    data = request.POST
    account = data['account']
    region = data['region']
    access_key, secret_key = get_creds(account, request.registry.settings)

    ec2 = boto3.client('ec2',
                       region,
                       aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key)

    response = {}
    try:
        offerings = get_reservation_offerings(ec2,\
                                availability_zone=data['availability_zone'],\
                                instance_type=data['instance_type'],\
                                product_description=[data['platform']],\
                                offering_type=data['payment_option'],\
                                offering_class=data['offering_class'],\
                                min_duration=int(data['min_duration']),\
                                max_duration=int(data['max_duration']))
        log.debug(offerings)
        response = {'offerings':offerings}
    except boto3.exceptions.Boto3Error as exc:
        log.error("Error communicating with AWS: %s\n\n", exc.message)
        response = {'errors':exc.message}

    return response

@view_config(route_name='reservation',
             match_param='loc=purchase',
             renderer='json')
def reservation_purchase(request):
    ''' Execute an RI purchase.

        ****************************
        IMPORTANT: THIS SPENDS MONEY
        ****************************
    '''
    log.debug(request.POST)

    data = request.POST
    account = data['account']
    region = data['region']

    access_key, secret_key = get_creds(account, request.registry.settings)

    ec2 = boto3.client('ec2',
                       region,
                       aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key)

    offerings = get_reservation_offerings(ec2,\
                                availability_zone=data['availability_zone'],\
                                instance_type=data['instance_type'],\
                                filters={'offeringClass':'convertible'})

    if len(offerings) == 1:
        log.debug(offerings[0].describe())
        # See:
        # https://github.com/boto/boto/blob/develop/boto/ec2/connection.py#3660
        #
        try:
            reserved = offerings[0].purchase(instance_count=str(data['amount']),
                                             dry_run=PURCHASE_DRY_RUN)
            log.debug(reserved)
        except boto3.exceptions.Boto3Error as exc:
            request.response.status = 500
            log.error(exc.message)
            return {'results' : 'FAIL', 'errors' : exc.message}
        return {'results' : 'SUCCESS', 'errors' : None}
    else:
        request.response.status = 500
        log.error('reservation purchase failed: %s', offerings)
        return {'results' : 'FAIL', 'errors' : offerings}

@view_config(route_name='reservation',
             match_param='loc=expiration-graph',
             renderer='budget:templates/structure.pt')
def reservation_expiration_graph(request):
    ''' output an nvd3 graph to show rate of RI expiration '''
    log.debug(request.params)

    data = {}

    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    accounts = sorted(load_yaml(creds_file).keys())
    for account in accounts:

        num = get_account_number(account, request.registry.settings)
        res = get_reservations(num)

        for rsrv in res:
            tup = (rsrv.instance_type, rsrv.availability_zone)

            if tup not in data.keys():
                holder = DataHolder(instance_type=rsrv.instance_type,
                                    availability_zone=rsrv.availability_zone,
                                    instances={},
                                    reservations={})
                data[tup] = holder
            if account in data[tup].reservations.keys():
                data[tup].reservations[account].append(rsrv)
            else:
                data[tup].reservations[account] = [rsrv]


    g_data = {}
    for tup, holder in data.items():
        holder = get_expirations(holder)

        for rsrv in holder.ri_expirations[tup]:
            addset(g_data, rsrv['end_date'], rsrv['count'])

    if not data:
        log.info('no graph data')
        return {'data' : 'No graph to show'}

    graph_data = []
    for key in sorted(g_data.keys()):
        graph_data.append({'label': key,
                           'value': int(g_data[key])})

    graph = DiscreteBarChart(staggerLabels='true')
    graph.data = [{'key' : 'reservations', 'values' : graph_data}]

    return {'data' : graph}

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
    ''' quick helper function to return an account number when given an account
        name
    '''
    creds_file = settings['creds.dir'] + "/creds.yaml"
    return load_yaml(creds_file)[name]['account']

def get_reservations(account):
    ''' fetch a list of active reservations from the DB '''
    results = DBSession.query(AwsReservationInventory).filter(\
                AwsReservationInventory.account == account,
                AwsReservationInventory.expiration_date >= datetime.now(),
                AwsReservationInventory.purchase_date <= datetime.now()).all()
    return results

def get_reservation_offerings(ec2client,
                              instance_type=None,
                              availability_zone=None,
                              product_description=['Linux/UNIX (Amazon VPC)'],
                              offering_type='Partial Upfront',
                              offering_class='convertible',
                              instance_tenancy='default',
                              min_duration=0,
                              max_duration=ONE_YEAR,
                              filters=None):
    ''' fetch a list of reserved instance offerings from AWS '''
    if not filters:
        filters = []
    filters.append({'Name':'product-description', 'Values':product_description})
    kwargs = {'InstanceType':instance_type,
              'OfferingType':offering_type,
              'OfferingClass':offering_class,
              'InstanceTenancy':instance_tenancy,
              'MinDuration':min_duration,
              'MaxDuration':max_duration,
              'Filters':filters}
    if availability_zone:
        kwargs['AvailabilityZone'] = availability_zone

    results = ec2client.describe_reserved_instances_offerings(**kwargs)
    return results['ReservedInstancesOfferings']

def get_instances(account):
    ''' fetch a list of running instances from the DB '''
    results = DBSession.query(AwsInstanceInventory).filter(\
                    AwsInstanceInventory.status == 'running',
                    AwsInstanceInventory.account == account).all()
    return results

def calculate_reservation_stats(data_holder):
    ''' calculate the differences between running and reserved instances.
        reports on totals and deltas by returning an updated DataHolder object.
    '''
    totals = {}
    running_instances = {}
    reserved_instances = {}

    for _, inst_list in data_holder.instances.items():
        for inst in inst_list:
            zone = inst.availability_zone
            size = inst.instance_type

            if (size, zone) not in totals.keys():
                totals[(size, zone)] = defaultdict(lambda: 0)

            # do a count of each type/zone combination
            running_instances[(size, zone)] = running_instances.get((size, zone), 0)+1
            totals[(size, zone)]['running'] = totals[(size, zone)].get('running', 0)+1

    for _, ri_list in data_holder.reservations.items():
        for rsrv in ri_list:
            zone = rsrv.availability_zone
            size = rsrv.instance_type

            if (size, zone) not in totals.keys():
                totals[(size, zone)] = defaultdict(lambda: 0)

            reserved_instances[(size, zone)] = reserved_instances.get((size, zone), 0)+rsrv.instance_count
            totals[(size, zone)]['reserved'] = totals[(size, zone)].get('reserved', 0)+rsrv.instance_count

    # for each type/zone combination, the diff will be
    # - postive if we have unused reservations
    # - negative if there are on-demand instances
    diff = dict([(x, reserved_instances[x]-running_instances.get(x, 0)) for x in reserved_instances])

    # diff only has keys present in reserved_instances.
    # now we add the keys from running_instances
    for placement in running_instances:
        if not placement in reserved_instances:
            diff[placement] = -running_instances[placement]

    data_holder.put(ri_delta=diff, ri_totals=totals)
    return data_holder

def calculate_costs(request, data_holder, cache=None):
    ''' calculate the cost differences between On-Demand and Reserved Instance
        pricing.

        Each DataHolder has a list of instances and reservations that need to
        be calculated against. Each combination of instance-size and
        availability-zone is considered individually, because prices differ
        based on these two variables. As a result, an in-memory cache of size/AZ
        prices is built to reduce the number of DB queries required to
        calculate cost differences for all data in the data_holder.
    '''
    cost = {}
    if not cache:
        cache = {}

    for (size, zone) in data_holder.ri_totals:
        if (size, zone) not in cost:
            cost[(size, zone)] = {}

        delta = data_holder.ri_delta[(size, zone)]

        r_kwargs = {'instance_type' : size,
                    'region' : zone[:-1],
                    'pricing' : 'Reserved',
                    'lease_contract_length' : '1yr',
                    'purchase_option' : 'Partial Upfront'}
        od_params = (size, zone[:-1], 'On-Demand')
        r_params = (size, zone[:-1], 'Reserved')

        if delta < 0:
            if r_params in cache.keys():
                rsrv = cache[r_params]
            else:
                rsrv = get_price(request, **r_kwargs)
                cache[r_params] = rsrv
            cost[(size, zone)]['up-front'] = rsrv['Quantity'] * -delta
        else:
            cost[(size, zone)]['up-front'] = 0

        if data_holder.ri_delta[(size, zone)] != 0:
            # calc savings of reserved over on-demand.
            if od_params in cache.keys():
                od_price = cache[od_params]
            else:
                od_price = get_price(request, instance_type=size, region=zone[:-1])
                cache[od_params] = od_price

            if r_params in cache.keys():
                rsrv_price = cache[r_params]
            else:
                rsrv_price = get_price(request, **r_kwargs)
                cache[r_params] = rsrv_price

            monthly_on_demand = od_price['Hrs'] * 24 * 30
            monthly_rsrv_amortized = (rsrv_price['Hrs'] * 24 * 30) + \
                                    (rsrv_price['Quantity'] / 12)
            savings = (monthly_on_demand - monthly_rsrv_amortized) * -delta
            cost[(size, zone)]['savings'] = savings
        else:
            cost[(size, zone)]['savings'] = 0

    data_holder.put(ri_costs=cost)
    return (data_holder, cache)

def get_price(request,
              instance_type='t1.micro',
              region='us-east-1',
              tenancy='Shared',
              pricing='OnDemand',
              **kwargs):
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

    region_name = region_lookup(request, region)
    products = DBSession.query(AwsPrice.price_dimensions,
                               AwsPrice.term_attributes
                              ).filter(\
                    AwsProduct.instance_type == instance_type,
                    AwsProduct.location == region_name,
                    AwsProduct.tenancy == tenancy,
                    AwsProduct.operating_system == 'Linux',
                    AwsPrice.sku == AwsProduct.sku).all()

    costs = {}
    for (dim, term) in products:
        price_dimensions = json.loads(dim)
        term_attributes = json.loads(term)

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

def region_lookup(request, region='us-east-1'):
    ''' AWS doesn't provide a mapping between the "location" name they use in
        the pricing files and the "region" name used everywhere else in the API.

        This method interprets a JSON mapping file based on this table:
        https://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region
    '''
    cache_dir = request.registry.settings['cache.dir']
    ec2_region_map = load_json(cache_dir+"/aws_pricing/ec2_region_map.json")

    for reg in ec2_region_map:
        if reg['region'] == region:
            return reg['region_name']
    return None

def get_expirations(data_holder):
    ''' given a list of ReservedInstances, return their expiration dates and
        the number of instances expiring
    '''

    data = defaultdict(lambda: [])
    for account, ri_list in data_holder.reservations.items():
        for rsrv in ri_list:
            zone = rsrv.availability_zone
            size = rsrv.instance_type

            data_dict = {'account' : account,
                         'end_date' : rsrv.expiration_date.strftime("%Y-%m-%d"),
                         'count' : rsrv.instance_count,
                         'days_left' : (rsrv.expiration_date - datetime.now()
                                       ).days}
            data[(size, zone)].append(data_dict)
    data_holder.put(ri_expirations=data)
    return data_holder

def layout_data_for_web(data):
    ''' format the data in the way expected by the DataTable '''

    # each table row has these fields:
    # Expiration Details | AZ | Type | Running | Reserved | Delta | Up-Front | Savings
    table_rows = []

    for tup, holder in data.items():
        row = {'zone' : tup[1],
               'type' : tup[0],
               'running' : holder.ri_totals[tup]['running'],
               'reserved' : holder.ri_totals[tup]['reserved'],
               'delta' : holder.ri_delta[tup],
               'upfront' : locale.currency(holder.ri_costs[tup]['up-front'],
                                           grouping=True),
               'savings' : locale.currency(holder.ri_costs[tup]['savings'],
                                           grouping=True),
               'expiration' : holder.ri_expirations[tup]}
        table_rows.append(row)
    return table_rows

def layout_data_for_csv(data):
    ''' format the data for consumption as a CSV  '''

    # each table row has these fields:
    #  AZ | Type | Running | Reserved | Delta | Up-Front
    table_rows = []

    for tup, holder in data.items():
        row = [tup[1], # zone
               tup[0], # type
               holder.ri_totals[tup]['running'], # running
               holder.ri_totals[tup]['reserved'], # reserved
               holder.ri_delta[tup], # delta
               holder.ri_costs[tup]['up-front']] # up-front
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
                holder = DataHolder(instance_type=i.instance_type,
                                    availability_zone=i.availability_zone,
                                    instances={},
                                    reservations={})
                data[tup] = holder

            if account in data[tup].instances.keys():
                data[tup].instances[account].append(i)
            else:
                data[tup].instances[account] = [i]

        for rsrv in res:
            tup = (rsrv.instance_type, rsrv.availability_zone)

            if tup not in data.keys():
                holder = DataHolder(instance_type=rsrv.instance_type,
                                    availability_zone=rsrv.availability_zone,
                                    instances={},
                                    reservations={})
                data[tup] = holder
            if account in data[tup].reservations.keys():
                data[tup].reservations[account].append(rsrv)
            else:
                data[tup].reservations[account] = [rsrv]

    query_cache = {}
    for tup, holder in data.items():
        holder = calculate_reservation_stats(holder)
        holder, query_cache = calculate_costs(request, holder, query_cache)
        holder = get_expirations(holder)
        data[tup] = holder

    return data

