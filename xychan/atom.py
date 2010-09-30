
from util import *

@get('/:board_name/atom-threads', name='atom-threads')
@view('feeds/atom-posts.tpl')
def atom_threads(board_name):
    response.content_type = 'text/xml'
    board = get_board_or_die(s, board_name)
    threads = (s.query(Thread).filter(Thread.board_id == board.id)
               .order_by(desc(Thread.id))
               .limit(50))

    posts = [thread.posts[0] for thread in threads]
    feed_title = "Threads in %s" % board.short_name
    feed_url = rurl('atom-threads', board_name=board_name)
    return locals()
