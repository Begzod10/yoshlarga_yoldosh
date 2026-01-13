from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import String, Integer, Boolean, Float, Column, ForeignKey, DateTime, or_, and_, desc, func, ARRAY, \
    JSON, \
    extract, Date, BigInteger
from sqlalchemy.orm import contains_eager
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, functions
from pprint import pprint
import uuid
from datetime import datetime

db = SQLAlchemy()


def db_setup(app):
    app.config.from_object('backend.models.config')
    db.app = app
    db.init_app(app)
    Migrate(app, db)
    return db


class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender = Column(String)
    tests = relationship('Test', backref='user', lazy="select", order_by="Test.id")

    def add(self):
        db.session.add(self)
        db.session.commit()


class TestInfo(db.Model):
    __tablename__ = "test_info"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)

    def add(self):
        db.session.add(self)
        db.session.commit()


class TestAnswerOptions(db.Model):
    __tablename__ = "test_answer_option"
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    desc = Column(String)
    test_info_id = Column(Integer, ForeignKey('test_info.id'))
    tests = relationship("Test", backref="answer_option", order_by="Test.id", lazy="select")

    def add(self):
        db.session.add(self)
        db.session.commit()


class Test(db.Model):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    test_info_id = Column(Integer, ForeignKey('test_info.id'))
    answer = Column(String)
    day = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    value = Column(Integer)
    test_answer_options_id = Column(Integer, ForeignKey('test_answer_option.id'))

    def add(self):
        db.session.add(self)
        db.session.commit()
