from  flask import render_template,Blueprint,url_for,flash,redirect,request

from app.main.views import home
from ..models import User
from app import auth
from flask_login import login_required,login_user,logout_user,current_user
from .forms import RegistrationForm, LoginForm, ResetPassword,NewPassword
import os


@auth.route('/login',methods=['GET', 'POST'])
def login():
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
        login_user = (user ,login_form.remember.data)
        return redirect(request.args.get('next') or url_for('main.home'))
    flash("Incorrect Username or Invalid Password")#
    
    title = "Welcome to Cream Blog!"
    return render_template('auth/login.html', login_form= login_form ,title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user ()
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash("Account  for {form.username.data} has been successfully registered")
        user =  User(email= form.email.data,username=form.username.data, password= form.password.data)
        
        
        return redirect(url_for('auth.login'))
    title = " Welcome to Cream Blog!"
    return render_template('auth/register.html',registration_form= form,title=title)
