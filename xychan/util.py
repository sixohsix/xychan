
from bottle import route, error, HTTPError, get, post, request, response
from bottle import view as _view


def view(tpl, **defaults):
    return _view("xychan/templates/" + tpl, **defaults)


__all__ = [name for name in locals().keys() if not name.startswith('_')]
