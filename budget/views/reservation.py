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
import logging
import os
import sys
import yaml

from collections import defaultdict

from pyramid.response import Response
from pyramid.view import view_config

ONE_YEAR = 31536000 # 1 year, in seconds
THREE_YEAR = ONE_YEAR * 3

log = logging.getLogger(__name__)

# adjust boto's logging level.
#logging.getLogger('boto').setLevel(logging.ERROR)

@view_config(route_name='reservation', renderer='budget:templates/reservation.pt')
def reservation(request):
    creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
    awscreds = load_yaml(creds_file)
    return { 'results' : sorted(awscreds.keys()) }

@view_config(route_name='reservation_csv', renderer='budget:templates/reservation_csv.pt')
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

@view_config(route_name='reservation_data', renderer='budget:templates/reservation_data.pt')
def reservation_data(request):
		creds_file = request.registry.settings['creds.dir'] + "/creds.yaml"
		awscreds = load_yaml(creds_file)
		data = request.POST
		account = data['id']

                header = [ 'Zone', 'Type', 'Running', 'Reserved',
                        'Delta', 'Hourly', 'Up Front', 'Subtotal', 'Purchase' ]

                log.debug('fetching reservations for %s' % account)
                results = get_current_reservations(
                                awscreds[account]['access_key'],
                                awscreds[account]['secret_key'] )

                return { 'account' : account,
                         'header'  : header,
                         'results' : results }

@view_config(route_name='reservation_purchase', renderer='budget:templates/reservation_purchase.pt')
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
        log.debug(offerings.describe())
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


def load_yaml(filename):
    try:
        yamlfile = yaml.load(open(filename, 'r+'))
    except IOError:
        raise
    return yamlfile

def get_current_reservations(access_key, secret_access_key):
    regions = boto.ec2.regions()
    results = {}

    for region in regions:
        # skip restricted access regions
        if region.name in [ 'us-gov-west-1', 'cn-north-1' ]:
            continue

        ec2conn = boto.ec2.connect_to_region(region.name,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_access_key)

        diff, totals = get_reservation_stats(ec2conn, region)
        if not diff:
            continue

        offerings = {}
        for params in diff.keys():
            if diff[params] < 0:
                offer = get_reserved_offerings(
                    ec2conn,
                    instance_type=params[0],
                    target_az=params[1] )
                offerings[params] = offer

        results[region] = get_display_results(diff, offerings, totals, region)
    return results

def get_reservation_stats(ec2conn, region):
    running_instances  = {}
    reserved_instances = {}
    totals             = {}

    try:
        instances = ec2conn.get_only_instances()
        reservations = ec2conn.get_all_reserved_instances()
    except boto.exception.EC2ResponseError as e:
        sys.stderr.write("Error communicating with %s: %s\n\n" % (
                region.name, e.message))
        return (None, None)

    for inst in instances:
        az   = inst.placement
        size = inst.instance_type

        if (size,az) not in totals.keys():
            totals[(size,az)] = defaultdict(lambda: 0)

        if inst.state == 'running':
            # do a count of each type/az combination
            running_instances[(size,az)] = running_instances.get((size,az),0)+1
            totals[(size,az)]['running'] = totals[(size,az)].get('running',0)+1

    for ri in reservations:
        az   = ri.availability_zone
        size = ri.instance_type

        if (size,az) not in totals.keys():
            totals[(size,az)] = defaultdict(lambda: 0)

        if ri.state == 'active':
            # do a count of each type/az combination
            reserved_instances[(size,az)] = reserved_instances.get((size,az),0)+ri.instance_count
            totals[(size,az)]['reserved'] = totals[(size,az)].get('reserved',0)+ri.instance_count

    # for each type/az combination, the diff will be
    # - postiive if we have unused reservations
    # - negative if there are on-demand instances
    diff = dict([(x,reserved_instances[x]-running_instances.get(x,0)) for x in reserved_instances])

    # diff only has keys present in reserved_instances.
    # now we add the keys from running_instances
    for placement in running_instances:
        if not placement in reserved_instances:
            diff[placement] = -running_instances[placement]

    return diff, totals

def get_reserved_offerings(ec2conn, target_az='us-east-1a',
        instance_type='m3.large', duration=ONE_YEAR):

    offerings = ec2conn.get_all_reserved_instances_offerings(
            instance_type = instance_type,
            availability_zone = target_az,
            max_duration = duration,
            product_description = 'Linux/UNIX (Amazon VPC)' )

    cheapest = None
    for offering in offerings:
        # skip marketplace offerings, we only want Amazon-sold RIs
        if offering.marketplace:
            continue

        #XXX: I'm not sure why there are reservation offerings with no fixed price.
        #XXX: This needs investigation.
        if offering.fixed_price == u'0.0':
            continue

        ongoing = get_hourly_charges(offering)

        if cheapest:
            c_annual = float(cheapest.fixed_price) + (ongoing * 24 * 365)
            o_annual = float(offering.fixed_price) + (ongoing * 24 * 365)
            if o_annual < c_annual:
                cheapest = offering
        else:
            cheapest = offering

    return cheapest

def get_hourly_charges(offering):
    charges = 0

    if len(offering.recurring_charges) == 1:
        if offering.recurring_charges[0].frequency == 'Hourly':
            charges = offering.recurring_charges[0].amount
        else:
            raise Exception('Unexpected recurring_charges frequency')
    else:
        charges = offering.usage_price

    return float(charges)


def get_display_results(diff, offerings, totals, region):
    total  = 0
    output = []
    keys   = diff.keys()

    for key in keys:
        size, az = key
        running  = totals[key]['running']
        reserved = totals[key]['reserved']
        delta    = diff[key]

        if key in offerings.keys() and offerings[key]:
            hourly   = get_hourly_charges(offerings[key])
            upfront  = offerings[key].fixed_price
            subtotal = abs(float(delta) * float(upfront)) #XXX: might be wrong
            total += subtotal
        else:
            hourly   = 0
            upfront  = 0
            subtotal = 0

        line = [az, size, running, reserved, delta, hourly, upfront, subtotal]

        output.append(line)
    return sorted(output)
