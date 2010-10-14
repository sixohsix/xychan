
from __future__ import with_statement

from bottle import debug
from webtest import TestApp

from xychan import app
from xychan.db import configure_db, Post, Thread, Board, active_session, User

debug(True)
configure_db('sqlite:///:memory:', echo=False)

app = TestApp(app)

def setUp():
    with active_session:
        s.query(Post).delete()
        s.query(Thread).delete()
        s.query(Board).delete()
        s.query(User).delete()

        b = Board(short_name='test', long_name='Test Board')
        s.add(b)
        t = Thread(board=b)
        s.add(t)
        s.add(Post(
                thread=t, content="This is a post", poster_ip='1.2.3.4',
                poster_name="poster_name", subject="subject"))
        u = User(username='admin')
        u.password = 'adminadmin1'
        s.add(u)


def test_home():
    r = app.get('/')


def test_post_to_board():
    r = app.post('/test/post', params=dict(
            content="Test post 2242"))
    r = app.get('/test/')
    assert "Test post 2242" in r


def test_no_blank_post():
    r = app.post('/test/post', params=dict(
            content=""))
    assert "No, you must" in r


def test_visit_board():
    r = app.get('/test/')
    assert "This is a post" in r
    r = app.get('/test')
    assert "This is a post" in r


def test_visit_thread():
    r = app.get('/test/1/')
    assert "This is a post" in r
    r = app.get('/test/1')
    assert "This is a post" in r


def test_post_reply():
    r = app.get('/test/1/')
    f = r.forms[0]
    f['content'] = 'Some reply'
    f['subject'] = 'My subject'
    r = f.submit()
    r = app.get('/test/')
    assert "Some reply" in r
    assert "My subject" in r


def test_thread_order():
    setUp()
    r = app.post('/test/post', params=dict(
            content="Test post NEW"))
    r = app.get('/test')
    assert r.body.index("Test post NEW") < r.body.index("This is a post")


def test_post_list():
    app.post('/test/post', params=dict(
            content="Test post OP"))
    for x in range(10):
        app.post('/test/1/post', params=dict(
                content="Test post #" + str(x)))
    r = app.get('/test')
    assert "Test post OP" in r
    assert "Test post #3" not in r
    assert "Test post #9" in r

