
import os

from bottle import (
    route, error, HTTPError, get, post, request, response, view, url,
    cookie_is_encoded,
    )

from .base62 import *


def cache_forever(func):
    def _cache_forever(*args, **kwargs):
        response.headers['Expires'] = 'Sun, 17-Jan-2038 19:14:07 GMT'
        response.headers['Cache-control'] = 'public'
        return func(*args, **kwargs)
    return _cache_forever


def admin_only(func):
    def _admin_only(*args, **kwargs):
        if not c.user:
            raise HTTPError(403, 'Forbidden')
        return func(*args, **kwargs)
    return _admin_only


def get_uni(key):
    return request.forms.get(key, '').decode('utf8')


from .image_store import *
from .db import *
from .cookies import *

from . import STATIC_PATH

__builtins__['url'] = url
