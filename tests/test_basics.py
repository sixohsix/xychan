
from bottle import debug
from paste.fixture import TestApp

from xychan import app
from xychan.db import configure_db

debug(True)
configure_db('sqlite:///:memory:', echo=True)

app = TestApp(app)


def test_home():
    r = app.get('/')


def test_post_to_board():
    app.get('/setup')
    r = app.post('/test/post', params=dict(
            content="Test post 2242"))
    r = app.get('/test/')
    assert "Test post 2242" in r
