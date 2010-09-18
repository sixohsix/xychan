
from .util import *

COOKIE_KEY = 'asdf82jfooapAOOOOOaf'
COOKIE_SECRET = 'nasdf423jndsfAJAfa'

class AuthCookie(object):
    def __init__(self, user_id):
        self.user_id = user_id

    @property
    def user(self):
        return s.query(User).filter(User.id == self.user_id).first()


@get('/login', name='login')
@view('login.tpl')
def login():
    return dict()


@post('/log_me_in_please', name='login_submit')
@view('message.tpl')
def login_submit():
    user = (s.query(User).filter(User.username == request.POST.get('username'))
            .first())
    if (not user) or (not user.verify_password(request.POST.get('password'))):
        return dict(message="Nope, that's not it", redirect=url('login'))
    else:
        response.set_cookie(COOKIE_KEY, AuthCookie(user.id), COOKIE_SECRET)
        return dict(message="You are now logged in", redirect=url('index'))


@post('/log_me_out_please', name='logout_submit')
@view('message.tpl')
def logout_submit():
    response.set_cookie(COOKIE_KEY, '')
    return dict(message="Seeya later", redirect=url('index'))


