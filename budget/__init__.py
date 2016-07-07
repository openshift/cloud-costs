from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    # pyramid_chameleon's configuration
    config.include('pyramid_chameleon')

    # pyramid_formalchemy's configuration
    config.include('pyramid_formalchemy')

    # Add fanstatic tween
    config.include('pyramid_fanstatic')

    # Adding the jquery libraries
    config.include('fa.jquery')

    # register an admin UI
    config.formalchemy_admin('admin', package='budget',
            view='fa.jquery.pyramid.ModelView')

    # register static assets
    config.add_static_view('static', 'static', cache_max_age=3601)

    # all other routes...
    config.add_route('root', '/')
    config.add_route('stats', '/stats/{graph}')
    config.add_route('stats_index', '/stats')
    config.add_route('myview', '/myview')
    config.add_route('reservation', '/reservation/{loc}')
    config.add_route('cost_allocation', '/cost_allocation/{type}')

    config.scan()
    return config.make_wsgi_app()
