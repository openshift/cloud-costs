from datetime import datetime, timedelta
from decimal import Decimal

from pyramid.response import Response
from pyramid.view import view_config, render_view_to_response
from pyramid.events import subscriber, BeforeRender

from sqlalchemy.exc import DBAPIError
from sqlalchemy import not_, desc, asc, distinct, func

from ..models import *
from ..util.addset import addset
from ..util.tree import Branch, Leaf
from ..util.queries.aws import get_dates

import collections
import locale
import logging
import yaml

import budget.util.nvd3js as nvd3js

LOG = logging.getLogger(__name__)
LAST_YEAR = datetime.now() - timedelta(days=365)
LAST_MONTH = datetime.now() - timedelta(days=30)
locale.setlocale(locale.LC_ALL, "en_US")

# from:
# https://stackoverflow.com/questions/8063012/ajax-widgets-in-pyramid-and-chameleon
@subscriber(BeforeRender)
def add_render_view_global(event):
    ''' adds a global render_view callable '''
    LOG.debug(event)
    event['render_view'] = lambda name: render_view_to_response(\
                                            event['context'],
                                            event['request'],
                                            name=name,
                                            secure=True).ubody

def epoch_date(date):
    ''' return the unix epoch date for dates after Y2K '''
    # %s - undocumented pass-through to system's strftime.
    #      need to multiply by 1000 to hit the right century.
    return int(date.strftime('%s'))*1000

@view_config(name='widget_gcp', renderer='budget:templates/widgets/graph.pt')
def widget_gcp(request):
    ''' GCP cost graph widget '''
    LOG.debug(request.params)

    graph_data = {}
    seen_dates = set()
    projects = DBSession.query(GcpLineItem.project_name.distinct()).all()
    for prj, in projects:
        project = str(prj)

        if project not in graph_data.keys():
            graph_data[project] = set()

        start_times = DBSession.query(GcpLineItem.start_time.distinct()
                                     ).filter(\
                                       GcpLineItem.project_name == project,
                                       GcpLineItem.start_time >= LAST_MONTH,
                                             ).all()

        for start, in start_times:
            # ignore hourly variations because we're displaying a daily view
            day_begin = start.replace(hour=0, minute=0, second=0, tzinfo=None)
            day_end = start.replace(hour=23, minute=59, second=59, tzinfo=None)

            if day_begin not in seen_dates:
                seen_dates.add(epoch_date(day_begin))

            results = DBSession.query(func.sum(GcpLineItem.cost_amount
                                              )).filter(\
                                    GcpLineItem.project_name == project,
                                    GcpLineItem.start_time.between(day_begin,
                                                                   day_end),
                                                       ).all()

            for rslt, in results:
                data = (epoch_date(day_begin), rslt)
                graph_data[project].add(data)

    # remove spurious key.
    del graph_data['None']

    # ensure that the length of the coordinate value arrays are all the same.
    for key, val in graph_data.items():
        for dat in seen_dates-set(coord[0] for coord in val):
            graph_data[key].add((dat, 0))

    graph = nvd3js.StackedAreaChart(showLegend=False,
                                    useInteractiveGuideline=False,
                                    showControls=False,
                                    margin={'top': 10,
                                            'right': 10,
                                            'bottom': 60,
                                            'left': 50},
                                    showXAxis=False,
                                    extra="""
    chart.xAxis.tickFormat(function(d) { return d3.time.format('%x')(new Date(d)) });
    chart.yAxis.tickFormat(d3.format('$,.2f'));
            """)

    # sets are used above instead of lists to maintain uniqueness of the time
    # series data. however, now we need to convert the sets back to lists so
    # that __repr__() correctly renders them into javascript-parsable
    # representations. the time series is also sorted by date to aid client-side
    # rendering.
    graph.data = [{'key' : k,
                   'values' : sorted([list(val) for val in v],
                                     key=lambda x: x[0])
                  } for k, v in graph_data.items()]

    return {'graph' : graph, 'title' : 'GCP Costs'}

@view_config(name='widget_aws_cost',
             renderer='budget:templates/widgets/aws_cost.pt')
def widget_aws_cost(request):
    ''' Produce a hierarchy of cost-categories to provide a high-level summary
        of spending while enabling a user to drill-into the billing details.
    '''
    LOG.debug(request.params)

    dates, selected_date = get_dates(request.params)

    results = DBSession.query(AwsAccountMetadata.account_id,
                              AwsAccountMetadata.account_name,
                              AwsAccountMetadata.tags).all()

    # create objects of accounts and tags to build our hierarchy from
    accounts = {}
    tags = []
    for res in results:
        accounts[res.account_id] = {'account_name' : res.account_name,
                                    'tags' : res.tags.split(',')}
        for tag in res.tags.split(','):
            if tag not in tags:
                tags.append(tag)

    # distinct list of products
    products = DBSession.query(AwsCostAllocation.product_name.distinct()).all()

    # line items for the selected invoice
    cost_lines = DBSession.query(AwsCostAllocation.linked_account_id,
                                 AwsCostAllocation.linked_account_name,
                                 AwsCostAllocation.product_name,
                                 AwsCostAllocation.usage_type,
                                 AwsCostAllocation.item_description,
                                 AwsCostAllocation.usage_quantity,
                                 AwsCostAllocation.blended_rate,
                                 AwsCostAllocation.total_cost,
                                ).filter(
                                    AwsCostAllocation.billing_period_start_date == selected_date,
                                ).order_by(
                                    asc(AwsCostAllocation.linked_account_id),
                                    asc(AwsCostAllocation.usage_type)
                                ).all()

    # build out our hierarchy
    root = []

    # Tag-level
    for tag in sorted(tags):
        tag_branch = Branch(parent='', name=tag, datatype='tag')
        root.append(tag_branch)

        # Account-level
        for account in sorted(accounts,
                              key=lambda x: accounts[x]['account_name']):
            if tag not in accounts[account]['tags']:
                continue

            account_branch = Branch(parent=tag_branch,
                                    name=accounts[account]['account_name'],
                                    datatype='account')
            tag_branch.children.append(account_branch)

            # Product-level
            for product, in sorted(products, key=lambda x: x[0]):
                if product == '':
                    product_name = 'Total'
                else:
                    product_name = product

                product_branch = Branch(parent=account_branch,
                                        name=product_name,
                                        datatype='product')
                account_branch.children.append(product_branch)

    # shove the leaves into the bottom level of the hierarchy
    for line in cost_lines:
        data = {'name' : 'data',
                'content' : {
                    'usage_type' : line.usage_type,
                    'description' : line.item_description,
                    'usage_quantity' : line.usage_quantity,
                    'blended_rate' : Decimal(line.blended_rate),
                    'total_cost' : Decimal(line.total_cost),
                    },
                'datatype' : 'lineitem'}
        leaf = Leaf(**data)
        for tag_branch in root:
            acct = tag_branch.get_child_by_name(line.linked_account_name)
            if acct:
                if line.product_name == '':
                    product_name = 'Total'
                else:
                    product_name = line.product_name
                product = acct.get_child_by_name(product_name)
                setattr(leaf, 'parent', product)
                product.children.append(leaf)

    rendered = []
    for branch in root:
        rendered.extend(branch.dump(False))

    return {'data' : rendered, 'title' : 'AWS Cost Breakdown'}

@view_config(name='widget_openshift_stats',
             renderer='budget:templates/widgets/openshift_stats.pt')
def widget_openshift_stats(request):
    ''' show openshift deployment stats '''
    node_count, = DBSession.query(func.count(Openshift3Node.id)).one()
    cluster_count, = DBSession.query(func.count(\
                                     distinct(\
                                     Openshift3Node.cluster_id))).one()
    top_projects = DBSession.query(Openshift3Project.cluster_id,
                                   func.count(Openshift3Project.id)
                                  ).order_by(desc(\
                                            func.count(Openshift3Project.id)
                                                 )).group_by(\
                                                Openshift3Project.cluster_id
                                                            ).limit(5)
    top_users = DBSession.query(Openshift3User.cluster_id,
                                func.count(Openshift3User.id)
                               ).order_by(desc(\
                                            func.count(Openshift3User.id)
                                              )).group_by(\
                                                    Openshift3User.cluster_id
                                                         ).limit(5)
    data = collections.OrderedDict(sorted(\
                   {'Cluster Count' : {'Total':cluster_count},
                    'Node Count'    : {'Total':node_count},
                    'Top Project Counts' : collections.OrderedDict(sorted(\
                                    {k:v for k, v in top_projects}.items(),
                                    key=lambda x: x[1],
                                    reverse=True)),
                    'Top User Counts'    : collections.OrderedDict(sorted(\
                                    {k:v for k, v in top_users}.items(),
                                    key=lambda x: x[1],
                                    reverse=True)),
                    'Node Type'     : openshift3_nodes_by_type(),
                    'Node Status'   : openshift3_nodes_by_status(),
                    'Pod Status'    : openshift3_pods_by_status(),
                    # Not sure we care...
                    #'Container Status' : openshift3_containers_by_status(),
                   }.items()))
    LOG.debug(data)
    return {'title':'OpenShift v3 Stats', 'data':data}

def openshift3_nodes_by_type():
    ''' displays openshift3 node stats by type '''
    #FIXME: won't scale
    nodes = DBSession.query(Openshift3Node.meta).all()
    stats = {'unknown':0}
    for node_meta, in nodes:
        meta = yaml.safe_load(node_meta)
        try:
            kind = meta['labels']['type']
            if kind in stats.keys():
                stats[kind] += 1
            else:
                stats[kind] = 1
        except KeyError:
            LOG.error("Unknown node: %s", meta)
            stats['unknown'] += 1
    return collections.OrderedDict(sorted(stats.items()))

def openshift3_nodes_by_status():
    ''' displays openshift3 node stats by status '''
    #FIXME: won't scale
    nodes = DBSession.query(Openshift3Node.status).all()
    stats = {}
    for node_status, in nodes:
        status = yaml.safe_load(node_status)
        for condition in status['conditions']:
            status = condition['type']+': '+condition['status']
            if status in stats.keys():
                stats[status] += 1
            else:
                stats[status] = 1
    return collections.OrderedDict(sorted(stats.items()))

def openshift3_pods_by_status():
    ''' displays openshift3 pod stats by status '''
    #FIXME: won't scale
    pods = DBSession.query(Openshift3Pod.status).all()
    stats = {}
    for pod_status, in pods:
        status = yaml.safe_load(pod_status)
        if 'conditions' in status:
            for condition in status['conditions']:
                status = condition['type']+': '+condition['status']
                addset(stats, status, 1)
        else:
            addset(stats, 'Phase: '+status['phase'], 1)
    return collections.OrderedDict(sorted(stats.items()))

def openshift3_containers_by_status():
    ''' displays openshift3 pod stats by status '''
    #FIXME: won't scale
    pods = DBSession.query(Openshift3Pod.status).all()
    stats = {}
    for pod_status, in pods:
        status = yaml.safe_load(pod_status)
        if 'containerStatuses' in status:
            for container_status in status['containerStatuses']:
                # State should always be a single state, despite it being a dict
                if len(container_status['state'].keys()) == 1:
                    for state in container_status['state'].keys():
                        addset(stats, state, 1)
                else:
                    LOG.error('Found more than one state for containerID: %s',
                              container_status['containerID'])
        else:
            addset(stats, 'Phase: '+status['phase'], 1)
    return collections.OrderedDict(sorted(stats.items()))
