
import os
from datetime import datetime, timedelta

from bottle import (
    route, error, HTTPError, get, post, request, response, view, url,
    cookie_is_encoded, template, HTTPResponse,
    )

from base62 import *
from image_store import *
from db import *
from cookies import *

def cache_forever(func):
    def _cache_forever(*args, **kwargs):
        response.headers['Expires'] = 'Sun, 17-Jan-2038 19:14:07 GMT'
        response.headers['Cache-control'] = 'public'
        return func(*args, **kwargs)
    return _cache_forever


def admin_only(func):
    def _admin_only(*args, **kwargs):
        if not c.user:
            raise HTTPError(302, 'Found', header=[('Location', url('login'))])
        return func(*args, **kwargs)
    return _admin_only


def get_uni(key):
    return request.forms.get(key, '').decode('utf8')


def assert_not_banned(board):
    ip_addr = request.get('REMOTE_ADDR', '0.0.0.0')
    if IpBan.ip_is_banned(ip_addr):
        raise HTTPResponse(
            template(
                'message.tpl', message="You are banned",
                redirect=url('board', board_name=board.short_name)),
            status=403)


def assert_not_locked(board):
    if board.locked:
        raise HTTPResponse(
            template(
                'message.tpl', message="This board is locked",
                redirect=url('board', board_name=board.short_name)),
            status=403)


def get_board_or_die(s, board_name):
    board = s.query(Board).filter(Board.short_name == board_name).first()
    if not board:
        raise HTTPError(404, "No such board.")
    return board


def get_thread_in_board_or_die(s, board, thread_id):
    thread = (s.query(Thread)
              .filter(Thread.id == thread_id)
              .filter(Thread.board == board)
              .first())
    if not thread:
        raise HTTPError(404, "No such thread.")
    return thread



from . import STATIC_PATH

def rurl(*args, **kwargs):
    return ''.join(['http://', c.server_name, url(*args, **kwargs)])

__builtins__['url'] = url
__builtins__['rurl'] = rurl
