from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# instance
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    phone = db.Column(db.String(11), unique=True)
    whatsapp = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    thumb = db.Column(db.String(25))
    benefit = db.relationship('Benefit', backref='user')
    timetrack = db.relationship('Timetrack', backref='user')
    created_at = db.Column(db.String(20), default= datetime.utcnow())


    def __repr__(self):
        return self.username

class Category(db.Model):
    __tablename__  = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=True)
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
    status = db.Column(db.String(8),default='active')
    moderation = db.Column(db.Integer,default=0)
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.String(20), default=datetime.utcnow())

class Timetrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seen = db.Column(db.String(15))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
