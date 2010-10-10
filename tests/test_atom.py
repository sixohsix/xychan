
from test_basics import app, setUp


def test_atom_feed_board():
    r = app.get('/test/atom-threads.xml')
    assert r
    assert r.header('Content-Type') == 'text/xml'


def test_atom_feed_thread():
    r = app.get('/test/1/atom.xml')
    assert r
    assert r.header('Content-Type') == 'text/xml'
