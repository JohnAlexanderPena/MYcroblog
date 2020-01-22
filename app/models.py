# from app import db
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True) # inherits from db.Model, field type as args, also optional args
#     username = db.Column(db.String(64), index=True, unique=True)
#     email =db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#
#     def __repr__(self): # Tells Python how to print Objects of this class
#         return '<User {}>'.format(self.username)
 ##########^^^^^^^^^^^^^ FIRST SETUP ^^^^^^^^^^^^^^################

from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic') ## One to many relationship (defined on the "one" side)
    ## The first argument in the relationship() is the model class of the "many" relationship


    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
