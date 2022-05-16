from flask_login import UserMixin
from datetime import datetime
from . import db,login_manager

from  werkzeug.security import check_password_hash,generate_password_hash


class Quote:
    '''
    to define quote objects
    '''
    
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    image_file = db.Column(db.String, nullable=False,default='default.jpg')
    hash_pass = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    photos = db.relationship('PhotoProfile',backref = 'user',lazy = "dynamic")
    
    
    
    @property
    def password(self):
        raise AttributeError("Unable to read this")
    
    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)
        
    def  set_password(self,password):
        self.hash_pass = generate_password_hash(password)
        
    def verify_password(self,password):
        self.hash__pass = check_password_hash(password)
        
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
    
    





class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'
    id = db.Column(db.Integer, primary_key=True)
    picture_path = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    
   
   
        
        