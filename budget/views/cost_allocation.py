from datetime import datetime, timedelta
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import not_, asc

from ..models import *
from ..util.addset import addset

import locale
import logging

log = logging.getLogger(__name__)
last_year = datetime.now() - timedelta(days=365)

locale.setlocale(locale.LC_ALL, "en_US")

@view_config(route_name='cost_allocation', match_param='type=by_account', renderer='budget:templates/cost_allocation.pt')
def cost_allocation_by_account(request):
    log.debug(request.params)

    dates = DBSession.query(
                AwsCostAllocation.usage_start_date.distinct()
            ).filter(
                OpenshiftProfileStats.collection_date >= last_year,
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
                AwsCostAllocation.usage_start_date == selected_date
            ).order_by(
                asc(AwsCostAllocation.usage_type)
            ).all()

    data = {}
    totals = {}

    for line in cost_lines:
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

        if line.linked_account_name == '':
            account_name = "Total"
        else:
            account_name = "%s [%s]" % (line.linked_account_name, line.linked_account_id)

        if line.product_name == '':
            product_name = "Sub-Total"
        else:
            product_name = line.product_name

        if account_name not in data.keys():
            data[account_name] = {}

        if account_name not in totals:
            totals[account_name] = {}

        if account_name != "Total" and product_name != "Sub-Total":
            addset(totals[account_name], product_name, line.total_cost)

        if account_name != "Total" and product_name == "Sub-Total":
            totals[account_name]['account_total'] = line.total_cost,
        else:
            addset(data[account_name], product_name, datum)

    for account in totals:
        for product in totals[account]:
            totals[account][product] = locale.format("%.2f",
                                                    totals[account][product],
                                                    grouping=True)

    # munge selected_date to avoid presenting "dd/mm/yy 00:00:00" in the UI
    if not isinstance(selected_date, str):
        selected_date = selected_date.strftime("%Y-%m-%d"),

    return { 'data' : data,
            'totals' : totals,
            'selectors' : {
                'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    }
                }
            }
