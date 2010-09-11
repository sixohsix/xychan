
from bottle import route, error, HTTPError, get, post
from bottle import view as _view

from .db import *

def view(tpl, **defaults):
    return _view("xychan/templates/" + tpl, **defaults)


@get('/')
def index():
    return "Go to the first board: <a href='/test/'>go there</a>."


@get('/favicon.ico')
def favicon():
    raise HTTPError(404)


@get('/setup')
def setup():
    with active_session as s:
        b = Board(short_name='test')
        s.add(b)
        s.add(Post(board=b, content="This is a post"))
    return dict()


@get('/:board_name')
@get('/:board_name/')
@view('board.tpl')
def board(board_name):
    with active_session as s:
        board = s.query(Board).filter(Board.short_name == board_name).first()
        if not board:
            raise HTTPError(404, "No such board.")
        posts = (s.query(Post)
                 .filter(Post.board == board).all())
        return dict(board=board, posts=posts)


@error(404)
def error404(msg):
    return "well, shit."
