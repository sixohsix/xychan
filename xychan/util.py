
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


from .image_store import *
from .db import *
from .cookies import *

__builtins__['url'] = url
