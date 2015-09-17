from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import DBSession

@view_config(route_name='root', renderer='budget:templates/root.pt')
def root(request):
    return {}
