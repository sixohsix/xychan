
from sqlalchemy import (
    create_engine,
    Table, Column, Integer, String, MetaData, ForeignKey,
    )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
metadata.bind = engine

Session = sessionmaker(bind=engine)

Base = declarative_base(metadata=metadata)

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


class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True)
    short_name = Column(String, nullable=False)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'), nullable=False)
    content = Column(String)

    board = relationship(Board, backref=backref('posts', order_by=id))

metadata.create_all()
