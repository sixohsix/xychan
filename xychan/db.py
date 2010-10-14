
from __future__ import with_statement

import math
from sha import sha
from datetime import datetime

from sqlalchemy import (
    create_engine,
    Table, Column, Integer, String, MetaData, ForeignKey, DateTime,
    func, or_
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql.expression import desc

from base62 import num_encode


metadata = MetaData()
Session = sessionmaker()
Base = declarative_base(metadata=metadata)

def random_str():
    import random
    return num_encode(random.randint(0, 18446744073709551615L))


class SessionContextMgr(object):
    def __init__(self):
        self.lvl = 0

    def __enter__(self):
        if not self.lvl:
            self.session = Session()
            __builtins__['s'] = self.session
        self.lvl += 1
        return self.session

    def __exit__(self, typ, value, tb):
        self.lvl -= 1
        if not self.lvl:
            if typ:
                self.session.rollback()
            else:
                self.session.commit()
            self.session = None
            del __builtins__['s']

active_session = SessionContextMgr()


def DbSessionMiddleware(wrapped_app):
    def _DbSessionMiddleware(environ, start_response):
        with active_session as s:
            environ['db_session'] = s
            return wrapped_app(environ, start_response)
    return _DbSessionMiddleware


def get_all_visible_boards():
    return s.query(Board).filter(Board.hidden == 0).all()


class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    short_name = Column(String, nullable=False, unique=True)
    locked = Column(Integer(1), nullable=False, default=0)
    hidden = Column(Integer(1), nullable=False, default=0)
    long_name = Column(String, nullable=False, unique=True)


    @property
    def num_pages(self):
        return int(math.ceil(float(len(self.threads)) / c.threads_per_page))


    @property
    def pretty_title(self):
        return "/%s/ - %s" % (self.short_name, self.long_name)


class Thread(Base):
    __tablename__ = 'threads'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'), nullable=False)
    last_post_time = Column(DateTime)
    pinned = Column(Integer(1), nullable=False, default=0)
    locked = Column(Integer(1), nullable=False, default=0)

    board = relationship(Board,
                         backref=backref(
            'threads', order_by=desc(last_post_time)))


    @property
    def short_view_posts(self):
        posts = self.posts
        if len(posts) < 5:
            return posts[:]
        else:
            return posts[0:1] + posts[-3:]


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    thread_id = Column(Integer, ForeignKey('threads.id'), nullable=False)
    posted = Column(DateTime, nullable=False, default=func.now())
    poster_ip = Column(String, nullable=False)
    poster_name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    content = Column(String, nullable=False)
    image_key = Column(String)
    visitor_id = Column(Integer, ForeignKey('visitors.id'),
                        nullable=True)

    thread = relationship(Thread, backref=backref('posts', order_by=id))
    visitor = relationship('Visitor', backref=backref('posts', order_by=id))

    @property
    def is_first(self):
        return self == self.thread.posts[0]

    @property
    def tripcode(self):
        if self.visitor_id:
            return self.visitor.tripcode

    @property
    def formatted_date(self):
        return self.posted.strftime('%d %B %Y %H:%M')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    def _calc_password(self, password):
        sig = sha()
        sig.update(str(self.username))
        sig.update('saltysalt8828282')
        sig.update(password)
        return sig.hexdigest()


    def _get_password(self):
        raise Exception("Write only")
    def _set_password(self, v):
        self.password_hash = self._calc_password(v)

    password = property(_get_password, _set_password)


    def verify_password(self, password):
        return self.password_hash == self._calc_password(password)


class Visitor(Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True)
    cookie_uuid = Column(String, unique=True, nullable=False)
    poster_name = Column(String, nullable=False, default='')
    tripcode = Column(String, nullable=False, default=random_str)
    use_tripcode = Column(Integer(1), nullable=False, default=0)


class IpBan(Base):
    __tablename__ = 'ip_ban'

    id = Column(Integer, primary_key=True)
    ip_address = Column(String, nullable=False)
    ban_start = Column(DateTime, nullable=False, default=func.now())
    ban_expire = Column(DateTime, nullable=True, default=None)

    @property
    def is_active(self):
        return self.ban_expire == None or self.ban_expire > datetime.now()

    @classmethod
    def ip_is_banned(cls, ip_addr):
        return (s.query(IpBan).filter(IpBan.ip_address == ip_addr)
                .filter(or_(
                    IpBan.ban_expire > func.now(),
                    IpBan.ban_expire == None))
                .count())


def configure_db(db_uri, echo=False):
    engine = create_engine(db_uri, echo=echo)
    metadata.bind = engine
    Session.bind = engine
    metadata.create_all()
