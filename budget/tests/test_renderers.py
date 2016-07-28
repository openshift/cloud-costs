import unittest
from budget.renderers import CSVRenderer
from pyramid import testing

class TestCsvRenderer(unittest.TestCase):
    data = { 'header' : ['x','y','z'],
            'rows': [[1,2,3],[4,5,6],[7,8,9]] }

    csv = "x,y,z\r\n1,2,3\r\n4,5,6\r\n7,8,9\r\n"

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def _makeOne(self, info):
        return CSVRenderer(info)

    def test_it(self):
        request = testing.DummyRequest()
        renderer = self._makeOne('foo')(self.data,{'request':request})
        self.assertEqual(renderer, self.csv)
        self.assertEqual(request.response.content_type, 'text/csv')

    def test_with_request_content_type_set(self):
        request = testing.DummyRequest()
        request.response.content_type = 'text/mishmash'
        renderer = self._makeOne('foo')(self.data,{'request':request})
        self.assertEqual(request.response.content_type, 'text/mishmash')

