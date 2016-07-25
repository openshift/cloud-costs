from datetime import datetime, timedelta
from decimal import Decimal, getcontext

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import not_, asc, distinct, func

from ..models import *
from ..util.addset import addset

import locale
import logging

from budget.util.nvd3js import *

log = logging.getLogger(__name__)
last_year = datetime.now() - timedelta(days=365)
last_month = datetime.now() - timedelta(days=30)
locale.setlocale(locale.LC_ALL, "en_US")

@view_config(route_name='stats_index', renderer='budget:templates/stats.pt')
def stats_index(request):
    return { 'graph' : None, 'selectors': {}, 'notes': '' }

@view_config(route_name='stats', match_param="graph=account", renderer='budget:templates/stats.pt')
def cost_by_account(request):
    log.debug(request.params)

    data = DBSession.query(
                AwsInvoiceLineItem.linked_account_id,
                AwsAccountMetadata.account_name,
                AwsInvoiceLineItem.blended_cost,
                AwsInvoiceLineItem.usage_start_date,
            ).filter(
                AwsInvoiceLineItem.linked_account_id != None,
                AwsInvoiceLineItem.linked_account_id == AwsAccountMetadata.account_id,
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
                width=800,
                height=800,
                labelType='percent',
                labelThreshold=0.05,
                legendPosition='right')
    graph.data = graph_data

    return { 'graph' : graph,
             'selectors' : {
                    'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    }
                },
             'notes' : ''
            }

@view_config(route_name='stats', match_param="graph=activity", renderer='budget:templates/stats.pt')
def gear_activity_distribution(request):
    log.debug(request.params)

    dates = DBSession.query(
                OpenshiftProfileStats.collection_date.distinct()
            ).filter(
                OpenshiftProfileStats.collection_date >= last_year,
            ).all()
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

    log.debug(stats)

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

    log.debug(graph_data)
    graph = PieChart(
                width=800,
                height=800,
                labelType='percent',
                labelThreshold=0.02,
                legendPosition='right')
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
                },
             'notes' : ''
            }

@view_config(route_name='stats', match_param="graph=nodes", renderer='budget:templates/stats.pt')
def node_distribution(request):
    log.debug(request.params)

    dates = DBSession.query(
                OpenshiftProfileStats.collection_date.distinct()
            ).filter(
                OpenshiftProfileStats.collection_date >= last_year,
            ).all()
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
                width=800,
                height=800,
                labelType='percent',
                labelThreshold=0.03,
                legendPosition='right')
    graph.data = graph_data

    return { 'graph' : graph,
             'selectors' : {
                    'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    }
                },
             'notes' : ''
            }

@view_config(route_name='stats', match_param="graph=v2gearcost", renderer='budget:templates/stats.pt')
def v2_gear_cost(request):
    log.debug(request.params)

    notes = "This does not factor in amortized RI costs (yet)."

    # TODO: move this to a yaml file
    v2_account_list = [
            '359618769746',
            '650808968249',
            '670906860104',
            '843635060166',
            '581437147696',
            '497942437747',
            '045668658042',
            '884652610271',
            '922711891673'
    ]

    # Set precision of Decimal objects
    getcontext().prec = 4

    #TODO: have this be the intersection of dates in profile stats and invoice stats
    dates = DBSession.query(
                OpenshiftProfileStats.collection_date.distinct()
            ).filter(
                OpenshiftProfileStats.collection_date >= last_year,
            ).all()
    dates = sorted(set([ item[0] for item in dates ]))

    log.debug(dates)

    if 'date' in request.params:
        selected_date = datetime.strptime(request.params['date'], "%Y-%m-%d %H:%M:%S")
    else:
        selected_date = max(dates)

    if 'type' in request.params:
        gear_type = str(request.params['type'])
    else:
        gear_type = 'total'

    stats = DBSession.query(
                    OpenshiftProfileStats.gears_active_count,
                    OpenshiftProfileStats.gears_total_count,
                    OpenshiftProfileStats.nodes_count,
                    OpenshiftProfileStats.profile_name
            ).filter(
                    OpenshiftProfileStats.collection_date == selected_date,
            ).all()

    log.debug(stats)

    # TODO: replace with AwsCostAllocation query
    invoice_date = selected_date.replace(day=1,hour=0,minute=0,second=0)
    invoices = DBSession.query(
                AwsCostAllocation.linked_account_id,
                AwsCostAllocation.total_cost,
                AwsCostAllocation.usage_start_date,
            ).filter(
                AwsCostAllocation.linked_account_id != None,
                AwsCostAllocation.linked_account_id.in_(v2_account_list),
                AwsCostAllocation.usage_start_date == invoice_date,
                AwsCostAllocation.record_type == 'LinkedLineItem',
                not_(AwsCostAllocation.item_description.like('%Sign up charge for subscription:%'))
            ).all()

    log.debug(invoices)

    graph_data = []

    total_v2_cost = Decimal(0)
    for invoice in invoices:
        log.debug(invoice)
        total_v2_cost += Decimal(invoice.total_cost)

    log.debug("Total Cost: %f" % total_v2_cost)

    total_gears = { 'total' : Decimal(0),
                    'active': Decimal(0),
                    'nodes' : Decimal(0) }
    total_per_account = {'total' : {}, 'active': {}, 'nodes': {}}

    for stat in stats:
        total_gears['total'] += Decimal(stat.gears_total_count)
        total_gears['active'] += Decimal(stat.gears_active_count)
        total_gears['nodes'] += Decimal(stat.nodes_count)

        if stat.profile_name in total_per_account.keys():
            total_per_account['active'][stat.profile_name] += Decimal(stat.gears_active_count)
            total_per_account['total'][stat.profile_name] += Decimal(stat.gears_total_count)
            total_per_account['nodes'][stat.profile_name] += Decimal(stat.nodes_count)
        else:
            total_per_account['active'][stat.profile_name] = Decimal(stat.gears_active_count)
            total_per_account['total'][stat.profile_name] = Decimal(stat.gears_total_count)
            total_per_account['nodes'][stat.profile_name] = Decimal(stat.nodes_count)

    for stat in stats:
        node_proportion =  total_per_account['nodes'][stat.profile_name] / total_gears['nodes']
        value = (total_v2_cost * node_proportion) / total_per_account[gear_type][stat.profile_name]

        graph_data.append( { 'label' : stat.profile_name, 'value' : float(value)  })

    log.debug(graph_data)

    graph = DiscreteBarChart(
                width=900,
                height=600,
                staggerLabels='true'
            )
    graph.data = [{ 'key' : 'Costs Per Gear (%s)' % gear_type, 'values' : graph_data }]


    return { 'graph' : graph,
            'notes' : notes,
            'selectors' : {
                    'date' : {
                        'selected' : selected_date,
                        'list' : dates,
                    },
                    'type' : {
                        'selected' : gear_type,
                        'list' : ['active', 'total' ],
                    }
                }
            }

@view_config(route_name='stats', match_param="graph=totalcost", renderer='budget:templates/stats.pt')
def total_cost(request):
    log.debug(request.params)

    # { key : [values] }
    graph_data = []

    aws_costs = DBSession.query(
                AwsCostAllocation.billing_period_start_date,
                AwsCostAllocation.total_cost,
                AwsCostAllocation.credits,
            ).filter(
                AwsCostAllocation.record_type == 'InvoiceTotal',
                AwsCostAllocation.billing_period_start_date >= last_year,
            ).order_by(
                asc(AwsCostAllocation.billing_period_start_date)
            ).all()

    other_expenses = DBSession.query(ExpensedCost).filter(
                ExpensedCost.invoice_date >= last_year
            ).order_by(
                asc(ExpensedCost.invoice_date)
            ).all()

    # nvd3 requires an exactly equal number of data points for all data sets.
    # so, we need to ensure we at least set y-values to 0 where there is no
    # data point.
    seen_dates = []
    for cost in aws_costs:
        if cost.billing_period_start_date not in seen_dates:
            seen_dates.append(cost.billing_period_start_date)

    for cost in other_expenses:
        if cost.invoice_date not in seen_dates:
            seen_dates.append(cost.invoice_date)

    log.debug(seen_dates)
    # add up all invoiced costs for the month into a single total
    aws_dated_data = {}
    for cost in aws_costs:
        addset(aws_dated_data,cost.billing_period_start_date,cost.total_cost)
        addset(aws_dated_data,cost.billing_period_start_date,cost.credits)

    aws_data = []
    for day in seen_dates:
        flag = False
        for d in aws_dated_data:
            if d == day:
                aws_data.append({'x':d.strftime('%Y-%m-%d'),'y':aws_dated_data[d]})
                flag = True

        if not flag:
            aws_data.append({'x':day.strftime('%Y-%m-%d'),'y':0})

    graph_data.append({'key':'AWS','values':aws_data})

    vendors = DBSession.query(
                    distinct(ExpensedCost.vendor)
            ).filter(
                    ExpensedCost.invoice_date >= last_year
            ).all()
    vendors = [x[0] for x in vendors]

    other_data = []
    for vendor in vendors:
        vendor_data = []
        # ensure we have values for all dates
        for day in seen_dates:
            flag = False
            for cost in other_expenses:
                if cost.vendor == vendor and cost.invoice_date == day:
                    vendor_data.append({
                            'x' : cost.invoice_date.strftime('%Y-%m-%d'),
                            'y' : cost.amount
                    })
                    flag = True
            if not flag:
                vendor_data.append({'x':day.strftime('%Y-%m-%d'), 'y':0})
        graph_data.append({'key':vendor,'values':vendor_data})

    graph = MultiBarChart(
                width=1280,
                height=800,
                extra='chart.stacked(true);'
            )
    graph.data = graph_data

    return { 'graph' : graph,
            'notes' : '',
            'selectors' : {}
            }

# %s - undocumented pass-through to system's strftime.
#      need to multiply by 1000 to hit the right century.
def epoch_date(d):
    ''' return the unix epoch date for dates after Y2K '''
    return int(d.strftime('%s'))*1000

@view_config(route_name='stats', match_param="graph=gcpcost", renderer='budget:templates/stats.pt')
def gcp_cost(request):
    log.debug(request.params)

    # Numer of coords for all keys MUST be equal.
    # Coord values MUST be numbers (no strings!)
    #
    # [
    #    { 'key': label1, 'values': [[x1,y1],[x2,y2]] },
    #    { 'key': label2, 'values': [[x1,y1],[x2,y2]] },
    # ]
    graph_data = {}
    seen_dates = []
    projects = DBSession.query(GcpLineItem.project_name.distinct()).all()
    for p, in projects:
        project = str(p)

        if project not in graph_data.keys():
            graph_data[project] = []

        end_times = DBSession.query(
                        GcpLineItem.end_time.distinct()
                    ).filter(
                        GcpLineItem.project_name == project,
                        GcpLineItem.start_time >= last_year,
                    ).all()

        for end, in end_times:
            if end not in seen_dates:
                seen_dates.append(epoch_date(end))

            results = DBSession.query(func.sum(GcpLineItem.cost_amount)).filter(
                    GcpLineItem.project_name == project,
                    GcpLineItem.end_time == end,
                ).all()

            for r, in results:
                data = [epoch_date(end), r]
                graph_data[project].append(data)

    # remove spurious key.
    del(graph_data['None'])

    # ensure that the length of the coordinate value arrays are all the same.
    for k,v in graph_data.items():
        for d in seen_dates:
            if d not in [x for x,y in v]:
                graph_data[k].append([d,0])

    graph = StackedAreaChart(width=800,
                            height=600,
                            extra="""
    chart.xAxis.tickFormat(function(d) { return d3.time.format('%x')(new Date(d)) });
    chart.yAxis.tickFormat(d3.format('$,.4f'));
                                    """)
    graph.data = [{'key':k,'values':sorted(v, key=lambda x: x[0])} for k,v in graph_data.items()]

    return { 'graph' : graph,
            'notes' : '',
            'selectors' : {}
            }
