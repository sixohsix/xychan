
from bottle import TEMPLATE_PATH, default_app, request, cookie_is_encoded
TEMPLATE_PATH.insert(0, './xychan/templates')

from .basics import *
from .db import DbSessionMiddleware


class Context(object):

    @property
    def user(self):
        auth_cookie = None
        if cookie_is_encoded(request.COOKIES.get(COOKIE_KEY, '')):
            auth_cookie = request.get_cookie(COOKIE_KEY, COOKIE_SECRET)
            return auth_cookie.user
        else:
            return None


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

__all__ = ['app']
