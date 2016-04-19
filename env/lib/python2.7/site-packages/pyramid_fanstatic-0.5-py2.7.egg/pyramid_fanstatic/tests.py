# -*- coding: utf-8 -*-

import unittest

from pyramid import testing
from webtest import TestApp
from js.jquery import jquery
import fanstatic


def home(request):
    resp = request.response
    resp.content_type = 'text/html'
    resp.body = '''\
<html>
<head>
</head>
<body>
</body>
</html>
'''
    jquery.need()
    return resp


class TestTween(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.include("pyramid_fanstatic")
        self.config.add_route('home', '/')
        self.config.add_view(route_name='home', view=home)
        self.app = TestApp(self.config.make_wsgi_app())

    def test_injector(self):
        resp = self.app.get('/')
        resp.mustcontain(('<script type="text/javascript" '
                          'src="/fanstatic/jquery/jquery.js"></script>'))

    def test_publisher(self):
        resp = self.app.get('/fanstatic/jquery/jquery.js')
        resp.mustcontain('window.jQuery = window.$ = jQuery;')

    def tearDown(self):
        testing.tearDown()


class TestCustomConfig(unittest.TestCase):

    _custom_config = {
            'fanstatic.publisher_signature': 'custom_sign',
    }

    def setUp(self):
        self.config = testing.setUp()
        self.config.registry.settings.update(self._custom_config)
        self.config.include("pyramid_fanstatic")
        self.config.add_route('home', '/')
        self.config.add_view(route_name='home', view=home)
        self.app = TestApp(self.config.make_wsgi_app())

    def tearDown(self):
        testing.tearDown()

class TestCustomConfigPublisherSignature(TestCustomConfig):

    def test_injector(self):
        resp = self.app.get('/')
        resp.mustcontain(('<script type="text/javascript" '
                          'src="/custom_sign/jquery/jquery.js"></script>'))

    def test_publisher(self):
        resp = self.app.get('/custom_sign/jquery/jquery.js')
        resp.mustcontain('window.jQuery = window.$ = jQuery;')

class TestCustomConfigUseApplicationUri(TestCustomConfig):
    """Test specifying use of application URI for Fanstatic resources.

    Application URI is generated from the environ for any given request,
    allowing resources to be served from URLs that aren't necessarily at the
    root of a given domain.
    """

    _custom_config = {
        'fanstatic.use_application_uri': 'true',
    }

    def setUp(self):
        """Set up and add dummy route to webtest application."""
        super(TestCustomConfigUseApplicationUri, self).setUp()
        self.config.add_route('dummy', '/subdir/page', view=home) #dummy route
        self.app = TestApp(self.config.make_wsgi_app())

    def test_base_url_is_set(self):
        """Ensure that Fanstatic has a base url set after a request."""
        resp = self.app.get('/')
        needed = resp.request.environ[fanstatic.NEEDED]
        self.assertTrue(needed.has_base_url())

    def test_base_url_complex(self):
        """Check resource URLs generated for a complex environ."""

        #http://example.com:8080/exampleapp/subdir/page?foo=bar
        environ = {
            'wsgi.url_scheme': 'https',
            'HTTP_HOST': 'example.com:8080',
            'SCRIPT_NAME': '/exampleapp',
            'PATH_INFO': '/subdir/page',
            'QUERY_STRING': 'foo=bar',
        }
        resp = self.app.get('/', extra_environ=environ)
        resp.mustcontain(('<script type="text/javascript" '
                          'src="https://example.com:8080/exampleapp/'
                          'fanstatic/jquery/jquery.js"></script>'))
        self.assertNotIn(environ['PATH_INFO'], resp.body)
        self.assertNotIn(environ['QUERY_STRING'], resp.body)

    def test_base_url_simple(self):
        """Check resource URLs generated for a simple environ."""

        #https://example.com/exampleapp/
        environ = {
            'wsgi.url_scheme': 'http',
            'HTTP_HOST': '',
            'SERVER_NAME': 'example.com',
            'SERVER_PORT': '80',
        }
        resp = self.app.get('/', extra_environ=environ)
        resp.mustcontain(('<script type="text/javascript" '
                          'src="http://example.com/'
                          'fanstatic/jquery/jquery.js"></script>'))
        self.assertNotIn(':%s' % environ['SERVER_PORT'], resp.body)

class TestCustomConfigUseApplicationUriPrecendence(TestCustomConfig):
    """Test precedence of use of application URI for Fanstatic resources.
    """

    _custom_config = {
        'fanstatic.use_application_uri': 'true',
        'fanstatic.base_url': 'https://example.com:1234/exampleapp',
    }

    def test_option_precendence(self):
        """Check resource URLs to ensure ``base_url`` takes precendence."""

        environ = {
            'wsgi.url_scheme': 'http',
            'HTTP_HOST': 'myexamplehost.com:80',
        }
        resp = self.app.get('/', extra_environ=environ)
        resp.mustcontain(('<script type="text/javascript" '
                          'src="https://example.com:1234/exampleapp/'
                          'fanstatic/jquery/jquery.js"></script>'))
        self.assertNotIn(environ['HTTP_HOST'], resp.body)

