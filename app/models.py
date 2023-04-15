# Add any model classes for Flask-SQLAlchemy here
from . import db
import datetime

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(250))
    photo = db.Column(db.String(250))
    user_id = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, caption, photo, user_id):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<post: %r>' % (self.id)