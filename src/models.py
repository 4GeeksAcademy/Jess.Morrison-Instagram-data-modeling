import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)

    def serialize(self):
        return {
            "email": self.email,
            "username": self.username,
            "first name": self.firstname,
            "last name": self.lastname,
        }

class Follower(Base):
    __tablename__ = 'Follower'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_from = relationship(User)
    user_to = relationship(User)   

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }
    
class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    

    def serialize(self):
        return {
            "user_id": self.user_id
        }
    
class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False)
    url = Column(String(120), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def serialize(self):
        return {
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id,
        }
    
class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(260), nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author = relationship(User)
    post = relationship(Post)

    def serialize(self):
        return {
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id,
        }

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
