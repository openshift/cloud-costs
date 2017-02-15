''' A view that tabulates AWS reserved instances against the inventory of
    running instances.
'''

import botocore.exceptions
import boto3
import json
import locale
import logging
import re

from collections import defaultdict
from datetime import datetime, timedelta
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config

from budget.util.nvd3js import *
from ..util.fileloader import load_json, load_yaml, save_yaml
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

LOG = logging.getLogger(__name__)

# adjust boto's logging level.
#logging.getLogger('boto').setLevel(logging.ERROR)

# set Decimal precision
getcontext().prec = 3

# set locale
locale.setlocale(locale.LC_ALL, "en_US")

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
    LOG.debug(request.params)

    # override attributes of response
    filename = 'ri-report.csv'
    request.response.content_disposition = 'attachment;filename=' + filename

    header = ['Zone', 'Type', 'Running', 'Reserved', 'Delta', 'Up Front']

    account_data = compile_data(request)
    rows = account_data.csv()
    LOG.debug(rows)
    return {'header': header, 'rows': rows}

@view_config(route_name='reservation', match_param='loc=data', renderer='json')
def reservation_data(request):
    ''' Deliver compiled data to the View as JSON. Called by AJAX query. '''
    LOG.debug(request.params)

    account_data = compile_data(request)
    out = account_data.json()

    # data formatted for jQuery DataTable
    return {'draw' : 1,
            'recordsTotal' : len(out),
            'recordsFiltered' : len(out),
            'data' : out}

@view_config(route_name='reservation',
             match_param='loc=instances',
             renderer='json')
def reservation_instances(request):
    ''' Deliver instance data to the View as JSON. Called by AJAX query. '''
    LOG.debug(request.params)

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
    LOG.debug(request.POST)
    data = request.POST
    account = data['account']
    region = data['region']
    ec2 = get_ec2_client(request, region, account)

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
        LOG.debug(offerings)
        response = {'offerings':offerings}
    except boto3.exceptions.Boto3Error as exc:
        LOG.error("Error communicating with AWS: %s\n\n", exc.message)
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
    LOG.debug(request.POST)

    data = request.POST
    account = data['account']
    region = data['region']
    instance_count = int(data['instance_count'])
    ec2 = get_ec2_client(request, region, account)

    # This is a somewhat redundant second Describe query.
    # My thinking is that it ensures we have a valid ReservedInstanceOfferingId
    # because we pass the id received from the client to a Describe call first,
    # rather than jumping straight to the Purchase call.
    kwargs = {'ReservedInstancesOfferingIds' : [data['reservation_id']]}
    response = ec2.describe_reserved_instances_offerings(**kwargs)
    offerings = response['ReservedInstancesOfferings']
    LOG.debug(offerings)

    if len(offerings) == 1:
        LOG.info('PURCHASING %s RESERVED INSTANCES: %s',
                 instance_count,
                 offerings[0]['ReservedInstancesOfferingId'])
        try:
            kwargs = {'ReservedInstancesOfferingId' : offerings[0]['ReservedInstancesOfferingId'],
                      'InstanceCount' : instance_count,
                      'DryRun' : PURCHASE_DRY_RUN
                     }
            reserved = ec2.purchase_reserved_instances_offering(**kwargs)
            LOG.debug(reserved)
        except botocore.exceptions.ClientError as exc:
            request.response.status = 500
            LOG.error(exc.message)
            return {'results' : 'FAIL', 'errors' : exc.message}
        return {'results' : 'SUCCESS', 'errors' : None}
    else:
        request.response.status = 500
        LOG.error('reservation purchase failed: %s', offerings)
        return {'results' : 'FAIL', 'errors' : offerings}

@view_config(route_name='reservation',
             match_param='loc=expiration-graph',
             renderer='budget:templates/structure.pt')
def reservation_expiration_graph(request):
    ''' output an nvd3 graph to show rate of RI expiration '''
    LOG.debug(request.params)

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
        LOG.info('no graph data')
        return {'data' : 'No graph to show'}

    graph_data = []
    for key in sorted(g_data.keys()):
        graph_data.append({'label': key,
                           'value': int(g_data[key])})

    graph = DiscreteBarChart(staggerLabels='true')
    graph.data = [{'key' : 'reservations', 'values' : graph_data}]

    return {'data' : graph}

#########################################################
# Model objects
#########################################################

class AwsAccount(object):
    ''' aws account-level info '''

    def __init__(self, **kwargs):
        self.account_number = kwargs.get('account_number', '000000000000')
        self.instances = kwargs.get('instances', [])
        self.reservations = kwargs.get('reservations', [])
        self.regions = kwargs.get('regions', [])
        self.availability_zones = kwargs.get('availability_zones', [])

    def instance_types(self):
        ''' return a list of instance types '''
        return set([inst.instance_type for inst in self.instances])

    def search_instances(self, **kwargs):
        ''' search for instances matching all provided criteria.

            kwargs keys must match attributes of the AwsInstance class
        '''
        instances = self.instances
        for key, val in kwargs.items():
            instances = [i for i in instances \
                            if key in i.__dict__ and getattr(i, key) == val]
        return instances

    def reservation_types(self):
        ''' return a list of reserved instance types '''
        return [rsrv.instance_type for rsrv in self.reservations]

    def search_reservations(self, **kwargs):
        ''' search for reservations matching all provided criteria.

            kwargs keys must match attributes of the AwsReservedInstance class
        '''
        reservations = self.reservations
        for key, val in kwargs.items():
            reservations = [i for i in reservations \
                            if key in i.__dict__ and getattr(i, key) == val]
        return reservations

    def unused_reservations(self, instance_type):
        ''' given an instance type, return a count of unused reserved
            instances.
        '''
        instance_count = len(self.search_instances(instance_type=instance_type))
        reservation_count = len(self.search_reservations(instance_type=instance_type))
        return max(0, instance_count-reservation_count)

    def expiring_reservations(self, instance_type, availability_zone):
        ''' given an instance type and availability zone,
            return a list of when this account's reservations will expire
        '''

        out = []
        for rsrv in self.reservations:
            if rsrv.instance_type == instance_type and \
                    rsrv.availability_zone == availability_zone:
                data = {'account' : self.account_number,
                        'end_date' : rsrv.end.strftime("%Y-%m-%d"),
                        'count' : rsrv.instance_count,
                        'days_left' : (rsrv.end - datetime.now()).days
                       }
                out.append(data)
        return out

    def total_upfront(self, instance_type, availability_zone):
        ''' return the total up-front cost for all reservations of this type,
            in this zone.
        '''

        cost = Decimal(0)
        for rsrv in self.reservations:
            if rsrv.instance_type == instance_type and \
                    rsrv.availability_zone == availability_zone:
                cost += rsrv.upfront_cost
        return cost

    def total_reserved_rate(self, instance_type, availability_zone):
        ''' return the total reserved hourly rate for all reservations of this type,
            in this zone.
        '''

        cost = Decimal(0)
        for rsrv in self.reservations:
            if rsrv.instance_type == instance_type and \
                    rsrv.availability_zone == availability_zone:
                cost += rsrv.hourly_rate
        return cost

    def total_ondemand_rate(self, instance_type, availability_zone):
        ''' return the total on-demand hourly cost for all instances of this type,
            in this zone.
        '''

        cost = Decimal(0)
        for inst in self.instances:
            if inst.instance_type == instance_type and \
                    inst.availability_zone == availability_zone:
                cost += inst.hourly_rate
        return cost

class AwsAccountList(object):
    ''' a collection of aws accounts '''

    def __init__(self, **kwargs):
        self.accounts = kwargs.get('accounts', [])

    def add(self, account):
        ''' appends an account to the list '''
        self.accounts.append(account)

    def json(self):
        ''' output json-formatted object '''

        # each table row has these fields:
        # Expiration Details | Account | AZ | Type | Running | Reserved | Delta | Up-Front | Savings


        out = []
        for account in self.accounts:
            for instance_type in account.instance_types():
                for zone in account.availability_zones:
                    running = len(account.search_instances(
                        instance_type=instance_type,
                        availability_zone=zone))

                    if running < 1:
                        continue

                    reserved = sum([r.instance_count for r in \
                        account.search_reservations(instance_type=instance_type,
                                                    availability_zone=zone)])

                    ondemand = account.total_ondemand_rate(instance_type, zone)
                    ondemand = ondemand * 24 * 30 # monthly rate

                    r_hourly = account.total_reserved_rate(instance_type, zone)
                    r_upfront = account.total_upfront(instance_type, zone)
                    r_monthly = (r_upfront/12) + (r_hourly * 24 * 30)

                    data = {'account' : account.account_number,
                            'expiration' : account.expiring_reservations(instance_type,
                                                                         zone),
                            'type' : instance_type,
                            'zone' : zone,
                            'running' : running,
                            'reserved' : reserved,
                            'delta' : running - reserved,
                            'upfront' : locale.currency(r_upfront),
                            'savings' : locale.currency(ondemand - r_monthly)
                           }
                    out.append(data)
        return out

    def csv(self):
        ''' output csv-formatted object '''

        # each table row has these fields:
        #  Account | AZ | Type | Running | Reserved | Delta | Up-Front
        out = []
        for account in self.accounts:
            for instance_type in account.instance_types():
                for zone in account.availability_zones:
                    running = len(account.search_instances(
                        instance_type=instance_type,
                        availability_zone=zone))

                    if running < 1:
                        continue

                    reserved = sum([r.instance_count for r in \
                        account.search_reservations(instance_type=instance_type,
                                                    availability_zone=zone)])

                    data = [account.account_number,
                            zone,
                            instance_type,
                            running,
                            reserved,
                            (running - reserved),
                            locale.currency(account.total_upfront(instance_type,
                                                                  zone)),
                           ]
                    out.append(data)
        return out

class AwsInstance(object):
    ''' aws instance model object '''

    def __init__(self, **kwargs):
        self.account = kwargs.get('account', None)
        self.instance_id = kwargs.get('id', 0)
        self.name = kwargs.get('name', None)
        self.environment = kwargs.get('environment', None)
        self.instance_type = kwargs.get('instance_type', None)
        self.region = kwargs.get('region', None)
        self.availability_zone = kwargs.get('availability_zone', None)
        self.hourly_rate = kwargs.get('hourly_rate', 0)

class AwsReservedInstance(object):
    ''' aws reserved instance model object '''

    def __init__(self, **kwargs):
        self.account = kwargs.get('account', None)
        self.reservation_id = kwargs.get('id', 0)
        self.instance_type = kwargs.get('instance_type', None)
        self.instance_count = kwargs.get('instance_count', None)
        self.region = kwargs.get('region', None)
        self.availability_zone = kwargs.get('availability_zone', None)
        self.scope = kwargs.get('scope', None)
        self.upfront_cost = kwargs.get('upfront_cost', 0)
        self.hourly_rate = kwargs.get('hourly_rate', 0)
        self.start = kwargs.get('start', datetime(1970, 1, 1, 0, 0, 0))
        self.end = kwargs.get('end', datetime(1970, 1, 1, 0, 0, 0))

#########################################################
# Helper methods
#########################################################

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

def availability_zones(request, account):
    ''' return a list of EC2 AZs for a given account,
        cache the data locally for performance reasons
    '''

    zone_file = request.registry.settings['cache.dir'] + "/ec2_zones.yaml"
    try:
        zones = load_yaml(zone_file)
    except IOError:
        zones = {}

    last_check = zones.get('last_check', datetime(1970, 1, 1, 0, 0, 0))

    regions = boto3.session.Session().get_available_regions('ec2')
    for region in regions:
        if region not in zones or datetime.now()-last_check > timedelta(days=30):
            ec2 = get_ec2_client(request, region, account)
            az_list = ec2.describe_availability_zones().get('AvailabilityZones', None)
            zones[region] = [zone['ZoneName'] for zone in az_list]
            zones['last_check'] = datetime.now()

    save_yaml(zone_file, zones)
    zones.pop('last_check')
    return [z for _, z_list in zones.items() for z in z_list]

def compile_data(request):
    ''' compile instance and RI information into a collection of DataHolder
        objects that can be manipulated into the desired presentation layout
    '''
    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    accounts = sorted(load_yaml(creds_file).keys())

    regions = boto3.session.Session().get_available_regions('ec2')

    acct_list = AwsAccountList()

    query_cache = {'i': {}, 'r': {}}

    for account in accounts:
        num = get_account_number(account, request.registry.settings)
        zones = availability_zones(request, account)
        aws_account = AwsAccount(account_number=num,
                                 regions=regions,
                                 availability_zones=zones)

        for i in get_instances(num):
            if i.instance_type in query_cache['i'].keys():
                price = query_cache['i'][i.instance_type]
            else:
                price = get_price(request,
                                  instance_type=i.instance_type,
                                  region=i.region,
                                  pricing='OnDemand')
                query_cache['i'][i.instance_type] = price

            instance = AwsInstance(instance_id=i.instance_id,
                                   name=i.name,
                                   environment=i.environment,
                                   account=i.account,
                                   instance_type=i.instance_type,
                                   region=i.region,
                                   availability_zone=i.availability_zone,
                                   hourly_rate=price.get('Hrs', 0),
                                  )
            aws_account.instances.append(instance)

        for r in get_reservations(num):
            if r.instance_type in query_cache['r'].keys():
                price = query_cache['r'][r.instance_type]
            else:
                price = get_price(request,
                                  instance_type=r.instance_type,
                                  region=r.region,
                                  pricing='Reserved',
                                  lease_contract_length='1yr',
                                  purchase_option='Partial Upfront',
                                  scope=r.scope)
                query_cache['r'][r.instance_type] = price

            reserved = AwsReservedInstance(account=r.account,
                                           reservation_id=r.reservation_id,
                                           instance_type=r.instance_type,
                                           instance_count=r.instance_count,
                                           region=r.region,
                                           availability_zone=r.availability_zone,
                                           scope=r.scope,
                                           upfront_cost=price.get('Quantity', 0),
                                           hourly_rate=price.get('Hrs', 0),
                                           start=r.start,
                                           end=r.end,
                                          )
            aws_account.reservations.append(reserved)
        acct_list.add(aws_account)
    return acct_list

def get_account_number(name, settings):
    ''' helper function to return an account number when given an account
        name
    '''
    creds_file = settings['creds.dir'] + "/creds.yaml"
    return load_yaml(creds_file)[name]['account']

def get_creds(account, settings):
    ''' helper function to return account creds when given an account name
    '''
    creds_file = settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)
    access_key = awscreds[account]['access_key']
    secret_key = awscreds[account]['secret_key']
    return (access_key, secret_key)

def get_ec2_client(request, region, account_name):
    ''' params:
            request      - pyramid request object
            region       - string, ec2 region
            account_name - string, defined in creds.yaml

        returns: boto3 ec2 client
    '''
    access_key, secret_key = get_creds(account_name, request.registry.settings)

    return boto3.client('ec2',
                        region,
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key)

def get_instances(account):
    ''' fetch a list of running instances from the DB '''
    results = DBSession.query(AwsInstanceInventory).filter(\
                    AwsInstanceInventory.status == 'running',
                    AwsInstanceInventory.account == account).all()
    return results

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

def get_reservations(account):
    ''' fetch a list of active reservations from the DB '''
    results = DBSession.query(AwsReservationInventory).filter(\
                AwsReservationInventory.account == account,
                AwsReservationInventory.end >= datetime.now(),
                AwsReservationInventory.start <= datetime.now()).all()
    return results

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
