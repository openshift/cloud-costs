import unittest
from budget.renderers import CSVRenderer
from pyramid import testing

class TestCsvRenderer(unittest.TestCase):
    data = {'header' : ['x', 'y', 'z'],
            'rows': [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}

    csv = "x,y,z\r\n1,2,3\r\n4,5,6\r\n7,8,9\r\n"

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def runTest(self):
        self.test_defaults()
        self.test_with_content_type()
        self.test_without_request()

    def test_defaults(self):
        ''' test that the defaults work and that they don't change the request
        '''
        request = testing.DummyRequest()
        renderer = CSVRenderer('foo')(self.data, {'request':request})
        self.assertEqual(request.response.content_type, 'text/csv')
        self.assertEqual(renderer, self.csv)

    def test_with_content_type(self):
        ''' test that we can change our content-type in the request '''
        request = testing.DummyRequest()
        request.response.content_type = 'text/mishmash'
        renderer = CSVRenderer('foo')(self.data, {'request':request})
        self.assertEqual(request.response.content_type, 'text/mishmash')
        self.assertEqual(renderer, self.csv)

    def test_without_request(self):
        ''' test null inputs still produces the expected csv '''
        renderer = CSVRenderer()(self.data, {'request':None})
        self.assertEqual(renderer, self.csv)
