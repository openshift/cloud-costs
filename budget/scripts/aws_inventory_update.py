#!/usr/bin/env python
''' update the inventory of aws instances and reservations '''

import boto.ec2
import logging
import sys
import transaction

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
CHECK_DATE = datetime.now().strftime(DATE_FORMAT)

def usage():
    ''' how to call this program '''
    print "Usage: %s <config_uri>" % sys.argv[0]
    sys.exit()

def update_instance_inventory(ec2conn, account):
    ''' update inventory of instances '''
    instances = []
    try:
        instances = ec2conn.get_only_instances()
    except boto.exception.EC2ResponseError as exc:
        log.error("Error communicating with AWS: %s\n\n", exc.message)
        return
    except SSLError  as exc:
        log.error("Error communicating with AWS: %s\n\n", exc.message)
        return

    objects = []
    for inst in instances:
        if 'Name' in inst.tags:
            name = inst.tags['Name']
        else:
            name = 'No Name'

        if 'environment' in inst.tags:
            env = inst.tags['environment']
        else:
            env = 'No Environment'

        obj = (AwsInstanceInventory,
               {'instance_id':inst.id},
               {'check_date' : CHECK_DATE,
                'name' : name,
                'environment' : env,
                'instance_type' : inst.instance_type,
                'availability_zone' : inst.placement,
                'account' : get_account_number(account),
                'status' : inst.state,
                'launch_date' : date_parser.parse(inst.launch_time
                                                 ).strftime(DATE_FORMAT)})
        objects.append(obj)
    return objects

def update_reservation_inventory(ec2conn, account):
    ''' update inventory of reserved instances '''
    reservations = []
    try:
        reservations = ec2conn.get_all_reserved_instances()
    except boto.exception.EC2ResponseError as exc:
        log.error("Error communicating with AWS: %s\n\n", exc.message)
        return

    objects = []
    for rsrv in reservations:
        obj = (AwsReservationInventory,
               {'reservation_id':rsrv.id},
               {'instance_type' : rsrv.instance_type,
                'availability_zone' : rsrv.availability_zone,
                'account' : get_account_number(account),
                'purchase_date' : date_parser.parse(rsrv.start
                                                   ).strftime(DATE_FORMAT),
                'expiration_date' : date_parser.parse(rsrv.end
                                                     ).strftime(DATE_FORMAT),
                'instance_count' : rsrv.instance_count})
        objects.append(obj)
    return objects

def expire_instances():
    ''' mark any instances that weren't updated as terminated. if we didn't see
        them on this pass, it means they are gone.
    '''
    DBSession.query(AwsInstanceInventory
                   ).filter(AwsInstanceInventory.check_date != CHECK_DATE
                           ).update({'status' : 'terminated',
                                     'check_date' : CHECK_DATE})
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
        regions = boto.ec2.regions()

        for region in regions:
            # skip restricted access regions
            if region.name in ['us-gov-west-1', 'cn-north-1']:
                continue

            log.debug('checking %s: %s', account, region.name)
            ec2 = boto.ec2.connect_to_region(region.name,
                                             aws_access_key_id=access_key,
                                             aws_secret_access_key=secret_key)

            run1 = pool.apply_async(update_instance_inventory,
                                    (ec2, account),
                                    callback=objects.extend)
            run2 = pool.apply_async(update_reservation_inventory,
                                    (ec2, account),
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
