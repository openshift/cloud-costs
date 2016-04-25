from datetime import datetime, timedelta
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_, not_, asc

from ..models import *
from ..util.addset import addset
from ..util.nvd3js.charts.historicalbar import HistoricalBarChart
from ..util.nvd3js.charts.discretebar import DiscreteBarChart

import locale
import logging
import re

log = logging.getLogger(__name__)
last_year = datetime.now() - timedelta(days=365)

locale.setlocale(locale.LC_ALL, "en_US")

def get_metadata(account_id):
    try:
        results = DBSession.query(
                        AwsAccountMetadata.tags
                    ).filter(
                        AwsAccountMetadata.account_id == account_id
                    ).all();
        # generate a single, flattened list
        metadata = [r for tup in results for result in tup for r in result.split(',')]
    except NoResultFound:
        metadata = []
    return metadata

@view_config(route_name='cost_allocation', match_param='type=by_account', renderer='budget:templates/cost_allocation.pt')
def cost_allocation_by_account(request):
    log.debug(request.params)

    dates = DBSession.query(
                AwsCostAllocation.billing_period_start_date.distinct()
            ).filter(
                AwsCostAllocation.billing_period_start_date >= last_year,
            ).all()
    dates = sorted(set([ item[0].strftime("%Y-%m-%d") for item in dates ]))

    if 'date' in request.params:
        selected_date = datetime.strptime(request.params['date'], "%Y-%m-%d")
    else:
        selected_date = max(dates)

    cost_lines = DBSession.query(
                AwsCostAllocation.linked_account_name,
                AwsCostAllocation.linked_account_id,
                AwsCostAllocation.product_name,
                AwsCostAllocation.usage_type,
                AwsCostAllocation.item_description,
                AwsCostAllocation.usage_quantity,
                AwsCostAllocation.blended_rate,
                AwsCostAllocation.total_cost
            ).filter(
                AwsCostAllocation.billing_period_start_date == selected_date,
            ).order_by(
                asc(AwsCostAllocation.usage_type)
            ).all()

    data = {}
    totals = {}
    metadata = {}
    ri_total = {}

    for line in cost_lines:
        # set account_name
        if line.linked_account_name == '':
            account_name = "Total"
        else:
            account_name = "%s [%s]" % (line.linked_account_name, line.linked_account_id)

        # identify RI up-front fees
        if re.search(r'Sign up charge for subscription',
                line.item_description):
            addset(ri_total, account_name, line.total_cost)
            continue

        # build our basic table output
        datum = "".join([
                "<tr class='aws_lineitem_list'>",
                "<td class='aws_usage_type'>%s</td>" % line.usage_type,
                "<td class='aws_item_description'>%s</td>" % line.item_description,
                "<td class='aws_usage_quantity'>%s</td>" % locale.format("%.8f",
                                                                        line.usage_quantity,
                                                                        grouping=True).rstrip('0').rstrip('.'),
                "<td class='aws_blended_rate'>$%s</td>" % locale.format("%.3f",
                                                                        line.blended_rate,
                                                                        grouping=True).rstrip('0').rstrip('.'),
                "<td class='aws_total_cost'>$%.2f</td>" % Decimal(line.total_cost),
                "</tr>"])

        # fetch metadata
        if account_name not in metadata.keys():
            metadata[account_name] = get_metadata(line.linked_account_id)

        if line.product_name == '':
            product_name = "Sub-Total"
        else:
            product_name = line.product_name

        # init data structures
        if account_name not in data.keys():
            data[account_name] = {}

        if account_name not in totals:
            totals[account_name] = {}

        # populate data structures
        if account_name != "Total" and product_name != "Sub-Total":
            addset(totals[account_name], product_name, line.total_cost)

        if account_name != "Total" and product_name == "Sub-Total":
            totals[account_name]['account_total'] = line.total_cost
        else:
            addset(data[account_name], product_name, datum)

    # collect account totals
    for account in totals:
        # adjust sub-total to remove RI up-front fees.
        if account in totals and account in ri_total:
            totals[account]['account_total'] = totals[account]['account_total'] - ri_total[account]

        for product in totals[account]:
            totals[account][product] = locale.format("%.2f",
                                                    totals[account][product],
                                                    grouping=True)

    # munge selected_date to avoid presenting "dd/mm/yy 00:00:00" in the UI
    if not isinstance(selected_date, str):
        selected_date = selected_date.strftime("%Y-%m-%d")

    log.debug(ri_total)

    return { 'data' : data,
            'totals' : totals,
            'metadata' : metadata,
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

    caller = None
    selected_date = None

    if 'caller' in request.params:
        # extract linked account id.
        caller = request.params["caller"]
        account_id = request.params["caller"].split('-')[-1]

    if 'selected_date' in request.params:
        selected_date = datetime.strptime(request.params['selected_date'], "%Y-%m-%d")

    if not caller and not selected_date:
        return { 'data' : '<p>No graph to show</p>' }

    graph_data = []

    results = DBSession.query(
                AwsCostAllocation.total_cost,
                AwsCostAllocation.billing_period_start_date
            ).filter(
                AwsCostAllocation.linked_account_id == account_id,
                AwsCostAllocation.billing_period_start_date >= last_year,
                AwsCostAllocation.record_type == 'AccountTotal'
            ).order_by(
                asc(AwsCostAllocation.billing_period_start_date)
            ).all()

    for result in results:
        #graph_data.append("%.3f" % Decimal(result.total_cost))
        graph_data.append({ 'label': result.billing_period_start_date.strftime("%Y-%m-%d"), 'value': "%.3f" % Decimal(result.total_cost)})

    log.debug(graph_data)

    #graph = HistoricalBarChart()
    #graph.data = [{ 'key' : str(caller), 'values' : graph_data , 'color' : '#ffffff' }]

    # setting y_domain because the default calculation often misses the max value
    graph = DiscreteBarChart(
                y_domain=[0, max([r.total_cost for r in results])],
                show_xaxis='false'
            )
    graph.data = [{ 'key' : str(caller), 'values' : graph_data}]
    return { 'data' : graph }
