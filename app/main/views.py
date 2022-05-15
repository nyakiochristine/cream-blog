from  flask import render_template, request, abort, flash, current_app
from ..models import User,  Quote
import os
from flask_login import  current_user,login_required
from . import main
from ..request import get_quote


@main.route('/')
def index():
    title= "Blog Posts"
    quote = get_quote()
    
    
    return render_template('index.html',title=title,quote=quote)

@main.route('/home')





