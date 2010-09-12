
from bottle import default_app
from paste.fixture import TestApp

from xychan import *

app = TestApp(default_app())


def test_home():
    r = app.get('/')


def test_post_to_board():
    app.get('/setup')
    r = app.post('/test/post', params=dict(
            content="This is the text."))
