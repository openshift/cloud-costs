from datetime import datetime, timedelta

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import *
from ..util.nvd3js.charts.piechart import PieChart
from ..util.nvd3js.charts.discretebar import DiscreteBarChart

import logging

log = logging.getLogger(__name__)

@view_config(route_name='stats', match_param='graph=default', renderer='budget:templates/stats.pt')
def stats(request):
    graph = PieChart()
    graph.data = [ {'label':'foo', 'value':5.0 }, {'label':'bar', 'value':3.0 }]
    return { 'graph' : graph }

@view_config(route_name='stats', match_param="graph=account", renderer='budget:templates/stats.pt')
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

    graph_data = []
    for item in data:
        if item[3] == selected_date:
            graph_data.append({'label': item[1], 'value': item[2]})

    graph = PieChart(
                width=400,
                height=400,
                label_type='percent',
                label_threshold=0.05,
                legend_position='right')
    graph.data = graph_data

    return { 'graph' : graph,
             'selectors' : {
                    'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    }
                }
            }

@view_config(route_name='stats', match_param="graph=activity", renderer='budget:templates/stats.pt')
def gear_activity_distribution(request):
    log.debug(request.params)

    dates = DBSession.query(OpenshiftProfileStats.collection_date.distinct()).all()
    dates = sorted(set([ item[0] for item in dates ]))

    if 'date' in request.params:
        selected_date = datetime.strptime(request.params['date'], "%Y-%m-%d %H:%M:%S")
    else:
        selected_date = max(dates)

    profiles = DBSession.query(OpenshiftProfileStats.profile_name.distinct()).all()
    profiles = sorted(set([ item[0] for item in profiles ]))

    if 'profile' in request.params:
        #XXX: security flaw?
        selected_profile = request.params['profile']
    else:
        selected_profile = profiles[0]

    stats = DBSession.query(
                    OpenshiftProfileStats.gears_active_count,
                    OpenshiftProfileStats.gears_idle_count,
                    OpenshiftProfileStats.gears_stopped_count,
                    OpenshiftProfileStats.gears_unknown_count
            ).filter(
                    OpenshiftProfileStats.collection_date == selected_date,
                    OpenshiftProfileStats.profile_name == selected_profile
            ).all()

    graph_data = []
    for stat in stats:
        graph_data.append({ 'label' : 'Active Gears',
                            'value' : int(stat.gears_active_count) })
        graph_data.append({ 'label' : 'Idle Gears',
                            'value' : int(stat.gears_idle_count) })
        graph_data.append({ 'label' : 'Stopped Gears',
                            'value' : int(stat.gears_stopped_count) })
        graph_data.append({ 'label' : 'Unknown Gears',
                            'value' : int(stat.gears_unknown_count) })

    graph = PieChart(
                width=400,
                height=400,
                label_type='percent',
                label_threshold=0.02,
                legend_position='right')
    graph.data = graph_data

    return { 'graph' : graph,
             'selectors' : {
                    'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    },
                    'profile' : {
                        'selected' : selected_profile,
                        'list' : profiles,
                    }
                }
            }

@view_config(route_name='stats', match_param="graph=nodes", renderer='budget:templates/stats.pt')
def node_distribution(request):
    log.debug(request.params)

    dates = DBSession.query(OpenshiftProfileStats.collection_date.distinct()).all()
    dates = sorted(set([ item[0] for item in dates ]))

    if 'date' in request.params:
        selected_date = datetime.strptime(request.params['date'], "%Y-%m-%d %H:%M:%S")
    else:
        selected_date = max(dates)

    stats = DBSession.query(
                    OpenshiftProfileStats.profile_name,
                    OpenshiftProfileStats.nodes_count,
            ).filter(
                    OpenshiftProfileStats.collection_date == selected_date,
            ).all()

    graph_data = []
    for stat in stats:
        graph_data.append({ 'label' : stat.profile_name,
                            'value' : int(stat.nodes_count) })

    graph = PieChart(
                width=400,
                height=400,
                label_type='percent',
                label_threshold=0.03,
                legend_position='right')
    graph.data = graph_data

    return { 'graph' : graph,
             'selectors' : {
                    'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    }
                }
            }
