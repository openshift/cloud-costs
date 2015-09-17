from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import DBSession
from ..util.nvd3js.charts.piechart import PieChart

@view_config(route_name='stats', renderer='budget:templates/stats.pt')
def stats(request):
    graph = PieChart()
    graph.data = [ {'label':'foo', 'value':5.0 }, {'label':'bar', 'value':3.0 }]
    return { 'graph' : graph }
