
from sqlalchemy import (
    create_engine,
    Table, Column, Integer, String, MetaData, ForeignKey, DateTime,
    func,
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


try:
    configured
except NameError:
    engine = create_engine('sqlite:///:memory:', echo=True)
    #engine = create_engine('sqlite:///test.db', echo=True)
    metadata = MetaData()
    metadata.bind = engine
    Session = sessionmaker(bind=engine)
    Base = declarative_base(metadata=metadata)
    configured = True


class SessionContextMgr(object):
    def __init__(self):
        self.lvl = 0

    def __enter__(self):
        if not self.lvl:
            self.session = Session()
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

active_session = SessionContextMgr()


def DbSessionMiddleware(wrapped_app):
    def _DbSessionMiddleware(environ, start_response):
        with active_session as s:
            environ['db_session'] = s
            return wrapped_app(environ, start_response)
    return _DbSessionMiddleware


class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    short_name = Column(String, nullable=False, unique=True)


class Thread(Base):
    __tablename__ = 'threads'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'), nullable=False)

    board = relationship(Board, backref=backref('threads', order_by=id))


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

    thread = relationship(Thread, backref=backref('posts', order_by=id))


metadata.create_all()
