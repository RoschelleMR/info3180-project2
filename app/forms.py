# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Email
from flask_wtf.csrf import CSRFProtect

class PostForm(FlaskForm):
    caption = StringField('Caption', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png'], 'Images only!')
        ])
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    firstName = StringField('Firstname', validators=[InputRequired()])
    lastName = StringField('Lastname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png'], 'Images only!')
        ])
