
from bottle import (
    route, error, HTTPError, get, post, request, response, view
    )

from .base62 import *

def random_key():
    from random import randint
    return randint(0, 2**160)

def cache_forever(func):
    def _cache_forever(*args, **kwargs):
        response.headers['Expires'] = 'Sun, 17-Jan-2038 19:14:07 GMT'
        response.headers['Cache-control'] = 'public'
        return func(*args, **kwargs)
    return _cache_forever

from .image_store import *
from .db import *
