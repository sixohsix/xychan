
from .util import *

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
    return dict(message="Shit's trashed, yo", redirect=redirect)
