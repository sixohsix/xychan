
from .util import *
from .db import *

def get_board_or_die(s, board_name):
    board = s.query(Board).filter(Board.short_name == board_name).first()
    if not board:
        raise HTTPError(404, "No such board.")
    return board


@get('/')
def index():
    return "Go to the first board: <a href='/test/'>go there</a>."


@get('/favicon.ico')
def favicon():
    response.content_type = "image/png"
    return open('./xychan/static/favicon.png').read()


@get('/style.css')
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
    return dict()


@get('/:board_name')
@get('/:board_name/')
@view('board.tpl')
def board(board_name):
    with active_session as s:
        board = get_board_or_die(s, board_name)
        threads = (s.query(Thread)
                   .filter(Thread.board == board).all())
        return dict(board=board, threads=threads)


@post('/:board_name/post')
@view('post_successful.tpl')
def post_thread(board_name):
    with active_session as s:
        board = get_board_or_die(s, board_name)
        image_key = None
        img = request.files.get('image')
        if img is not None: # LOL WAT
            image_key = store_image(img.value)
        thread = Thread(board=board)
        s.add(thread)
        s.add(Post(thread=thread,
                   content=request.POST.get('content', ''),
                   poster_name=request.POST.get('poster_name', ''),
                   subject=request.POST.get('subject', ''),
                   poster_ip=request.get('REMOTE_ADDR', '0.0.0.0'),
                   image_key=image_key))
        return dict(board=board)


@get('/t_/:image')
def get_thumbnail(image):
    thumb_data = fetch_thumb(image)
    response.content_type = 'image/' + image.split('.')[-1]
    return thumb_data


@get('/i_/:image')
def get_image(image):
    thumb_data = fetch_image(image)
    response.content_type = 'image/' + image.split('.')[-1]
    return thumb_data


@error(404)
def error404(msg):
    return "well, shit."
