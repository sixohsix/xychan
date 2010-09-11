
from bottle import default_app
from paste.fixture import TestApp

from xychan import *

app = TestApp(default_app())

def test_home():
    r = app.get('/')
