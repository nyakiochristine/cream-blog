from ..models import User
from wtforms import SubmitField,TextAreaField,StringField
from wtforms.validators import DataRequired,Email,ValidationError,Length,EqualTo
from flask_wtf.file import FileAllowed,FileField
from flask_login import current_user
from flask_wtf import FlaskForm


class UpdateProfileForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(),Email()])
    picture = FileField(' Update Profile picture', validators=[FileAllowed('jpg','png')])
    submit = SubmitField('Update Profile')
    
    def validate_username(self,username):
        if username.data !=current_user.username:
            user = User.query.filter_by(username = username).first()
            if user:
                raise ValidationError("Username is already taken. Use a different one")
    
    
    def validate_email(self,email):
        if email.data !=current_user.email:
            user = User.query.filter_by(email = email).first()
            if user:
                raise ValidationError("Email is already taken or it is in use. Use a different one")
            
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post', validators=[DataRequired()])
    
    