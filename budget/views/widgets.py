from datetime import datetime, timedelta
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config, render_view_to_response
from pyramid.events import subscriber, BeforeRender

from sqlalchemy.exc import DBAPIError
from sqlalchemy import not_, asc, distinct, func

from ..models import *
from ..util.addset import addset
from ..util.tree import Branch, Leaf
from ..util.queries.aws import get_dates, get_metadata

import locale
import logging

from budget.util.nvd3js import *

log = logging.getLogger(__name__)
last_year = datetime.now() - timedelta(days=365)
last_month = datetime.now() - timedelta(days=30)
locale.setlocale(locale.LC_ALL, "en_US")

# from:
# https://stackoverflow.com/questions/8063012/ajax-widgets-in-pyramid-and-chameleon
@subscriber(BeforeRender)
def add_render_view_global(event):
    log.debug(event)
    event['render_view'] = lambda name: render_view_to_response(event['context'],
                event['request'], name=name, secure=True).ubody

def epoch_date(d):
    ''' return the unix epoch date for dates after Y2K '''
    # %s - undocumented pass-through to system's strftime.
    #      need to multiply by 1000 to hit the right century.
    return int(d.strftime('%s'))*1000

@view_config(name='widget_gcp', renderer='budget:templates/widgets/graph.pt')
def widget_gcp(request):
    log.debug(request.params)

    graph_data = {}
    seen_dates = []
    projects = DBSession.query(GcpLineItem.project_name.distinct()).all()
    for p, in projects:
        project = str(p)

        if project not in graph_data.keys():
            graph_data[project] = []

        start_times = DBSession.query(
                        GcpLineItem.start_time.distinct()
                    ).filter(
                        GcpLineItem.project_name == project,
                        GcpLineItem.start_time >= last_month,
                    ).all()

        for start, in start_times:
            if start not in seen_dates:
                seen_dates.append(epoch_date(start))

            results = DBSession.query(func.sum(GcpLineItem.cost_amount)).filter(
                    GcpLineItem.project_name == project,
                    GcpLineItem.start_time == start,
                ).all()

            for r, in results:
                data = [epoch_date(start), r]
                graph_data[project].append(data)

    # remove spurious key.
    del(graph_data['None'])

    # ensure that the length of the coordinate value arrays are all the same.
    for k,v in graph_data.items():
        for d in seen_dates:
            if d not in [x for x,y in v]:
                graph_data[k].append([d,0])

    graph = StackedAreaChart(
            showLegend=False,
            useInteractiveGuideline=False,
            showControls=False,
            margin={'top': 10, 'right': 10, 'bottom': 60, 'left': 50},
            showXAxis=False,
            extra="""
    chart.xAxis.tickFormat(function(d) { return d3.time.format('%x')(new Date(d)) });
    chart.yAxis.tickFormat(d3.format('$,.2f'));
            """)
    graph.data = [{'key':k,'values':sorted(v, key=lambda x: x[0])} for k,v in graph_data.items()]

    return { 'graph' : graph, 'title' : 'GCP Costs' }

@view_config(name='widget_aws_cost', renderer='budget:templates/widgets/aws_cost.pt')
def widget_aws_cost(request):
    ''' Produce a hierarchy of cost-categories to provide a high-level summary
        of spending while enabling a user to drill-into the billing details.
    '''
    log.debug(request.params)

    dates, selected_date = get_dates(request.params)

    results = DBSession.query(
                AwsAccountMetadata.account_id,
                AwsAccountMetadata.account_name,
                AwsAccountMetadata.tags,
            ).all()

    # create objects of accounts and tags to build our hierarchy from
    accounts = {}
    tags = []
    for res in results:
        accounts[res.account_id] = {
                    'account_name' : res.account_name,
                    'tags' : res.tags.split(',') }
        for tag in res.tags.split(','):
            if tag not in tags:
                tags.append(tag)

    # distinct list of products
    products = DBSession.query(AwsCostAllocation.product_name.distinct()).all()

    # line items for the selected invoice
    cost_lines = DBSession.query(
                AwsCostAllocation.linked_account_id,
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
        for account in sorted(accounts, key=lambda x: accounts[x]['account_name']):
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
        data = {
                'name' : 'data',
                'content' : {
                    'usage_type' : line.usage_type,
                    'description' : line.item_description,
                    'usage_quantity' : line.usage_quantity,
                    'blended_rate' : Decimal(line.blended_rate),
                    'total_cost' : Decimal(line.total_cost),
                    },
                'datatype' : 'lineitem'
                }
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
    for x in root:
        rendered.extend(x.dump(False))

    return { 'data' : rendered, 'title' : 'AWS Cost Breakdown' }
