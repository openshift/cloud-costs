import transaction
import unittest

from datetime import datetime, timedelta
from pyramid import testing

from budget.models import (Base,
                           DBSession,
                           GcpLineItem)

now = datetime.now()
today = datetime(now.year, now.month, now.day, 0, 0, 0)
yesterday = today - timedelta(days=1)

class TestFilenameTodate(unittest.TestCase):
    def runTest(self):
        from budget.scripts.gcp_billing_import import filename_to_date
        filename = 'gcp-billing-2001-02-03.json'
        result = filename_to_date(filename)
        self.assertEqual(result, datetime(2001, 2, 3, 0, 0, 0))

class TestDateToFilename(unittest.TestCase):
    def runTest(self):
        from budget.scripts.gcp_billing_import import date_to_filename
        result = date_to_filename(datetime(2001, 2, 3))
        self.assertEqual(result, 'gcp-billing-2001-02-03.json')

class TestInsertData(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        import os
        cache_dir = os.path.dirname(__file__) + "/gcp"

        from budget.scripts.gcp_billing_import import insert_data
        filename = 'gcp-billing-2001-01-01.json'
        insert_data(filename, cache_dir)
        result = DBSession.query(GcpLineItem).all()
        self.assertEqual(result[0].cost_amount, 1.234567)

class TestRunWithDate(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        import os
        from budget.scripts.gcp_billing_import import run
        settings = {'cache.dir' : os.path.dirname(__file__)}
        options = {'rundate' : '2001-01-01', 'nocacheupdate' : True}
        run(settings, options)
        result = DBSession.query(GcpLineItem).all()
        self.assertEqual(result[0].cost_amount, 1.234567)

class TestRunWithoutDate(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    #TODO: because of how run() works, we need to write out the test data file
    # to be <6 months old.

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        import os
        from budget.scripts.gcp_billing_import import run
        settings = {'cache.dir' : os.path.dirname(__file__)}
        options = {'nocacheupdate' : True}
        run(settings, options)
        result = DBSession.query(GcpLineItem).all()
        self.assertEqual(result[0].cost_amount, 1.234567)
