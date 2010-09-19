
from bottle import response
from .db import VisitorPrefs, User


class AuthCookie(object):

    cookie_key = 'asdf82jfooapAOOOOOaf'
    cookie_secret = 'nasdf423jndsfAJAfa'

    def __init__(self, user_id):
        self.user_id = user_id

    @property
    def user(self):
        return s.query(User).filter(User.id == self.user_id).first()


class VisitorPrefsCookie(object):

    cookie_key = 'jkasdfa99a9a9'
    cookie_secret = 'nakNJKNJANoi*8f**'

    def __init__(self, cookie_uuid):
        self.cookie_uuid = cookie_uuid

    @property
    def visitor_prefs(self):
        return (s.query(VisitorPrefs)
                .filter(VisitorPrefs.cookie_uuid == self.cookie_uuid).first())


def set_cookie(cookie):
    response.set_cookie(cookie.cookie_key, cookie, cookie.cookie_secret)


def wipe_cookie(cookie):
    response.set_cookie(cookie.cookie_key, "")
