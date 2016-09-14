import transaction
import unittest
import yaml

from datetime import datetime, timedelta
from pyramid import testing

from budget.models import (
    Base,
    DBSession,
    Openshift3Node,
    Openshift3Pod,
    Openshift3Project,
    Openshift3User
    )

now = datetime.now()
today = datetime(now.year, now.month, now.day, 0, 0, 0)
yesterday = today - timedelta(days=1)

class TestInsert(unittest.TestCase):
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
        from budget.scripts.openshift_v3_stats import update
        yml = yaml.load('''
apiVersion: v1
items:
- apiVersion: v1
  kind: Node
  metadata:
    creationTimestamp: 2001-01-01T12:00:00Z
    labels:
      color: red
      type: compute
    name: test
    uid: 12345678-1234-5678-1234-567812345678
  spec:
    externalID: i-123456789abcdef
    providerID: test:///test/i-123456789abcdef
  status:
    addresses:
    - address: 10.0.0.5
      type: InternalIP
    - address: 10.0.0.6
      type: ExternalIP
    allocatable:
      cpu: "2"
      memory: 2048Ki
      pods: "20"
    capacity:
      cpu: "2"
      memory: 2048Ki
      pods: "20"
    conditions:
    - lastHeartbeatTime: 2001-01-01T12:01:00Z
      lastTransitionTime: 2001-01-01T12:01:00Z
      message: kubelet is posting ready status
      reason: KubeletReady
      status: "True"
      type: Ready''')
        yaml_info = {'collection_date' : datetime.now(),
                     'cluster_id' : 'test'}
        lst = update(DBSession, Openshift3Node, yml, yaml_info)
        self.assertEqual(lst, ['12345678-1234-5678-1234-567812345678'])
        result = DBSession.query(Openshift3Node.uid).all()
        self.assertEqual(result, [(u'12345678-1234-5678-1234-567812345678',)])

class TestUpdate(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            node = Openshift3Node(
                    collection_date = yesterday,
                    create_date = yesterday,
                    end_date = None,
                    uid = '12345678-1234-5678-1234-567812345678',
                    status = '''
status:
  addresses:
  - address: 10.0.0.1
    type: InternalIP
  - address: 10.0.0.2
    type: ExternalIP
  allocatable:
    cpu: "1"
    memory: 1024Ki
    pods: "10"
  capacity:
    cpu: "1"
    memory: 1024Ki
    pods: "10"
  conditions:
  - lastHeartbeatTime: 2001-01-01T12:01:00Z
    lastTransitionTime: 2001-01-01T12:01:00Z
    message: kubelet is posting ready status
    reason: KubeletReady
    status: "True"
    type: Ready
''',
                    meta = '''
metadata:
  creationTimestamp: 2001-01-01T12:00:00Z
  labels:
    color: red
    type: compute
  name: test
  uid: 12345678-1234-5678-1234-567812345678
                    ''',
                    cluster_id = 'test'
                    )
            DBSession.add(node)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.scripts.openshift_v3_stats import update
        yml = yaml.load('''
apiVersion: v1
items:
- apiVersion: v1
  kind: Node
  metadata:
    creationTimestamp: 2001-01-01T12:00:00Z
    labels:
      color: red
      type: compute
    name: test
    uid: 12345678-1234-5678-1234-567812345678
  spec:
    externalID: i-123456789abcdef
    providerID: test:///test/i-123456789abcdef
  status:
    addresses:
    - address: 10.0.0.5
      type: InternalIP
    - address: 10.0.0.6
      type: ExternalIP
    allocatable:
      cpu: "2"
      memory: 2048Ki
      pods: "20"
    capacity:
      cpu: "2"
      memory: 2048Ki
      pods: "20"
    conditions:
    - lastHeartbeatTime: 2001-01-01T12:01:00Z
      lastTransitionTime: 2001-01-01T12:01:00Z
      message: kubelet is posting ready status
      reason: KubeletReady
      status: "True"
      type: Ready''')
        yaml_info = {'collection_date' : datetime.now(),
                     'cluster_id' : 'test'}
        lst = update(DBSession, Openshift3Node, yml, yaml_info)
        self.assertEqual(lst, ['12345678-1234-5678-1234-567812345678'])
        result = DBSession.query(Openshift3Node.uid).all()
        self.assertEqual(result, [(u'12345678-1234-5678-1234-567812345678',)])

class TestExpire(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            node1 = Openshift3Node(
                    collection_date = yesterday,
                    create_date = yesterday,
                    end_date = None,
                    uid = '12345678-1234-5678-1234-567812345678',
                    status = '''
status:
  addresses:
  - address: 10.0.0.1
    type: InternalIP
  - address: 10.0.0.2
    type: ExternalIP
  allocatable:
    cpu: "1"
    memory: 1024Ki
    pods: "10"
  capacity:
    cpu: "1"
    memory: 1024Ki
    pods: "10"
  conditions:
  - lastHeartbeatTime: 2001-01-01T12:01:00Z
    lastTransitionTime: 2001-01-01T12:01:00Z
    message: kubelet is posting ready status
    reason: KubeletReady
    status: "True"
    type: Ready
''',
                    meta = '''
metadata:
  creationTimestamp: 2001-01-01T12:00:00Z
  labels:
    color: red
    type: compute
  name: test
  uid: 12345678-1234-5678-1234-567812345678
                    ''',
                    cluster_id = 'test'
                    )
            node2 = Openshift3Node(
                    collection_date = yesterday,
                    create_date = yesterday,
                    end_date = None,
                    uid = '23456789-2345-6789-2345-678923456789',
                    status = '''
status:
  addresses:
  - address: 10.0.0.3
    type: InternalIP
  - address: 10.0.0.4
    type: ExternalIP
  allocatable:
    cpu: "1"
    memory: 1024Ki
    pods: "10"
  capacity:
    cpu: "1"
    memory: 1024Ki
    pods: "10"
  conditions:
  - lastHeartbeatTime: 2001-01-01T12:01:00Z
    lastTransitionTime: 2001-01-01T12:01:00Z
    message: kubelet is posting ready status
    reason: KubeletReady
    status: "True"
    type: Ready
''',
                    meta = '''
metadata:
  creationTimestamp: 2001-01-01T12:00:00Z
  labels:
    color: red
    type: compute
  name: test
  uid: 23456789-2345-6789-2345-678923456789
                    ''',
                    cluster_id = 'test'
                    )

            DBSession.add(node1)
            DBSession.add(node2)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def runTest(self):
        from budget.scripts.openshift_v3_stats import expire
        expire(DBSession, Openshift3Node, ['12345678-1234-5678-1234-567812345678'])
        result = DBSession.query(Openshift3Node.uid, Openshift3Node.end_date).all()
        self.assertEqual(result[0], ('12345678-1234-5678-1234-567812345678',None))
        self.assertEqual(result[1][0], '23456789-2345-6789-2345-678923456789')
        self.assertLessEqual((datetime.now()-result[1][1]).total_seconds(), 2)

class TestParseFilename(unittest.TestCase):
    def runTest(self):
        from budget.scripts.openshift_v3_stats import parse_filename
        result = parse_filename('pods-test-master-abcde-2001-01-01.yaml')
        self.assertEqual(result['type'], 'pods')
        self.assertEqual(result['cluster_id'], 'test')
        self.assertEqual(result['collection_date'], '2001-01-01')
