
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


from . import STATIC_PATH

__builtins__['url'] = url
