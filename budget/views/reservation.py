''' A view that tabulates AWS reserved instances against the inventory of
    running instances.
'''

import collections
import json
import locale
import logging
import re

from datetime import datetime, timedelta
from decimal import Decimal, getcontext

import botocore.exceptions
import boto3

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

    header = ['Account', 'Zone', 'Type', 'Running', 'Reserved', 'Delta', 'Up Front']

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
    LOG.debug(out)
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
        self.name = kwargs.get('name', None)
        self.account_number = kwargs.get('account_number', '000000000000')
        self.reservations = kwargs.get('reservations', [])
        self.regions = kwargs.get('regions', [])

    def __repr__(self):
        return "AwsAccount %s: %s" % (self.name, self.account_number)

    def get_regional_reservations(self):
        ''' return a dict of region-scoped RIs '''
        out = {}
        for region in self.regions:
            for instance_type in region.reserved_instance_types():
                reserved = sum([r.instance_count for r in \
                    region.search_reservations(instance_type=instance_type,
                                               region=region)])
                if reserved > 0:
                    out[(instance_type, region)] = {'reserved' : reserved}
        return out

    def reservation_delta(self):
        ''' returns a dict identifying difference between reservations and
            running instances
        '''
        out = {}
        for region in self.regions:
            out.update(region.reservation_delta())
        return out

    def region(self, name):
        ''' getter method for regions '''
        for region in self.regions:
            if region.name == name:
                return region

    def reservation_types(self):
        ''' return a list of reserved instance types '''
        return [rsrv.instance_type for rsrv in self.reservations]

class AwsAccountList(collections.MutableSet):
    ''' a collection of aws accounts '''

    def __init__(self, **kwargs):
        self.accounts = kwargs.get('accounts', [])

    def __iter__(self):
        return iter(self.accounts)

    def __contains__(self, thing):
        return thing in self.accounts

    def __len__(self):
        return len(self.accounts)

    def add(self, account):
        self.accounts.append(account)

    def discard(self, account):
        self.accounts.remove(account)

    def get_reservation_deltas(self):
        ''' get counts of RIs and running instances, along with a rough
            approximation of allocation of RIs to instances. Factor in
            region-scoped RIs and allocation of RIs across accounts.
        '''

        out = {}
        for account in self.accounts:
            out[account] = account.reservation_delta()

        # pylint: disable=invalid-name
        def _reallocate(a, b):
            ''' reallocate RIs from a to b '''
            if a['scope'] == 'AvailabilityZone':
                if abs(a['delta']) >= abs(b['delta']):
                    a['delta'] += b['delta']
                    b['delta'] = 0
                elif abs(a['delta']) < abs(b['delta']):
                    a['delta'] = 0
                    b['delta'] += a['delta']
            elif a['scope'] == 'Region':
                if abs(a['delta']) >= abs(b['delta']):
                    a['delta'] -= b['delta']
                    b['delta'] = 0
                elif abs(a['delta']) < abs(b['delta']):
                    a['delta'] = 0
                    b['delta'] -= a['delta']
            return a, b

        def _scan(dic, term1, term2, source, seen=set()):
            ''' scan the dict for other accounts with instances of the same
                size in the given AZ/region.

                allocate unused RIs to matching instances.

                recurse until we can't allocate any more unused RIs
            '''
            for a, b in dic.iteritems():
                if a == source or a in seen:
                    continue

                for x, y in b.iteritems():
                    if dic[source][(term1, term2)]['scope'] == 'AvailabilityZone':
                        x_one = x[1]
                    elif dic[source][(term1, term2)]['scope'] == 'Region':
                        x_one = x[1].name[:-1]

                    if x[0] == term1 and \
                            x_one == term2.name and \
                            y['delta'] > 0:
                        d1, d2 = _reallocate(dic[source][(term1, term2)], y)
                        dic[source][(term1, term2)] = d1
                        dic[a][x] = d2

            if source not in seen:
                seen.add(source)

            if len(dic.keys()) > seen and \
                    (dic[source][(term1, term2)].get('delta', 0) < 0 or \
                    dic[source][(term1, term2)].get('reserved', 0) > 0):
                dic = _scan(dic, term1, term2, source, seen)

            return dic

        for account, val in out.iteritems():
            for tup, delta in val.iteritems():
                instance_type = tup[0]

                if delta['scope'] == 'AvailabilityZone' and delta['delta'] < 0:
                    zone = tup[1]
                    out = _scan(out, instance_type, zone, account)
                elif delta['scope'] == 'Region' and delta['reserved'] > 0:
                    region = tup[1]
                    out = _scan(out, instance_type, region, account)
        return out

    def json(self):
        ''' output json-formatted object for display in DataTable

            each table row has these fields:
            Expiration Details | Account | AZ | Type | Running | Reserved | Delta | Up-Front | Savings
        '''

        out = []
        deltas = self.get_reservation_deltas()
        for account, delta in deltas.iteritems():
            for tup, val in delta.iteritems():
                instance_type = tup[0]
                zone = tup[1]

                r_upfront, r_hourly = zone.reserved_cost(instance_type)
                r_monthly = ((r_upfront/12) + (r_hourly * 24 * 30))

                expiration = zone.expiring_reservations(instance_type)
                if len(expiration) > 0:
                    for idx, dic in enumerate(expiration):
                        dic['account'] = account.name
                        expiration[idx] = dic

                data = {'account' : account.name,
                        'expiration' : expiration,
                        'type' : instance_type,
                        'zone' : zone.name,
                        'reserved' : val['reserved'],
                        'delta' : val['delta'],
                        'upfront' : locale.currency(r_upfront*val['delta']),
                       }

                if isinstance(tup[1], AwsRegion):
                    data.update({'running' : 'N/A',
                                 'savings' : 'N/A'
                                })
                elif isinstance(tup[1], AwsAvailabilityZone):
                    ondemand = zone.ondemand_cost(instance_type)
                    od_monthly = ondemand * 24 * 30

                    data.update({'running' : val['running'],
                                 'savings' : locale.currency( \
                                    abs((od_monthly-r_monthly))*val['delta'])
                                })
                out.append(data)
        return out

    def csv(self):
        ''' output csv-formatted object

            each table row has these fields:
            Account | AZ | Type | Running | Reserved | Delta | Up-Front
        '''

        out = []
        deltas = self.get_reservation_deltas()
        for account, delta in deltas.iteritems():
            for tup, val in delta.iteritems():
                instance_type = tup[0]
                zone = tup[1]

                r_upfront, _ = zone.reserved_cost(instance_type)

                data = [account.account_number,
                        zone.name,
                        instance_type,
                        val.get('running', 'N/A'),
                        val.get('reserved', 0),
                        val.get('delta', 0),
                        locale.currency(r_upfront*val.get('delta', 0))
                       ]
                out.append(data)
        return out

class AwsInstance(object):
    ''' aws instance model object '''

    def __init__(self, **kwargs):
        self.instance_id = kwargs.get('id', 0)
        self.name = kwargs.get('name', None)
        self.environment = kwargs.get('environment', None)
        self.instance_type = kwargs.get('instance_type', None)
        self.region = kwargs.get('region', None)
        self.availability_zone = kwargs.get('availability_zone', None)
        self.hourly_rate = kwargs.get('hourly_rate', 0)
        self.ri_price = kwargs.get('ri_price', 0)

    def __repr__(self):
        return "AwsInstance %s" % (self.instance_id)

class AwsReservedInstance(object):
    ''' aws reserved instance model object '''

    def __init__(self, **kwargs):
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

    def __repr__(self):
        return "AwsReservedInstance %s" % (self.reservation_id)

class AwsRegion(object):
    ''' aws region model object '''

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.availability_zones = kwargs.get('availability_zones', [])
        self.reserved_instances = kwargs.get('reserved_instances', [])

    def __repr__(self):
        return "AwsRegion %s" % (self.name)

    def availability_zone(self, name):
        ''' getter method for AZs '''
        for zone in self.availability_zones:
            if zone.name == name:
                return zone

    def expiring_reservations(self, instance_type):
        ''' given an instance type and availability zone,
            return a list of when this account's reservations will expire
        '''

        out = []
        for rsrv in self.reserved_instances:
            if rsrv.instance_type == instance_type:
                data = {'end_date' : rsrv.end.strftime("%Y-%m-%d"),
                        'count' : rsrv.instance_count,
                        'days_left' : (rsrv.end - datetime.now()).days
                       }
                out.append(data)
        return out

    def reservation_delta(self):
        ''' return difference between running instances and reserved instances
        '''
        out = {}
        for zone in self.availability_zones:
            out.update(zone.reservation_delta())

        # Allocate regional reserved instances
        # XXX: currently, this will cause the output to show things like "5
        # instances running, zero reservations, but zero delta",
        # which isn't wholly intuitive.
        for instance_type in self.reserved_instance_types():
            reserved = sum([r.instance_count for r in \
                    self.search_reservations(instance_type=instance_type)])
            delta = reserved

            for tup, val in out.iteritems():
                if tup[0] == instance_type and val['delta'] > 0:
                    if val['delta'] >= reserved:
                        out[tup]['delta'] -= reserved
                        delta = 0
                    elif val['delta'] < reserved:
                        out[tup]['delta'] = 0
                        delta -= val['delta']

            if reserved > 0:
                out[(instance_type, self)] = {'reserved' : reserved,
                                              'scope' : 'Region',
                                              'delta' : delta }
        return out

    def reserved_cost(self, instance_type):
        ''' return the up-front cost for a reservation of this type,
            in this region.
        '''

        for rsrv in self.reserved_instances:
            if rsrv.instance_type == instance_type:
                return (rsrv.upfront_cost, rsrv.hourly_rate)
        return (0, 0)

    def reserved_instance_types(self):
        ''' return list of region-scoped reserved instance types used in this region '''
        return set([rsrv.instance_type for rsrv in self.reserved_instances])

    def search_reservations(self, **kwargs):
        ''' search for reservations matching all provided criteria.

            kwargs keys must match attributes of the AwsReservedInstance class
        '''
        reservations = self.reserved_instances
        for key, val in kwargs.items():
            reservations = [i for i in reservations \
                            if key in i.__dict__ and getattr(i, key) == val]
        return reservations

class AwsAvailabilityZone(object):
    ''' aws availability zone model object '''

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.instances = kwargs.get('instances', [])
        self.reserved_instances = kwargs.get('reserved_instances', [])

    def __repr__(self):
        return "AwsAvailabilityZone %s" % (self.name)

    def expiring_reservations(self, instance_type):
        ''' given an instance type and availability zone,
            return a list of when this account's reservations will expire
        '''

        out = []
        for rsrv in self.reserved_instances:
            if rsrv.instance_type == instance_type:
                data = {'end_date' : rsrv.end.strftime("%Y-%m-%d"),
                        'count' : rsrv.instance_count,
                        'days_left' : (rsrv.end - datetime.now()).days
                       }
                out.append(data)
        return out

    def instance_types(self):
        ''' return list of instance types used in this AZ '''
        return set([inst.instance_type for inst in self.instances])

    def reserved_instance_types(self):
        ''' return list of reserved instance types used in this AZ '''
        return set([rsrv.instance_type for rsrv in self.reserved_instances])

    def search_instances(self, **kwargs):
        ''' search for instances matching all provided criteria.

            kwargs keys must match attributes of the AwsInstance class
        '''
        instances = self.instances
        for key, val in kwargs.items():
            instances = [i for i in instances \
                            if key in i.__dict__ and getattr(i, key) == val]
        return instances

    def search_reservations(self, **kwargs):
        ''' search for reservations matching all provided criteria.

            kwargs keys must match attributes of the AwsReservedInstance class
        '''
        reservations = self.reserved_instances
        for key, val in kwargs.items():
            reservations = [i for i in reservations \
                            if key in i.__dict__ and getattr(i, key) == val]
        return reservations

    def ondemand_cost(self, instance_type):
        ''' return the on-demand hourly rate for instances of this type,
            in this zone.
        '''

        for inst in self.instances:
            if inst.instance_type == instance_type:
                return inst.hourly_rate
        return 0

    def reserved_cost(self, instance_type):
        ''' return the up-front cost for a reservation of this type,
            in this zone.
        '''

        for rsrv in self.reserved_instances:
            if rsrv.instance_type == instance_type:
                return (rsrv.upfront_cost, rsrv.hourly_rate)

        for i in self.instances:
            if i.instance_type == instance_type:
                return (i.ri_price.get('Quantity', 0), i.ri_price.get('Hrs', 0))

        return (0, 0)

    def reservation_delta(self):
        ''' return difference between running instances and reserved instances
        '''

        out = {}
        for instance_type in self.instance_types():
            running = len(self.search_instances(instance_type=instance_type))

            reserved = sum([r.instance_count for r in \
                self.search_reservations(instance_type=instance_type)])

            if running < 1 and reserved < 1:
                continue

            out[(instance_type, self)] = {'running' : running,
                                          'reserved' : reserved,
                                          'delta' : running - reserved,
                                          'scope' : 'AvailabilityZone'}
        return out

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
    THRESHOLD=3

    zone_file = request.registry.settings['cache.dir'] + "/ec2_zones.yaml"
    try:
        zones = load_yaml(zone_file)
    except IOError:
        zones = {}

    last_check = zones.get('last_check', datetime(1970, 1, 1, 0, 0, 0))

    if len(zones.keys()) > 0 and \
           datetime.now()-last_check < timedelta(days=THRESHOLD):
        regions = zones.keys()
    else:
        regions = boto3.session.Session().get_available_regions('ec2')

    for region in regions:
        if region not in zones or \
                datetime.now()-last_check > timedelta(days=THRESHOLD):
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

    boto_regions = boto3.session.Session().get_available_regions('ec2')

    acct_list = AwsAccountList()

    query_cache = {'a':{}, 'b':{}, 'i':{}, 'j':{}}

    for account in accounts:
        num = get_account_number(account, request.registry.settings)
        aws_account = AwsAccount(name=account,
                                 account_number=num)

        for boto_region in boto_regions:
            region = AwsRegion(name=boto_region)

            boto_zones = availability_zones(request, account)

            az_dict = {zone : AwsAvailabilityZone(name=zone) for zone in
                       boto_zones if boto_region == zone[:-1]}

            if num in query_cache['a'].keys():
                instances = query_cache['a'][num]
            else:
                instances = get_instances(num)
                query_cache['a'][num] = instances

            for i in instances:
                tup = (i.instance_type, i.availability_zone)

                if i.region != boto_region:
                    continue

                if tup in query_cache['i'].keys():
                    od_price = query_cache['i'][tup]
                else:
                    od_price = get_price(request,
                                         instance_type=i.instance_type,
                                         region=i.region,
                                         pricing='OnDemand')
                    query_cache['i'][tup] = od_price

                if tup in query_cache['j'].keys():
                    r_price = query_cache['j'][tup]
                else:
                    r_price = get_price(request,
                                        instance_type=i.instance_type,
                                        region=i.region,
                                        pricing='Reserved',
                                        lease_contract_length='1yr',
                                        purchase_option='Partial Upfront',
                                        scope='AvailabilityZone')
                    query_cache['j'][tup] = r_price

                instance = AwsInstance(instance_id=i.instance_id,
                                       name=i.name,
                                       environment=i.environment,
                                       instance_type=i.instance_type,
                                       region=region,
                                       availability_zone=az_dict[i.availability_zone],
                                       hourly_rate=od_price.get('Hrs', 0),
                                       ri_price=r_price
                                      )
                az_dict[i.availability_zone].instances.append(instance)

            if num in query_cache['b'].keys():
                reservations = query_cache['b'][num]
            else:
                reservations = get_reservations(num)
                query_cache['b'][num] = reservations

            for r in reservations:
                tup = (r.instance_type, r.availability_zone)

                if r.region != boto_region:
                    continue

                if tup in query_cache['j'].keys():
                    price = query_cache['j'][tup]
                else:
                    price = get_price(request,
                                      instance_type=r.instance_type,
                                      region=r.region,
                                      pricing='Reserved',
                                      lease_contract_length='1yr',
                                      purchase_option='Partial Upfront',
                                      scope=r.scope)
                    query_cache['j'][tup] = price

                reserved = AwsReservedInstance(reservation_id=r.reservation_id,
                                               instance_type=r.instance_type,
                                               instance_count=r.instance_count,
                                               region=region,
                                               availability_zone=az_dict.get(r.availability_zone),
                                               scope=r.scope,
                                               upfront_cost=price.get('Quantity', 0),
                                               hourly_rate=price.get('Hrs', 0),
                                               start=r.start,
                                               end=r.end,
                                              )
                if r.scope == 'Region':
                    region.reserved_instances.append(reserved)
                else:
                    az_dict[r.availability_zone].reserved_instances.append(reserved)
            region.availability_zones = az_dict.values()
            aws_account.regions.append(region)
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
