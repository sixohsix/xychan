
from bottle import (
    route, error, HTTPError, get, post, request, response, view
    )

from .base62 import *

def random_key():
    from random import randint
    return randint(0, 2**160)

from .image_store import *
from .db import *
