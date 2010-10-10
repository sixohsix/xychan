
from bottle import cookie_is_encoded, request
from cookies import *


class Context(object):

    threads_per_page = 10

    def __init__(self):
        self.visitor_prefs = None

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

    def _get_visitor_prefs(self):
        if not self._visitor_prefs:
            cookie = self._fetch_cookie(VisitorPrefsCookie)
            if cookie:
                self._visitor_prefs = cookie.visitor_prefs
        return self._visitor_prefs

    def _set_visitor_prefs(self, v):
        self._visitor_prefs = v

    visitor_prefs = property(_get_visitor_prefs, _set_visitor_prefs)

    @property
    def server_name(self):
        return request.environ['SERVER_NAME'] or 'localhost'


def context_middleware(wrapped_app):
    def _context_middleware(environ, start_response):
        __builtins__['c'] = Context()
        try:
            return wrapped_app(environ, start_response)
        finally:
            del __builtins__['c']
    return _context_middleware
