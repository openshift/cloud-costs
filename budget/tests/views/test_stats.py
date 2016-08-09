import unittest
import transaction

from pyramid import testing

from budget.models import DBSession

from budget.models import (
    Base,
    AwsAccountMetadata,
    AwsCostAllocation,
    )

class TestStatsIndex(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def runTest(self):
        from budget.views.stats import stats_index
        request = testing.DummyRequest()
        request.context = testing.DummyResource()

        results = stats_index(request)
        self.assertEqual(results.keys(), ['graph','notes','selectors'])
        self.assertEqual(results['graph'], None)
        self.assertEqual(results['selectors'], {})
        self.assertEqual(results['notes'], '')


