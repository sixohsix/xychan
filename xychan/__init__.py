
from bottle import TEMPLATE_PATH, default_app
TEMPLATE_PATH.insert(0, './xychan/templates')

from .basics import *
from .db import DbSessionMiddleware

app = DbSessionMiddleware(default_app())

__all__ = ['app']
