#!/usr/bin/env python

import csv
import logging
import os
import sys
import transaction

from datetime import datetime
from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from budget.models import DBSession, ExpensedCost, Base

def insert_data():
    filename = cache_dir+'/other_expenses.csv'
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        header = reader.next() # pop the header

        for row in reader:
            for idx,el in enumerate(row):
                if idx > 0 and float(el) > 0.0:
                    data.append(ExpensedCost(
                        vendor=header[idx],
                        invoice_date=datetime.strptime(row[0],'%Y-%m-%d'),
                        amount=el
                    ))
    DBSession.add_all(data)
    transaction.commit()

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

    global cache_dir
    cache_dir = settings['cache.dir']

    insert_data()

    #Base.metadata.create_all(engine)
    #with transaction.manager:
    #    model = MyModel(name='one', value=1)
    #    DBSession.add(model)

if '__main__' in __name__:
    try:
        main()
    except KeyboardInterrupt:
        print "Ctrl+C detected. Exiting..."
