
from util import *

@get('/:board_name/atom-threads.xml', name='atom-threads')
@view('feeds/atom-posts.tpl')
def atom_threads(board_name):
    response.content_type = 'text/xml'
    board = get_board_or_die(s, board_name)
    threads = (s.query(Thread).filter(Thread.board_id == board.id)
               .order_by(desc(Thread.id))
               .limit(50))

    posts = [thread.posts[0] for thread in threads]
    feed_title = "Threads in %s - %s" % (board.pretty_title, c.server_name)
    feed_url = rurl('atom-threads', board_name=board_name)
    self_url = rurl('board', board_name=board.short_name)
    return locals()


@get(':board_name/:thread_id#[0-9]+#/atom.xml', name='atom-thread-posts')
@view('feeds/atom-posts.tpl')
def atom_thread_posts(board_name, thread_id):
    response.content_type = 'text/xml'
    board = get_board_or_die(s, board_name)
    thread = get_thread_in_board_or_die(s, board, thread_id)
    posts = (s.query(Post).filter(Post.thread_id == thread.id)
             .order_by(desc(Post.id))
             .limit(50))

    feed_title = "Posts in %s thread %i - %s" % (
        board.pretty_title, thread.id, c.server_name)
    feed_url = rurl('atom-thread-posts', board_name=board.short_name,
                    thread_id=thread.id)
    self_url = rurl('thread', board_name=board.short_name, thread_id=thread.id)
    return locals()
