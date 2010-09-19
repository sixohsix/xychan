"""
xychan - a simple Python message board system
Copyright (C) 2010 Mike Verdone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Running xychan
--------------

::

    from xychan import app
    app.configure_db("sqlite:///database.db")
    app.configure_image_dir("path/to/image_dir")

"app" is the xychan WSGI app which you can run through pretty much any
WSGI server. The simplest is CGI::

    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)

Check out the file ``xychan.dh.cgi`` for a working CGI script, and
``xychan.dh.passenger`` for a Passenger WSGI deployment.

"""

from bottle import TEMPLATE_PATH, default_app, request, cookie_is_encoded
import os

STATIC_PATH = __path__[0] + os.sep + 'static'

TEMPLATE_PATH.insert(0, __path__[0] + os.sep + 'templates')

from .basics import *
from .db import DbSessionMiddleware, configure_db
from .image_store import configure_image_dir
from .cookies import *


class Context(object):

    def _fetch_cookie(self, cookie_def):
        cookie = None
        if cookie_is_encoded(request.COOKIES.get(cookie_def.cookie_key, '')):
            cookie = request.get_cookie(
                cookie_def.cookie_key,
                cookie_def.cookie_secret)
        return cookie

    @property
    def user(self):
        auth_cookie = self._fetch_cookie(AuthCookie)
        if auth_cookie:
            return auth_cookie.user
        else:
            return None

    @property
    def visitor_prefs(self):
        cookie = self._fetch_cookie(VisitorPrefsCookie)
        if cookie:
            return cookie.visitor_prefs


def context_middleware(wrapped_app):
    def _context_middleware(environ, start_response):
        __builtins__['c'] = Context()
        try:
            return wrapped_app(environ, start_response)
        finally:
            del __builtins__['c']
    return _context_middleware


app = context_middleware(
    DbSessionMiddleware(
        default_app()))
app.configure_image_dir = configure_image_dir
app.configure_db = configure_db

__all__ = ['app']
