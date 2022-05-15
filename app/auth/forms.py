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
    
    
    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("An account already exists with that email")
        
        
    def validate_username(self,data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("An account already exists with that username")
        
        
        



class LoginForm(FlaskForm):
    email = StringField('Enter your email address', validator=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')