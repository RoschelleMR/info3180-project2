# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.csrf import CSRFProtect

class PostForm(FlaskForm):
    caption = StringField('Caption', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
            FileRequired(),
            FileAllowed(['jpg', 'png'], 'Images only!')
        ])