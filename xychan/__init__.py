
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
