from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

# instance
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    phone = db.Column(db.String(11))
    whatsapp = db.Column(db.String(11))
    password = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    thumb = db.Column(db.String(25))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())
    benefit = db.relationship('Benefit', backref='user')
    created_at = db.Column(db.DateTime, default= datetime.utcnow())
    def __repr__(self):
        return self.username

class Category(db.Model):
    __tablename__  = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=True)
    icon = db.Column(db.String(20), default="&CircleDot;")
    benefit = db.relationship('Benefit', backref='category')

class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12),nullable=True)
    benefit = db.relationship('Benefit', backref='state')

class Benefit(db.Model):
    __tablename__ = 'benefits'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    desc = db.Column(db.Text(800), nullable=False)
    moderation = db.Column(db.Integer,default=0)
    thumbone = db.Column(db.String(50),nullable=False)
    thumbtwo = db.Column(db.String(50),nullable=False)
    thumbthree = db.Column(db.String(50),nullable=False)
    slug = db.Column(db.String(50), default=uuid.uuid4(), nullable=True)
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(400), nullable=False)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(25), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

