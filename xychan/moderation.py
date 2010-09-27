
from util import *

@get("/mod/home")
@view("mod_home.tpl")
@admin_only
def mod_home():
    return dict()


@post("/mod/trash_post/:post_id#[0-9]+#", name="trash_post")
@view("message.tpl")
@admin_only
def trash_post(post_id):
    post = s.query(Post).filter(Post.id == post_id).first()
    if post:
        redirect = url("board", board_name=post.thread.board.short_name)
        if post.is_first:
            thread = post.thread
            [s.delete(p) for p in thread.posts]
            s.delete(thread)
        else:
            s.delete(post)
    else:
        redirect = url("index")
    return dict(message="Trashed", redirect=redirect)


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
    if get_uni("delete"):
        s.delete(post)
    elif get_uni("delete_and_ban"):
        days = int(get_uni("num_days_to_ban"))
        s.delete(post)
        s.add(IpBan(ip_address=post.poster_ip,
                    ban_expire=datetime.now() + timedelta(days=days)))
    elif get_uni("delete_and_ban_forever"):
        s.delete(post)
        s.add(IpBan(ip_address=post.poster_ip, expire=None))
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
