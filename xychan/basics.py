
import re
import cgi
from uuid import uuid4

from .util import *

_link_line_re = re.compile(r"&gt;&gt; *([0-9]+) *")

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


def sanitize_content(s, content):
    lines = []
    for line in content.split('\n'):
        line = cgi.escape(line)
        m = _link_line_re.match(line)
        if m:
            post = s.query(Post).filter(Post.id == m.groups()[0]).first()
            if post:
                line = (u"<a href=\""
                        + url('thread', board_name=post.thread.board.short_name,
                              thread_id=post.thread.id)
                        + "#" + str(post.id) + "\">"
                        + line
                        + "</a>")
        lines.append(line)
    return '<br>\n'.join(lines)


PREFS_COOKIE_KEY = 'jkasdfa99a9a9'
PREFS_COOKIE_SECRET = 'nakNJKNJANoi*8f**'

class VisitorPrefsCookie(object):
    def __init__(self, cookie_uuid):
        self.cookie_uuid = cookie_uuid

    @property
    def visitor_prefs(self):
        return (s.query(VisitorPrefs)
                .filter(VisitorPrefs.cookie_uuid == self.cookie_uuid).first())


@get('/', name='index')
def index():
    return (
        "Go to the first board: <a href='"
        + url('board', board_name='test')
        + "'>go there</a>.")


@get('/favicon.ico', name='favicon')
@cache_forever
def favicon():
    response.content_type = "image/png"
    return open('./xychan/static/favicon.png').read()


@get('/style.css', name='style')
@cache_forever
def style():
    response.content_type = "text/css"
    return open('./xychan/static/style.css').read()


@get('/setup')
def create_a_board():
    with active_session as s:
        b = Board(short_name='test')
        s.add(b)
        t = Thread(board=b)
        s.add(t)
        s.add(Post(
                thread=t, content="This is a post", poster_ip='1.2.3.4',
                poster_name="poster_name", subject="subject"))
        u = User(username='admin')
        u.password = 'adminadmin1'
        s.add(u)
    return dict()


from .login import *

from .moderation import *


@get('/t_/:image', name='thumb')
@cache_forever
def get_thumbnail(image):
    thumb_data = fetch_thumb(image)
    response.content_type = 'image/' + image.split('.')[-1]
    return thumb_data


@get('/i_/:image', name='image')
@cache_forever
def get_image(image):
    image_data = fetch_image(image)
    response.content_type = 'image/' + image.split('.')[-1]
    return image_data


@get('/:board_name/', name='board')
@view('board.tpl')
def board(board_name):
    with active_session as s:
        board = get_board_or_die(s, board_name)
        threads = (s.query(Thread)
                   .filter(Thread.board == board)
                   .order_by(desc(Thread.last_post_time))
                   .all())
        threads = [thread for thread in  threads if thread.posts]
        return dict(board=board, threads=threads)


def remember_poster_name(poster_name):
    vp = c.visitor_prefs
    if not vp:
        vp = VisitorPrefs(cookie_uuid=str(uuid4()))
        s.add(vp)
        response.set_cookie(PREFS_COOKIE_KEY,
                            VisitorPrefsCookie(vp.cookie_uuid),
                            PREFS_COOKIE_SECRET)
    vp.poster_name = poster_name


@post('/:board_name/post', name="post_thread")
@view('post_successful.tpl')
def post_thread(board_name):
    with active_session as s:
        board = get_board_or_die(s, board_name)
        image_key = None
        img = request.files.get('image')
        if img is not None: # LOL WAT
            image_key = store_image(img.value)
        thread = Thread(board=board, last_post_time=func.now())
        s.add(thread)
        poster_name = request.POST.get('poster_name', '')
        s.add(Post(thread=thread,
                   content=sanitize_content(s, request.POST.get('content', '')),
                   poster_name=poster_name,
                   subject=request.POST.get('subject', ''),
                   poster_ip=request.get('REMOTE_ADDR', '0.0.0.0'),
                   image_key=image_key))
        remember_poster_name(poster_name)
        return dict(board=board)


@get('/:board_name/:thread_id#[0-9]+#/', name='thread')
@get('/:board_name/:thread_id#[0-9]+#')
@view('thread.tpl')
def thread(board_name, thread_id):
    with active_session as s:
        board = get_board_or_die(s, board_name)
        thread = get_thread_in_board_or_die(s, board, thread_id)
        return dict(board=board, thread=thread)


@post('/:board_name/:thread_id/post', name="post_reply")
@view('post_successful.tpl')
def post_reply(board_name, thread_id):
    with active_session as s:
        board = get_board_or_die(s, board_name)
        thread = get_thread_in_board_or_die(s, board, thread_id)
        image_key = None
        img = request.files.get('image')
        if img is not None: # LOL WAT
            image_key = store_image(img.value)
        thread.last_post_time = func.now()
        poster_name = request.POST.get('poster_name', '')
        s.add(Post(thread=thread,
                   content=sanitize_content(s, request.POST.get('content', '')),
                   poster_name=poster_name,
                   subject=request.POST.get('subject', ''),
                   poster_ip=request.get('REMOTE_ADDR', '0.0.0.0'),
                   image_key=image_key))
        remember_poster_name(poster_name)
        return dict(board=board)


get('/:board_name')(board)


@error(404)
def error404(msg):
    return "well, shit."
