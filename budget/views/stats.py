from datetime import datetime, timedelta

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import *
from ..util.nvd3js.charts.piechart import PieChart

import logging

log = logging.getLogger(__name__)

@view_config(route_name='stats', match_param='graph=default', renderer='budget:templates/stats.pt')
def stats(request):
    graph = PieChart()
    graph.data = [ {'label':'foo', 'value':5.0 }, {'label':'bar', 'value':3.0 }]
    return { 'graph' : graph }

@view_config(route_name='stats', match_param="graph=acct", renderer='budget:templates/stats.pt')
def cost_by_account(request):
    log.debug(request.params)

    last_year = datetime.now() - timedelta(days=365)
    data = DBSession.query(
                AwsInvoiceLineItem.linked_account_id,
                AwsLinkedAccountId.account_name,
                AwsInvoiceLineItem.blended_cost,
                AwsInvoiceLineItem.usage_start_date,
            ).filter(
                AwsInvoiceLineItem.linked_account_id != None,
                AwsInvoiceLineItem.linked_account_id == AwsLinkedAccountId.linked_account_id,
                AwsInvoiceLineItem.usage_start_date >= last_year,
            ).all()

    dates = sorted(set([ item[3] for item in data ]))
    if 'date' in request.params:
        selected_date = datetime.strptime(request.params['date'], "%Y-%m-%d %H:%M:%S")
    else:
        selected_date = max(dates)
    log.debug("selected: " + str(selected_date))

    graph_data = []
    for item in data:
        if item[3] == selected_date:
            log.debug("selected: " + str(item))
            graph_data.append({'label': item[1], 'value': item[2]})

    graph = PieChart(
                width=400,
                height=400,
                label_type='percent',
                label_threshold=0.05,
                legend_position='right')
    graph.data = graph_data

    return { 'graph' : graph, 'dates' : dates, 'selected_date' : selected_date }

@view_config(route_name='stats', match_param="graph=activity", renderer='budget:templates/stats.pt')
def gear_activity_distribution(request):
    log.debug(request.params)

    dates = DBSession.query(OpenshiftProfileStats.collection_date.distinct()).all()
    dates = sorted(set([ item[0] for item in dates ]))

    log.debug("dates: " + str(dates))

    if 'date' in request.params:
        selected_date = datetime.strptime(request.params['date'], "%Y-%m-%d %H:%M:%S")
    else:
        selected_date = max(dates)
    log.debug("selected: " + str(selected_date))

    graph = None
    return { 'graph' : graph, 'dates' : dates, 'selected_date' : selected_date }
