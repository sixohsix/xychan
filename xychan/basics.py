
from bottle import route, error, HTTPError

from .db import *

@route('/')
def index():
    return "Go to the first board: <a href='/test/'>go there</a>."


@route('/favicon.ico')
def favicon():
    raise HTTPError(404)


@route('/setup')
def setup():
    with active_session as s:
        b = Board(short_name='test')
        s.add(b)
        s.add(Post(board=b, content="This is a post"))


@route('/:board_name')
@route('/:board_name/')
def board(board_name):
    with active_session as s:
        board = s.query(Board).filter(Board.short_name == board_name).first()
        if not board:
            raise HTTPError(404, "No such board.")

@error(404)
def error404(msg):
    return "well, shit."
