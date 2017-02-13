#!/usr/bin/env python
''' update the inventory of aws instances and reservations '''

import logging
import ssl
import sys
import transaction
import traceback

import botocore.exceptions
import boto3

from datetime import datetime, timedelta
from dateutil import parser as date_parser
from multiprocessing import Pool, cpu_count

from sqlalchemy import engine_from_config
from sqlalchemy.sql import functions
from sqlalchemy.exc import IntegrityError

from pyramid.paster import (get_appsettings,
                            setup_logging)

from pyramid.scripts.common import parse_vars

from ..models import (DBSession,
                      AwsInstanceInventory,
                      AwsReservationInventory)

from ..util.fileloader import load_yaml
from ..util.queries.util import insert_or_update

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
CHECK_DATE = datetime.now()
CHECK_DATE_STR = CHECK_DATE.strftime(DATE_FORMAT)

def usage():
    ''' how to call this program '''
    print "Usage: %s <config_uri>" % sys.argv[0]
    sys.exit()

def update_instance_inventory(region, access_key, secret_key, account):
    ''' update inventory of instances '''
    instances = []
    try:
        ec2conn = get_ec2_client(region, access_key, secret_key)
        response = ec2conn.describe_instances()
    except boto3.exceptions.Boto3Error as exc:
        log.error("Error communicating with AWS: %s\n\n", exc.message)
        return []
    except ssl.SSLError  as exc:
        log.error("SSL Error when communicating with AWS: %s\n\n", exc.message)
        return []

    if len(response['Reservations']) == 0:
        return []

    instances = []
    for res in response['Reservations']:
        instances.extend(res['Instances'])

    objects = []
    try:
        for inst in instances:
            name = 'No Name'
            env = 'No Environment'
            for dic in inst.get('Tags', {}):
                if dic['Key'] == 'Name':
                    name = dic['Value']
                if dic['Key'] == 'environment':
                    env = dic['Value']

            obj = (AwsInstanceInventory,
                   {'instance_id': inst['InstanceId']},
                   {'check_date' : CHECK_DATE_STR,
                    'name' : name,
                    'environment' : env,
                    'instance_type' : inst['InstanceType'],
                    'availability_zone' : inst['Placement']['AvailabilityZone'],
                    'account' : get_account_number(account),
                    'status' : inst['State']['Name'],
                    'launch_date' : inst['LaunchTime'].replace(tzinfo=None),
                   })
            objects.append(obj)
    except Exception:
        traceback.print_exc()
        raise
    return objects

def update_reservation_inventory(region, access_key, secret_key, account):
    ''' return an inventory of reserved instances for the given region in the
        given account
    '''
    try:
        ec2conn = get_ec2_client(region, access_key, secret_key)
        response = ec2conn.describe_reserved_instances()
    except boto3.exceptions.Boto3Error as exc:
        log.error("Error communicating with AWS: %s\n\n", exc.message)
        return []
    except ssl.SSLError  as exc:
        log.error("SSL Error when communicating with AWS: %s\n\n", exc.message)
        return []

    if len(response['ReservedInstances']) == 0:
        return []

    objects = []
    try:
        for rsrv in response['ReservedInstances']:
            obj = (AwsReservationInventory,
                   {'reservation_id': rsrv['ReservedInstancesId']},
                   {'instance_type' : rsrv['InstanceType'],
                    'availability_zone' : rsrv.get('AvailabilityZone', None),
                    'account' : get_account_number(account),
                    'purchase_date' : rsrv['Start'].replace(tzinfo=None),
                    'expiration_date' : rsrv['End'].replace(tzinfo=None),
                    'scope' : rsrv['Scope'],
                    'instance_count' : rsrv['InstanceCount'],
                   })
            objects.append(obj)
    except Exception:
        traceback.print_exc()
        raise
    return objects

def expire_instances():
    ''' mark any instances that weren't updated as terminated. if we didn't see
        them on this pass, it means they are gone.
    '''
    DBSession.query(AwsInstanceInventory
                   ).filter(AwsInstanceInventory.check_date != CHECK_DATE_STR
                           ).update({'status' : 'terminated',
                                     'check_date' : CHECK_DATE_STR})
    transaction.commit()

def prune_instances(threshold=365):
    ''' delete any instances that have been terminated over our threshold
        number of days.
    '''
    threshold_date = CHECK_DATE - timedelta(days=threshold)
    DBSession.query(AwsInstanceInventory
                   ).filter(AwsInstanceInventory.check_date <= threshold_date,
                            AwsInstanceInventory.status == 'terminated'
                           ).delete()
    transaction.commit()

def prune_reservations(threshold=365):
    ''' delete any reservations that have expired over our threshold
        number of days.
    '''
    threshold_date = CHECK_DATE - timedelta(days=threshold)
    DBSession.query(AwsReservationInventory
                   ).filter(AwsReservationInventory.expiration_date <= threshold_date,
                           ).delete()
    transaction.commit()

def get_creds(account):
    ''' read AWS creds from file '''
    awscreds = load_yaml(creds_file)
    access_key = awscreds[account]['access_key']
    secret_key = awscreds[account]['secret_key']
    return (access_key, secret_key)

def get_accounts():
    ''' read AWS account names from file '''
    return sorted(load_yaml(creds_file).keys())

def get_account_number(name):
    ''' read AWS account numbers from file '''
    return load_yaml(creds_file)[name]['account']

def get_ec2_client(region, access_key, secret_key):
    ''' return an ec2 client object '''
    cli = boto3.client('ec2',
                       region_name=region,
                       aws_access_key_id=access_key,
                       aws_secret_access_key=secret_key)
    return cli

def main():
    ''' main method '''
    if len(sys.argv) < 2:
        usage()
    config_uri = sys.argv[1]
    options = parse_vars(sys.argv[2:])

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    global settings
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    global creds_file
    creds_file = settings['creds.dir'] + "/creds.yaml"


    # global to enable us to handle KeyboardInterrupts without leaving zombies
    # around.
    global pool
    pool = Pool(processes=cpu_count()*2)

    objects = []
    pids = []

    for account in get_accounts():
        access_key, secret_key = get_creds(account)

        regions = boto3.session.Session().get_available_regions('ec2')
        for region in regions:
            # skip restricted access regions
            if region in ['us-gov-west-2', 'cn-north-1']:
                continue

            log.debug('checking %s: %s', account, region)
            run1 = pool.apply_async(update_instance_inventory,
                                    (region, access_key, secret_key, account),
                                    callback=objects.extend)
            run2 = pool.apply_async(update_reservation_inventory,
                                    (region, access_key, secret_key, account),
                                    callback=objects.extend)

            pids.append(run1)
            pids.append(run2)

        # get the output of all our processes
        for pid in pids:
            pid.get()
        del pids[:]

    # ensure the sqlalchemy objects aren't garbage-collected before we commit
    # them.
    # see: http://docs.sqlalchemy.org/en/latest/orm/session_state_management.html#session-referencing-behavior
    merged = []
    for col, kwargs, defaults in objects:
        obj = insert_or_update(DBSession, col, defaults=defaults, **kwargs)
        merged.append(DBSession.merge(obj))
    try:
        transaction.commit()
    except IntegrityError as exc:
        DBSession.rollback()
        log.error(exc)

    pool.close()
    pool.join()
    expire_instances()
    #TODO: enable passing in threshold value
    prune_instances()
    prune_reservations()

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
        pool.terminate()
        pool.join()
