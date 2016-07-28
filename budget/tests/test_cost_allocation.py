import unittest
import transaction

from datetime import datetime,timedelta
from pyramid import testing

from budget.models import DBSession

from budget.models import (
    Base,
    AwsAccountMetadata,
    AwsCostAllocation,
    )

now = datetime.now()
today = datetime(now.year,now.month,now.day,0,0,0)
yesterday = today - timedelta(days=1)

class TestCostAllocationGetMetadata(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from budget.models import (
            Base,
            AwsCostAllocation,
            )
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            meta = AwsAccountMetadata(
                        account_id = 0,
                        account_name = 'account name',
                        tags = "Lorem,ipsum,dolor,sit,amet,consectetur"
                    )
            DBSession.add(meta)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.views.cost_allocation import get_metadata
        info = get_metadata(0)
        self.assertEqual(info,
                ['Lorem','ipsum','dolor','sit','amet','consectetur'])

class TestCostAllocationGraph(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from budget.models import (
            Base,
            AwsCostAllocation,
            )
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            cost = AwsCostAllocation(
                        invoice_id = 'invoice id',
                        payer_account_id = 0,
                        linked_account_id = 0,
                        record_type = 'AccountTotal',
                        record_id = 0,
                        billing_period_start_date = yesterday,
                        billing_period_end_date = today,
                        invoice_date = today,
                        payer_account_name = 'payer account name',
                        linked_account_name = 'linked account name',
                        taxation_address = 'tax address',
                        payer_po_number = 0,
                        product_code = 'product code',
                        product_name = 'product name',
                        seller_of_record = 'seller',
                        usage_type = 'usage type',
                        operation = 'operation',
                        availability_zone = 'availability zone',
                        rate_id = 0,
                        item_description = 'description',
                        usage_start_date = yesterday,
                        usage_end_date = today,
                        usage_quantity = 1.0001,
                        blended_rate = 2.0002,
                        currency_code = 'currency',
                        cost_before_tax = 3.0003,
                        credits = 4.0004,
                        tax_amount = 5.0005,
                        tax_type = 'tax',
                        total_cost = 6.0006,
                        user_environment = 'env',
                        user_node = 'node'
                    )
            DBSession.add(cost)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.views.cost_allocation import cost_allocation_graph
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        request.params = { 'caller' : 'foo-0' }
        info = cost_allocation_graph(request)
        self.assertEqual(info['data'].data, 
                [{ 'key':'foo-0',
                    'values':[{'value': '6.001',
                                'label': yesterday.strftime('%Y-%m-%d')}]}])

class TestCostAllocationByAccount(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            cost = AwsCostAllocation(
                        invoice_id = 'invoice id',
                        payer_account_id = 0,
                        linked_account_id = 0,
                        record_type = 'AccountTotal',
                        record_id = 0,
                        billing_period_start_date = yesterday,
                        billing_period_end_date = today,
                        invoice_date = today,
                        payer_account_name = 'payer account name',
                        linked_account_name = 'linked account name',
                        taxation_address = 'tax address',
                        payer_po_number = 0,
                        product_code = 'product code',
                        product_name = 'product name',
                        seller_of_record = 'seller',
                        usage_type = 'usage type',
                        operation = 'operation',
                        availability_zone = 'availability zone',
                        rate_id = 0,
                        item_description = 'description',
                        usage_start_date = yesterday,
                        usage_end_date = today,
                        usage_quantity = 1.0001,
                        blended_rate = 2.0002,
                        currency_code = 'currency',
                        cost_before_tax = 3.0003,
                        credits = 4.0004,
                        tax_amount = 5.0005,
                        tax_type = 'tax',
                        total_cost = 6.0006,
                        user_environment = 'env',
                        user_node = 'node'
                    )
            meta = AwsAccountMetadata(
                        account_id = 0,
                        account_name = 'account name',
                        tags = "Lorem,ipsum,dolor,sit,amet,consectetur"
                    )
            DBSession.add(meta)
            DBSession.add(cost)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.views.cost_allocation import cost_allocation_by_account
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        request.params = { 'date' : yesterday.strftime('%Y-%m-%d') }
        info = cost_allocation_by_account(request)
        self.assertEqual(info['selectors']['date']['selected'], yesterday.strftime('%Y-%m-%d'))
        self.assertEqual(info['totals'], {u'linked account name [0]':{u'product name':'6.00'}})

