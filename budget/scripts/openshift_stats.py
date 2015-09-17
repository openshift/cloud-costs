#!/usr/bin/env python

import getpass
import json
import logging
import os
import paramiko
import random
import subprocess
import sys
import transaction

from datetime import datetime
from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from budget.models import DBSession, OpenshiftProfileStats, Base

brokers = [
        'use-srv1.prod.rhcloud.com',
        'use-srv2.prod.rhcloud.com',
        'use-srv3.prod.rhcloud.com',
        'use-srv4.prod.rhcloud.com',
        ]
sshkey = "/home/%s/.ssh/id_rsa" % getpass.getuser()
stats_filename = 'oostats.json'


def collect_stats():
    log.info("collecting stats from a broker...")

    key = paramiko.RSAKey.from_private_key_file(sshkey)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
            hostname=random.choice(brokers),
            username='root',
            pkey=key
            )
    stdin,stdout,stderr = client.exec_command('/usr/sbin/oo-stats -f json')
    save_json(stats_filename, stdout.read())


def insert_stats():
    oostats = load_json(stats_filename)
    stats = []
    for profile in oostats['profile_summaries']:
        stats.append(OpenshiftProfileStats(
            gears_total_count = profile['gears_total_count'],
            gears_active_count = profile['gears_active_count'],
            gears_idle_count = profile['gears_idle_count'],
            gears_stopped_count = profile['gears_stopped_count'],
            gears_unknown_count = profile['gears_unknown_count'],
            nodes_count = profile['nodes_count'],
            profile_name = profile['profile'],
            collection_date = datetime.today()
        ))
    DBSession.add_all(stats)
    transaction.commit()

def load_json(filename):
    try:
        fh = json.loads(json.load(open(filename, 'r+')))
    except IOError:
        fh = json.loads('{}')
    return fh


def save_json(filename, data):
    try:
        json.dump(data, open(filename, 'w+'))
    except IOError:
        raise

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    try:
        delta = datetime.now() - datetime.fromtimestamp(os.path.getmtime(stats_filename))
        if delta.days > 1 or os.path.getsize(stats_filename) == 0:
            collect_stats()
    except OSError as e:
        collect_stats()

    insert_stats()

    #Base.metadata.create_all(engine)
    #with transaction.manager:
    #    model = MyModel(name='one', value=1)
    #    DBSession.add(model)

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
