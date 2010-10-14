
from util import *

@get("/mod")
def mod():
    raise HTTPError(302, "Found", header=[('Location', url('mod_home'))])


@get("/mod/home", name="mod_home")
@view("mod_home.tpl")
@admin_only
def mod_home():
    return dict()


def delete_post_or_thread(post):
    if post.is_first:
        thread = post.thread
        [s.delete(p) for p in thread.posts]
        s.delete(thread)
    else:
        s.delete(post)


@get("/mod/post/:post_id#[0-9]+#", name="mod_post")
@view("moderate_post.tpl")
@admin_only
def mod_post(post_id):
    post = s.query(Post).filter(Post.id == post_id).first()
    if not post:
        return template("message.tpl", message="Post already vanished",
                        redirect=None)
    return dict(post=post)


@post("/mod/post/submit", name="mod_submit")
@view("message.tpl")
@admin_only
def mod_submit():
    post = s.query(Post).filter(Post.id == get_uni("post_id")).first()
    if not post:
        return template("message.tpl", message="Post already vanished",
                        redirect=None)

    redirect = url("board", board_name=post.thread.board.short_name)
    if get_uni("pin"):
        post.thread.pinned = 1
    elif get_uni("unpin"):
        post.thread.pinned = 0
    elif get_uni("lock"):
        post.thread.locked = 1
    elif get_uni("unlock"):
        post.thread.locked = 0
    elif get_uni("delete"):
        delete_post_or_thread(post)
    elif get_uni("delete_and_ban"):
        days = int(get_uni("num_days_to_ban"))
        delete_post_or_thread(post)
        s.add(IpBan(ip_address=post.poster_ip,
                    ban_expire=datetime.now() + timedelta(days=days)))
    elif get_uni("delete_and_ban_forever"):
        delete_post_or_thread(post)
        s.add(IpBan(ip_address=post.poster_ip, ban_expire=None))
    elif get_uni("annihilate"):
        raise NotImplemented()
    else:
        raise Exception("wat?")

    return dict(message="Thy will be done", redirect=redirect)


@get("/mod/bans", name="mod_bans")
@view("mod_bans.tpl")
@admin_only
def mod_bans():
    bans = s.query(IpBan).order_by(IpBan.ban_start).all()
    return dict(bans=bans)


@post("/mod/ban_submit", name="mod_ban_submit")
@view("message.tpl")
@admin_only
def mod_ban_submit():
    ban = s.query(IpBan).filter(IpBan.id == get_uni("ban_id")).first()
    if not ban:
        return dict(message="Ban not there", redirect=url('mod_bans'))

    ban.ban_expire = datetime.now()
    return dict(message="Ban lifted", redirect=url('mod_bans'))


@get("/mod/boards", name="mod_boards")
@view("mod_boards.tpl")
@admin_only
def mod_board():
    boards = s.query(Board).order_by(Board.id).all()
    return dict(boards=boards)

@post("/mod/boards/create", name="mod_create_board")
@view("message.tpl")
@admin_only
def mod_create_board():
    short_name = request.forms['short_name']
    long_name = request.forms['long_name']
    board = Board(short_name=short_name, long_name=long_name)
    s.add(board)
    return dict(message="Board created", redirect=url("mod_boards"))

@get("/mod/boards/lock/:board_name", name="mod_lock")
@view("message.tpl")
@admin_only
def mod_lock_board(board_name):
    locked = 1 if request.GET['state'] == 'lock' else 0
    board = s.query(Board).filter(Board.short_name == board_name).first()
    board.locked = locked
    return dict(message="Done.", redirect=url("mod_boards"))


@get("/mod/boards/hide/:board_name", name="mod_hide")
@view("message.tpl")
@admin_only
def mod_lock_board(board_name):
    hidden = 1 if request.GET['state'] == 'hide' else 0
    board = s.query(Board).filter(Board.short_name == board_name).first()
    board.hidden = hidden
    return dict(message="Done.", redirect=url("mod_boards"))
