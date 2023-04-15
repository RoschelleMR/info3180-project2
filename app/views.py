"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file, send_from_directory
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from app.forms import PostForm
from app.models import Post
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@app.route('/api/v1/users/<user_id>/posts', methods=['GET'])
def userPosts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    postLst = []

    for post in posts:
        postLst.append({
            "id": post.id,
            "caption": post.caption,
            "photo": "/api/v1/photos/{}".format(post.photo),
            "user_id": post.user_id,
            "created_on": post.created_on
        })
    
    data = {"posts": postLst}
    return jsonify(data)

@app.route('/api/v1/users/<user_id>/posts', methods=['POST'])
def addPost(user_id):
    form = PostForm()

    if form.validate_on_submit():
        caption = form.caption.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))

        newPost = Post(caption, filename, user_id)
        db.session.add(newPost)
        db.session.commit()

        return jsonify({"message": "Successfully created a new post"})
    else:
        formErrors = form_errors(form)
        errors = {
            "errors": formErrors
        }
        return jsonify(errors)

@app.route('/api/v1/photos/<filename>')
def getPoster(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)
###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404