
from bottle import run, debug

from xychan import app
from xychan.db import configure_db

debug(True)
configure_db('sqlite:///test.db', echo=True)

run(app, reloader=True)
