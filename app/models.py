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
        