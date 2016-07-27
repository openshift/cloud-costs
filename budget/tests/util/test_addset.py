import unittest
import budget.util.addset as a

class TestAddSet(unittest.TestCase):
    def key_exists(self):
        foo = { 'foo' : 0 }
        foo = a.addset(foo, 'foo', 1)
        self.assertEqual(foo['foo'], 1)

    def key_absent(self):
        foo = {}
        foo = a.addset(foo, 'foo', 1)
        self.assertEqual(foo['foo'], 1)

    def runTest(self):
        self.key_exists()
        self.key_absent()
