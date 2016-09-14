import os
import unittest
import budget.util.fileloader as f

class TestFileLoaderYaml(unittest.TestCase):
    testdir = os.path.dirname(__file__)
    data = testdir+'/fileloader.yaml'

    def runTest(self):
        test = f.load_yaml(self.data)
        self.assertEqual(test['Foo'], 'Bar')

        test['blah'] = ['blah blah']
        saved = None
        f.save_yaml(self.data+'.new', test)

        test2 = f.load_yaml(self.data+'.new')
        self.assertEqual(test, test2)

    def tearDown(self):
        os.remove(self.data+'.new')

class TestFileLoaderJson(unittest.TestCase):
    testdir = os.path.dirname(__file__)
    data = testdir+'/fileloader.json'

    def runTest(self):
        test = f.load_json(self.data)
        self.assertEqual(test['widget']['text']['number'], 42)

        test['blah'] = ['blah blah']
        saved = None
        f.save_json(self.data+'.new', test)

        test2 = f.load_json(self.data+'.new')
        self.assertEqual(test, test2)

    def tearDown(self):
        os.remove(self.data+'.new')
