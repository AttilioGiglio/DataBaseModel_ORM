import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True)
    likes_number = Column(Integer, nullable=False)
    comments_number = Column(Integer, nullable=False)
    date = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

class Followers(Base):
    __tablename__ = 'follower'
    id = Column(Integer,primary_key=True)
    follower_number = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

class Followeds(Base):
    __tablename__ = 'followed'
    id = Column(Integer,primary_key=True)
    followed_number = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

class Messages_received(Base):
    __tablename__ = 'message_received'
    id = Column(Integer,primary_key=True)
    message_received_number = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

class Messages_sent(Base):
    __tablename__ = 'message_sent'
    id = Column(Integer,primary_key=True)
    message_sent_number = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)

class Notifications(Base):
    __tablename__ = 'notification'
    id = Column(Integer,primary_key=True)
    notification_number = Column(Integer, nullable=False)
    date = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    follower_id= Column(Integer, ForeignKey('follower.id'))
    follower = relationship(Followers)
    followed_id= Column(Integer, ForeignKey('followed.id'))
    followed = relationship(Followeds)
    message_received_id= Column(Integer, ForeignKey('message_received.id'))
    message_received = relationship(Messages_received)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')