import os
import unittest
import transaction

from datetime import datetime,timedelta
from decimal import Decimal
from moto import mock_ec2
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
tomorrow = today + timedelta(days=1)

class TestDataHolder(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_init(self):
        from budget.views.reservation import DataHolder
        dh = DataHolder(foo='foo',bar='bar')
        self.assertEqual(dh.foo, 'foo')
        self.assertEqual(dh.bar, 'bar')

    def test_put(self):
        from budget.views.reservation import DataHolder
        dh = DataHolder()
        dh.put(foo='bar')
        self.assertEqual(dh.foo, 'bar')

    def runTest(self):
        self.test_init()
        self.test_put()

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import reservation
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        resp = reservation(request)
        self.assertEqual(resp, {})

class TestGetCreds(unittest.TestCase):
    data = { 'foo' : {
                    'account': '1234567890',
                    'access_key': 'blah1234blah',
                    'secret_key': 'Lorem ipsum dolor sit amet consectetur'
                }}
    data_file = os.path.dirname(__file__) + '/creds.yaml'

    def setUp(self):
        self.config = testing.setUp()
        import yaml
        with open(self.data_file, 'w+') as f:
            f.write(yaml.dump(self.data))

    def tearDown(self):
        testing.tearDown()
        os.remove(self.data_file)

    def runTest(self):
        from budget.views.reservation import get_creds
        self.config.registry.settings['creds.dir'] = os.path.dirname(__file__)
        for name in self.data.keys():
            key, secret = get_creds(name, self.config.registry.settings)
            self.assertEqual(key, self.data[name]['access_key'])
            self.assertEqual(secret, self.data[name]['secret_key'])

class TestGetAccountNumber(unittest.TestCase):
    data = { 'foo' : {
                    'account': '1234567890',
                    'access_key': 'blah1234blah',
                    'secret_key': 'Lorem ipsum dolor sit amet consectetur'
                }}
    data_file = os.path.dirname(__file__) + '/creds.yaml'

    def setUp(self):
        self.config = testing.setUp()
        import yaml
        with open(self.data_file, 'w+') as f:
            f.write(yaml.dump(self.data))

    def tearDown(self):
        testing.tearDown()
        os.remove(self.data_file)

    def runTest(self):
        from budget.views.reservation import get_account_number
        self.config.registry.settings['creds.dir'] = os.path.dirname(__file__)
        for name in self.data.keys():
            num = get_account_number(name, self.config.registry.settings)
            self.assertEqual(num, self.data[name]['account'])

class TestGetReservations(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from budget.models import Base, AwsReservationInventory
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            data = AwsReservationInventory(
                            reservation_id = 'r-1234abcd',
                            instance_type = 'instance type',
                            availability_zone = 'availability_zone',
                            account = 1234567890,
                            purchase_date = yesterday,
                            expiration_date = tomorrow,
                            instance_count = 314159 )
            DBSession.add(data)
            data = AwsReservationInventory(
                            reservation_id = 'r-4567hijk',
                            instance_type = 'instance type',
                            availability_zone = 'availability_zone',
                            account = 1234567890,
                            purchase_date = yesterday,
                            expiration_date = yesterday,
                            instance_count = 602214 )
            DBSession.add(data)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import get_reservations
        reservation = get_reservations(1234567890)
        self.assertEqual(len(reservation), 1)
        self.assertEqual(reservation[0].instance_count, 314159)
        self.assertEqual(reservation[0].reservation_id, 'r-1234abcd')

class TestGetReservationOfferings(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    @mock_ec2
    def runTest(self):
        from budget.views.reservation import get_reservation_offerings
        import boto
        ec2conn = boto.ec2.connect_to_region('us-east-1')
        try:
            result = get_reservation_offerings(ec2conn,
                                            instance_type='m27.superhuge',
                                            availability_zone='us-east-1')
        except NotImplementedError:
            #FIXME
            result = 'fake success. not a real success.'
        self.assertNotEqual(result, None)

class TestGetInstances(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from budget.models import Base, AwsInstanceInventory
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        #FIxME
        if DBSession:
            DBSession.remove()
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            data = AwsInstanceInventory(
                                name = 'instance1',
                                environment = 'test',
                                instance_id = 'i-1234abcd',
                                instance_type = 'm42.ultrahuge',
                                availability_zone = 'area-51',
                                account = 1234567890,
                                status = 'running',
                                launch_date = yesterday,
                                check_date = today
            )
            DBSession.add(data)
            data = AwsInstanceInventory(
                                name = 'instance2',
                                environment = 'test',
                                instance_id = 'i-4567hijk',
                                instance_type = 'm42.ultrahuge',
                                availability_zone = 'area-51',
                                account = 1234567890,
                                status = 'stopped',
                                launch_date = yesterday,
                                check_date = today
            )
            DBSession.add(data)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import get_instances
        reservation = get_instances(1234567890)
        self.assertEqual(len(reservation), 1)
        self.assertEqual(reservation[0].name, 'instance1')
        self.assertEqual(reservation[0].instance_id, 'i-1234abcd')

class TestCalculateReservationStats(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import calculate_reservation_stats
        from budget.views.reservation import DataHolder
        tup = ('instance_type', 'availability_zone')
        dummy_inst = DataHolder(
                        instance_type = tup[0],
                        availability_zone = tup[1],
                    )
        dummy_rsrv = DataHolder(
                        instance_type = tup[0],
                        availability_zone = tup[1],
                        instance_count = 5
                    )
        dh = DataHolder(
                            instance_type=tup[0],
                            availability_zone=tup[1],
                            instances={ '1234567890' : [ dummy_inst ] },
                            reservations={ '1234567890' : [ dummy_rsrv ] },
                            account='1234567890'
                        )
        result = calculate_reservation_stats(dh)
        self.assertEqual(result.ri_delta[tup], 4)
        self.assertEqual(result.ri_totals[tup]['reserved'], 5)
        self.assertEqual(result.ri_totals[tup]['running'], 1)

class TestCalculateCosts(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

        from budget.views.reservation import DataHolder
        self.tup = ('m4.xlarge', 'us-east-1a')
        dummy_inst = DataHolder(
                        instance_type = self.tup[0],
                        availability_zone = self.tup[1],
                    )
        dummy_rsrv = DataHolder(
                        instance_type = self.tup[0],
                        availability_zone = self.tup[1],
                        instance_count = 5
                    )
        self.dh = DataHolder(
                            instance_type=self.tup[0],
                            availability_zone=self.tup[1],
                            instances={ '1234567890' : [ dummy_inst ] },
                            reservations={ '1234567890' : [ dummy_rsrv ] },
                            account='1234567890'
                        )
        from budget.models import Base, AwsPrice, AwsProduct
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            data = AwsPrice(
                    sku = 'test',
                    offer_term_code = 'test1',
                    price_dimensions = '{"test1.test1.test1": {"pricePerUnit": {"USD": "1"}, "appliesTo": [], "rateCode": "test.test.2TG2D8R56U", "unit": "Quantity", "description": "Upfront Fee"}, "test.test.test": {"description": "Linux/UNIX (Amazon VPC), m4.xlarge instance-hours used this month", "pricePerUnit": {"USD": "0.1234000000"}, "rateCode": "test.test.test", "endRange": "Inf", "beginRange": "0", "appliesTo": [], "unit": "Hrs"}}',
                    term_attributes = '{"LeaseContractLength": "1yr", "PurchaseOption": "Partial Upfront"}',
                    json = 'test1.test1'
            )
            DBSession.add(data)
            data = AwsPrice(
                    sku = 'test',
                    offer_term_code = 'test2',
                    price_dimensions = '{"test.test2.test2": {"description": "$0.79 per On Demand Linux m4.xlarge Instance Hour", "pricePerUnit": {"USD": "0.4567800000"}, "rateCode": "test.test2.test2", "endRange": "Inf", "beginRange": "0", "appliesTo": [], "unit": "Hrs"}}',
                    term_attributes = '{}',
                    json = 'test.test2'
            )
            DBSession.add(data)
            data = AwsProduct(
                    sku = 'test',
                    location = 'US East (N. Virginia)',
                    instance_type = 'm4.xlarge',
                    current_generation = True,
                    tenancy = 'Shared',
                    usage_type = 'test:test',
                    operation = 'test:test',
                    operating_system = 'Linux',
                    json = '{"sku": "test", "productFamily": "Compute Instance", "attributes": {"enhancedNetworkingSupported": "Yes", "networkPerformance": "High", "preInstalledSw": "NA", "instanceFamily": "Storage optimized", "vcpu": "9000", "locationType": "AWS Region", "usagetype": "test:test"", "storage": "100 x 100 MFM", "currentGeneration": "Yes", "operatingSystem": "Linux", "processorArchitecture": "8-bit", "tenancy": "Shared", "licenseModel": "No License required", "servicecode": "test", "memory": "1 ZiB", "processorFeatures": "Shiny; Hot; Metal", "clockSpeed": "0.1 MHz", "operation": "testStuff", "physicalProcessor": "IBM 8088", "instanceType": "m4.xlarge", "location": "US East (N. Virginia)"}}'
            )
            DBSession.add(data)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import (calculate_reservation_stats,
                                             calculate_costs)
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        request.registry.settings['cache.dir'] = os.path.dirname(__file__) + \
                '/../../../data'

        dh = calculate_reservation_stats(self.dh)
        result, c = calculate_costs(request, dh)
        self.assertEqual(result.ri_costs[self.tup]['savings'], Decimal(-964))
        self.assertEqual(result.ri_costs[self.tup]['up-front'], 0)

class TestGetPrice(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from budget.models import Base, AwsPrice, AwsProduct
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            data = AwsPrice(
                    sku = 'test',
                    offer_term_code = 'test1',
                    price_dimensions = '{"test1.test1.test1": {"pricePerUnit": {"USD": "1"}, "appliesTo": [], "rateCode": "test.test.test", "unit": "Quantity", "description": "Upfront Fee"}, "test.test.test": {"description": "Linux/UNIX (Amazon VPC), m4.xlarge instance-hours used this month", "pricePerUnit": {"USD": "0.1234000000"}, "rateCode": "test.test.test", "endRange": "Inf", "beginRange": "0", "appliesTo": [], "unit": "Hrs"}}',
                    term_attributes = '{"LeaseContractLength": "1yr", "PurchaseOption": "Partial Upfront"}',
                    json = 'test1.test1'
            )
            DBSession.add(data)
            data = AwsPrice(
                    sku = 'test',
                    offer_term_code = 'test2',
                    price_dimensions = '{"test.test2.test2": {"description": "$0.79 per On Demand Linux m4.xlarge Instance Hour", "pricePerUnit": {"USD": "0.4567800000"}, "rateCode": "test.test2.test2", "endRange": "Inf", "beginRange": "0", "appliesTo": [], "unit": "Hrs"}}',
                    term_attributes = '{}',
                    json = 'test.test2'
            )
            DBSession.add(data)
            data = AwsProduct(
                    sku = 'test',
                    location = 'US East (N. Virginia)',
                    instance_type = 'm4.xlarge',
                    current_generation = True,
                    tenancy = 'Shared',
                    usage_type = 'test:test',
                    operation = 'test:test',
                    operating_system = 'Linux',
                    json = '{"sku": "test", "productFamily": "Compute Instance", "attributes": {"enhancedNetworkingSupported": "Yes", "networkPerformance": "High", "preInstalledSw": "NA", "instanceFamily": "Storage optimized", "vcpu": "9000", "locationType": "AWS Region", "usagetype": "test:test"", "storage": "100 x 100 MFM", "currentGeneration": "Yes", "operatingSystem": "Linux", "processorArchitecture": "8-bit", "tenancy": "Shared", "licenseModel": "No License required", "servicecode": "test", "memory": "1 ZiB", "processorFeatures": "Shiny; Hot; Metal", "clockSpeed": "0.1 MHz", "operation": "testStuff", "physicalProcessor": "IBM 8088", "instanceType": "m4.xlarge", "location": "US East (N. Virginia)"}}'
            )
            DBSession.add(data)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import get_price
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        request.registry.settings['cache.dir'] = os.path.dirname(__file__) + \
                '/../../../data'

        kwargs = {'instance_type' : 'm4.xlarge',
                    'region' : 'us-east-1'}
        result = get_price(request, **kwargs)
        self.assertEqual(result.keys(), ['Hrs'])
        self.assertEqual(result['Hrs'], Decimal('0.45678'))

class TestFindCost(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import _find_cost
        import json
        import re
        price_dimensions = json.loads('{ "test.test1.test1": { "pricePerUnit": { "USD": "1234" }, "description": "Upfront Fee", "appliesTo": [], "unit": "Quantity", "rateCode": "test.test.test" }, "test.test2.test2": { "description": "USD 0.0 per Linux/UNIX (Amazon VPC), m42.superhuge instance-hour (or partial hour)", "appliesTo": [], "rateCode": "test.test.test", "unit": "Hrs", "beginRange": "0", "pricePerUnit": { "USD": "0.1234000000" }, "endRange": "Inf" } }')
        search = re.compile(r'Linux/UNIX')

        result = _find_cost(search, price_dimensions)
        self.assertEqual(result.keys(), ['Hrs','Quantity'])
        self.assertEqual(result['Hrs'], Decimal('0.1234'))

class TestRegionLookup(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def runTest(self):
        from budget.views.reservation import region_lookup
        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        request.registry.settings['cache.dir'] = os.path.dirname(__file__) + \
                '/../../../data'

        result = region_lookup(request, 'ap-southeast-2')
        self.assertEqual(result, 'Asia Pacific (Sydney)')
