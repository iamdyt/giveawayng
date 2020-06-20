from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# instance
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    phone = db.Column(db.String(11), unique=True)
    password = db.Column(db.String(400), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    thumb = db.Column(db.String(25))
    created_at = db.Column(db.String(20), default= datetime.utcnow())

    def __repr__(self):
        return self.username