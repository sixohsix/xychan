
import re
import cgi
from uuid import uuid4
from mimetypes import guess_type

from util import *

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


@get('/', name='index')
@view('index.tpl')
def index():
    boards = s.query(Board).order_by(Board.short_name).all()
    return dict(boards=boards)


@get('/setup')
def create_a_board():
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


from login import *

from moderation import *


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
@get('/:board_name/page/:page#[0-9]+#', name='board_page')
@view('board.tpl')
def board(board_name, page=None):
    board = get_board_or_die(s, board_name)
    page_offset = int(page or 0) * c.threads_per_page
    threads = (s.query(Thread)
               .filter(Thread.board == board)
               .order_by(desc(Thread.last_post_time))
               .offset(page_offset).limit(c.threads_per_page))
    threads = [thread for thread in threads if thread.posts]
    return dict(board=board, threads=threads)


def remember_poster_prefs(poster_name, use_tripcode):
    vp = c.visitor_prefs
    if not vp:
        vp = Visitor(cookie_uuid=str(uuid4()))
        s.add(vp)
        set_cookie(VisitorPrefsCookie(vp.cookie_uuid))
    vp.poster_name = poster_name
    vp.use_tripcode = use_tripcode


def handle_post(board_name, thread_id=None):
    board = get_board_or_die(s, board_name)
    if thread_id:
        thread = get_thread_in_board_or_die(s, board, thread_id)
    else:
        thread = Thread(board=board, last_post_time=func.now())
        s.add(thread)
    image_key = None
    img = request.files.get('image')
    if img is not None: # LOL WAT
        image_key = store_image(img.value)
    if not (image_key or get_uni('content').strip()):
        return dict(
            message="No, you must provide an image or some text in your post",
            redirect=url('board', board_name=board.short_name))
    poster_name = get_uni('poster_name')
    use_tripcode = bool(get_uni('use_tripcode'))
    remember_poster_prefs(poster_name, use_tripcode)
    s.add(Post(thread=thread,
               content=sanitize_content(s, get_uni('content')),
               poster_name=poster_name,
               subject=get_uni('subject'),
               poster_ip=request.get('REMOTE_ADDR', '0.0.0.0'),
               image_key=image_key,
               visitor_id=(c.visitor_prefs.id
                           if use_tripcode else None)))
    return dict(message="Post successful",
                redirect=url('board', board_name=board.short_name))


@post('/:board_name/post', name="post_thread")
@view('message.tpl')
def post_thread(board_name):
    return handle_post(board_name)


@get('/:board_name/:thread_id#[0-9]+#/', name='thread')
@get('/:board_name/:thread_id#[0-9]+#')
@view('thread.tpl')
def thread(board_name, thread_id):
    board = get_board_or_die(s, board_name)
    thread = get_thread_in_board_or_die(s, board, thread_id)
    return dict(board=board, thread=thread)


@post('/:board_name/:thread_id#[0-9]+#/post', name="post_reply")
@view('message.tpl')
def post_reply(board_name, thread_id):
    return handle_post(board_name, thread_id)


get(r'/:board_name#[^.]+#')(board)


@get(r'/:file#.+\..+#', name='static')
@cache_forever
def static(file):
    if file.split('.')[-1] in ('py', 'pyo', 'pyc'):
        raise HTTPError(404, "Not found")
    mime_type, encoding = guess_type(file)
    if mime_type:
        response.content_type = mime_type
    return open(STATIC_PATH + os.sep + file, 'rb').read()


@error(404)
def error404(msg):
    return "Page not found."
