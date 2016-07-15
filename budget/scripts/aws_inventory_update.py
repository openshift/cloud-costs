#!/usr/bin/env python

import boto.ec2
import logging
import os
import sys
import transaction

from datetime import datetime
from dateutil import parser as date_parser
from multiprocessing import Pool, Queue

from sqlalchemy import engine_from_config
from sqlalchemy.sql import functions
from sqlalchemy.sql.expression import ClauseElement

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
                        DBSession,
                        AwsInstanceInventory,
                        AwsReservationInventory,
                        Base,
                    )

from ..util.fileloader import load_yaml

MAX_PROCESSES = 20

def update_instance_inventory(ec2conn, account):
    instances = []
    try:
        instances = ec2conn.get_only_instances()
    except boto.exception.EC2ResponseError as e:
        log.error("Error communicating with AWS: %s\n\n" % e.message)
        return
    except SSLError  as e:
        log.error("Error communicating with AWS: %s\n\n" % e.message)
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

        obj = insert_or_update(DBSession, AwsInstanceInventory,
                    defaults = { 'check_date' : now },
                    instance_id = inst.id,
                    name = name,
                    environment = env,
                    instance_type = inst.instance_type,
                    availability_zone = inst.placement,
                    account = get_account_number(account),
                    status = inst.state,
                    launch_date = date_parser.parse(inst.launch_time).strftime("%Y-%m-%d %H:%M:%S"),
                )
        objects.append(obj)
    return objects

def update_reservation_inventory(ec2conn, account):
    reservations = []
    try:
        reservations = ec2conn.get_all_reserved_instances()
    except boto.exception.EC2ResponseError as e:
        log.error("Error communicating with AWS: %s\n\n" % e.message)
        return

    objects = []
    for rsrv in reservations:
        log.debug(rsrv.instance_count)
        obj = insert_or_update(DBSession, AwsReservationInventory,
                    reservation_id = rsrv.id,
                    instance_type = rsrv.instance_type,
                    availability_zone = rsrv.availability_zone,
                    account = get_account_number(account),
                    purchase_date = date_parser.parse(rsrv.start).strftime("%Y-%m-%d %H:%M:%S"),
                    expiration_date = date_parser.parse(rsrv.end).strftime("%Y-%m-%d %H:%M:%S"),
                    instance_count = rsrv.instance_count
                )
        objects.append(obj)
    return objects

def get_creds(account):
    awscreds = load_yaml(creds_file)
    access_key = awscreds[account]['access_key']
    secret_key = awscreds[account]['secret_key']
    return (access_key, secret_key)

def get_accounts():
    return sorted(load_yaml(creds_file).keys())

def get_account_number(name):
    return load_yaml(creds_file)[name]['account']

# https://stackoverflow.com/questions/6611563/sqlalchemy-on-duplicate-key-update
def insert_or_update(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = dict((k, v) for k, v in kwargs.iteritems() if not isinstance(v, ClauseElement))
        if defaults:
            params.update(defaults)
        instance = model(**params)
        return instance

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    global settings
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    global creds_file
    creds_file = settings['creds.dir'] + "/creds.yaml"

    global now
    now = datetime.now()

    # global to enable us to handle KeyboardInterrupts without leaving zombies around.
    global pool
    pool = Pool(processes=MAX_PROCESSES)

    objects = []
    pids = []

    for account in get_accounts():
        access_key, secret_key = get_creds(account)
        regions = boto.ec2.regions()

        for region in regions:
            # skip restricted access regions
            if region.name in [ 'us-gov-west-1', 'cn-north-1' ]:
                continue

            log.debug('checking %s: %s' % (account,region.name))
            ec2 = boto.ec2.connect_to_region(region.name,
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key)

            r1 = pool.apply_async(update_instance_inventory, (ec2, account),
                    callback=objects.extend)
            r2 = pool.apply_async(update_reservation_inventory, (ec2, account),
                    callback=objects.extend)

            pids.append(r1)
            pids.append(r2)

    # get the output of all our processes
    for pid in pids:
        pid.get()

    # ensure the sqlalchemy objects aren't garbage-collected before we commit them.
    # see:
    # http://docs.sqlalchemy.org/en/latest/orm/session_state_management.html#session-referencing-behavior
    merged = []
    for obj in objects:
        merged.append(DBSession.merge(obj))
    transaction.commit()

    pool.close()
    pool.join()

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
        pool.terminate()
        pool.join()
