from flask_login import UserMixin
from datetime import datetime
from  werkzeug.security import check_password_hash,generate_password_hash


class Quote:
    '''
    to define quote objects
    '''
    
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote


class User(UserMixin):
    
    
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
        
    
        
        