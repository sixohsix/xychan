
from bottle import run, debug

from xychan import app

debug(True)
run(app, reloader=True)
