from ..models import User
from wtforms import SubmitField,PasswordField, ValidationError,BooleanField,StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo,Email,Length

class RegistrationForm(FlaskForm):
    email = StringField('Enter your email address', validators=[DataRequired(),Email()])
    username = StringField('Enter your username', validators=[DataRequired])
    password = PasswordField('Create password',validators=[DataRequired(),EqualTo('password_confirm',message="Passwords must much!")])
    password_confirm = PasswordField('Confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    