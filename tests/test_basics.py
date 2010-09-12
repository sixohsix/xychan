
from bottle import default_app, debug
from paste.fixture import TestApp

from xychan import *

debug(True)

app = TestApp(default_app())


def test_home():
    r = app.get('/')


def test_post_to_board():
    app.get('/setup')
    r = app.post('/test/post', params=dict(
            content="Test post 2242"))
    r = app.get('/test')
    assert "Test post 2242" in r
