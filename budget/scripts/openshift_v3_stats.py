#!/usr/bin/python
""" This script processes yaml stats files collected from openshift v3 systems """

# Copyright 2016 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
import os
import re
import sys
import tarfile
import transaction

from datetime import datetime

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from budget.models import DBSession, OpenshiftV3ProfileStats, Base

from ..util.fileloader import load_yaml, save_yaml
from ..util.addset import addset

def usage():
    ''' how to call this program '''
    print "Usage: %s <config_uri> [statsfile-YYYY-MM-DD.tar.bz2]" % sys.argv[0]
    sys.exit()

def parse_name(filename):
    """ parses a yaml filename for individual components.
        this is tightly coupled to the anisble playbook that collects the stats
    """
    arr = filename.split('.')[0].split('-')
    return {'data_type' : arr.pop(0),
            'collect_date' : '-'.join(pop_slice(arr, 3)),
            'cluster_name': '-'.join(arr)}

def pop_slice(lis, num):
    ''' pop an array slice of num length off the end of an array '''
    sliced = lis[-num:]
    del lis[-num:]
    return sliced

def calc_nodes(yml):
    ''' calculates total number of nodes and pod capacity by node type '''
    data = {}
    for item in yml['items']:
        pod_capacity = int(item['status']['capacity']['pods'])

        try:
            node_type = item['metadata']['labels']['type']
        except KeyError:
            node_type = 'unknown'

        if node_type not in data:
            data[node_type] = {}

        data[node_type]['pod_capacity'] = pod_capacity
        addset(data[node_type], 'total_nodes', 1)

    return data

def prepare_nodes(dataset):
    """ add node data to the DB object """
    totals = {}

    # key: cluster name
    for data in dataset:
        # key: cluster type
        for datum in dataset[data]:
            if datum not in totals:
                totals[datum] = {}

            addset(totals[datum], 'pod_capacity', dataset[data][datum]['pod_capacity'])
            addset(totals[datum], 'nodes', dataset[data][datum]['total_nodes'])

    result = {'clusters':len(dataset.keys())}
    for total in totals:
        result["%s_nodes" % total] = totals[total]['nodes']
        result["%s_node_pod_capacity" % total] = totals[total]['pod_capacity']

    return result

def calc_pods(yml):
    ''' calculates total number of pods and individual container states '''
    pods = {}
    containers = {}
    pod_total = 0
    container_total = 0
    for item in yml['items']:
        if item['kind'] == 'Pod' and 'conditions' in item['status']:
            for status in item['status']['containerStatuses']:
                for state in status['state'].keys():
                    container = status['name']

                    if state in containers:
                        containers[state].append(container)
                    else:
                        containers[state] = [container]
                container_total = container_total + 1

        phase = item['status']['phase']
        uid = item['metadata']['uid']
        if phase in pods:
            pods[phase].append(uid)
        else:
            pods[phase] = [uid]
        pod_total = pod_total + 1

    return {'total_pods' : pod_total,
            'total_containers' : container_total,
            'pods' : pods,
            'containers' : containers}

def prepare_pods(dataset):
    """ add pod data to db object """
    total_pods = 0
    total_containers = 0
    state_totals = {'pods':{}, 'containers':{}}

    # key: cluster name
    for cluster in dataset:
        pods = dataset[cluster].pop('total_pods')
        total_pods = total_pods + pods
        containers = dataset[cluster].pop('total_containers')
        total_containers = total_containers + containers
        # key: pods or containers
        for key in dataset[cluster]:
            # key: state
            for state in dataset[cluster][key]:
                addset(state_totals[key], state, len(dataset[cluster][key][state]))


    result = {'total_pods':total_pods,'total_containers':total_containers}
    for pod_con in state_totals:
        for state in state_totals[pod_con]:
            result["%s_%s" % (state.lower(), pod_con)] = state_totals[pod_con][state]
    return result

def calc_projects(yml):
    ''' calculates total number of projects and project states '''
    data = {}
    total = 0

    for item in yml['items']:
        if item['kind'] == 'Project':
            addset(data, item['status']['phase'], 1)
            total = total + 1

    data['total_projects'] = total
    return data

def prepare_projects(dataset):
    """ add project data to db object """
    totals = {}

    # key: cluster name
    for data in dataset:
        # key: data type
        for datum in dataset[data]:
            addset(totals, datum, dataset[data][datum])

    result = { 'projects' : totals.pop('total_projects') }

    for total in totals:
        result["%s_containers" % total.lower()] = totals[total]

    return result

def calc_users(yml):
    ''' calculates total number of users '''
    users = []
    for item in yml['items']:
        if 'fullName' in item:
            users = item
    return {'total_users' : len(users)}

def prepare_users(dataset):
    """ add user data to db object """
    totals = {}

    # key: cluster name
    for data in dataset:
        # key: data type
        for datum in dataset[data]:
            addset(totals, datum, dataset[data][datum])

    return {'users':totals.pop('total_users')}

def select_latest():
    ''' examines filename for YYYY-MM-DD portion of filename, returns latest '''

    # os.walk returns (dirpath, dirnames, filenames)
    # we only use the filenames.
    bz2_files = []
    for (_, _, filenames) in os.walk(cache_dir):
        bz2_files.extend([f for f in filenames if re.search(r'\.bz2$', f)])

    regex = r'^v3stats-(\d{4}-\d{2}-\d{2})\.tar\.bz2$'
    latest = max([re.search(regex, f).groups()[0] for f in bz2_files if re.search(regex, f)])

    return '%s/v3stats-%s.tar.bz2' % (cache_dir, latest)

def get_collection_date(filename):
    ''' parse collection_date from filename '''
    rgx = re.compile(r'v3stats-(\d{4}-\d{2}-\d{2}).tar.bz2')
    g, = rgx.search(filename).groups()
    return datetime.strptime(g,'%Y-%m-%d')

def main(args):
    ''' entry point '''

    if len(args) < 1:
        usage()

    selected = None
    if len(args) > 2:
        selected = args[2]
        if not os.path.exists(selected):
            usage()

    config_uri = args[1]
    options = parse_vars(args[3:])

    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    setup_logging(config_uri)
    global log
    log = logging.getLogger(__name__)

    global cache_dir
    cache_dir = settings['cache.dir'] + "/v3stats"

    if not selected:
        selected = select_latest()

    collection_date = get_collection_date(selected)

    log.info('processing %s.' % selected)

    tar = tarfile.open(selected, 'r:bz2')
    member_list = tar.getmembers()
    # skip the directory entry in the tar file
    member_list.pop(0)

    data = {}
    for member in member_list:
        log.info('processing %s.' % member)
        # pylint: disable=unused-variable
        yml = load_yaml(tar.extractfile(member))

        parsed_name = parse_name(member.name.split('/')[-1])
        if parsed_name['data_type'] not in data:
            data[parsed_name['data_type']] = {}

        # call appropriate calc_* method
        # pylint: disable=eval-used
        output = eval("calc_"+parsed_name['data_type']+"(yml)")
        data[parsed_name['data_type']][parsed_name['cluster_name']] = output

    log.debug(data)
    # pylint: disable=unused-variable
    row_params = { 'collection_date' : collection_date,
                    'clusters' : 0,
                    'compute_nodes' : 0,
                    'compute_node_pod_capacity' : 0,
                    'master_nodes' : 0,
                    'master_node_pod_capacity' : 0,
                    'unknown_nodes' : 0,
                    'unknown_node_pod_capacity' : 0,
                    'infra_nodes' : 0,
                    'infra_node_pod_capacity' : 0,
                    'total_pods' : 0,
                    'total_containers' : 0,
                    'terminated_containers' : 0,
                    'terminating_containers' : 0,
                    'waiting_containers' : 0,
                    'running_containers' : 0,
                    'failed_pods' : 0,
                    'running_pods' : 0,
                    'pending_pods' : 0,
                    'succeeded_pods' : 0,
                    'users' : 0,
                    'projects' : 0,
                    'active_projects' : 0,
                    'terminating_projects' : 0,
                }
    for datum in data:
        # call appropriate method
        # pylint: disable=eval-used
        eval("row_params.update(prepare_"+datum+"(data[datum]))")

    log.debug(row_params)
    #row = OpenshiftV3ProfileStats(**row_params)
    #DBSession.add(row)
    #transaction.commit()

if '__main__' in __name__:
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print "Ctrl-C detected. Exiting."
        sys.exit()
