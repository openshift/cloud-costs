from datetime import datetime, timedelta
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_, not_, asc

from ..models import *
from ..util.addset import addset
from ..util.tree import Branch, Leaf
from ..util.queries.aws import get_dates, get_metadata
from ..util.nvd3js import *

import locale
import logging
import re

log = logging.getLogger(__name__)
last_year = datetime.now() - timedelta(days=365)

locale.setlocale(locale.LC_ALL, "en_US")

@view_config(route_name='cost_allocation', match_param='type=by_account', renderer='budget:templates/cost_allocation.pt')
def cost_allocation_by_account(request):
    ''' Produce a hierarchy of cost-categories to provide a high-level summary
        of spending while enabling a user to drill into the billing details.
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

    # fetch a distinct list of AWS products
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

    print cost_lines
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

    #TODO: product totals

#                    # identify RI up-front fees
#                    # TODO: insert this into our hierarchy somewhere
#                    if re.search(r'Sign up charge for subscription',
#                            line.item_description):
#                        ri_total += line.total_cost
#                        continue
#
    #log.debug(ri_total)
    rendered = []
    for x in root:
        rendered.extend(x.dump())

    return { 'data' : rendered,
            'selectors' : {
                'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    }
                }
            }

@view_config(route_name='cost_allocation', match_param='type=graph', renderer='budget:templates/structure.pt')
def cost_allocation_graph(request):
    log.debug(request.params)

    account_name = None
    selected_date = None

    if request.params.get('caller', None):
        account_name = request.params["caller"]

    if request.params.get('selected_date', None):
        selected_date = datetime.strptime(request.params['selected_date'], "%Y-%m-%d")

    if not account_name and not selected_date:
        return { 'data' : '<p>No graph to show</p>' }

    graph_data = []

    results = DBSession.query(
                AwsCostAllocation.total_cost,
                AwsCostAllocation.billing_period_start_date
            ).filter(
                AwsCostAllocation.linked_account_name == account_name,
                AwsCostAllocation.billing_period_start_date >= last_year,
                AwsCostAllocation.record_type == 'AccountTotal'
            ).order_by(
                asc(AwsCostAllocation.billing_period_start_date)
            ).all()

    for result in results:
        #graph_data.append("%.3f" % Decimal(result.total_cost))
        graph_data.append({ 'label': result.billing_period_start_date.strftime("%Y-%m-%d"), 'value': "%.3f" % Decimal(result.total_cost)})

    log.debug(graph_data)

    # setting y_domain because the default calculation often misses the max value
    graph = DiscreteBarChart(
                yDomain=[0, max([r.total_cost for r in results])],
                showXAxis=False
            )
    graph.data = [{ 'key' : str(account_name), 'values' : graph_data}]
    return { 'data' : graph }
