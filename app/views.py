"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file, send_from_directory, g
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.forms import PostForm, LoginForm, RegisterForm
from app.models import Post, Users, Likes, Follow
import os, jwt
from functools import wraps
from datetime import datetime, timedelta



###
# SECURITY FUNCTIONS
###


# generates csrf token
@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})



# decorator to allow route functions to check if a valid jwt token was found
def requires_auth(f):
    
  @wraps(f)
  
  def decorated(*args, **kwargs):
    
    # Note: might use cookie instead since it's easier to set an expiration time
    
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None)

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated


@app.route("/api/v1/generate-token")
def generate_token():
    timestamp = datetime.utcnow()
    # do i update to have username and password?
    payload = {
        "sub": 1,
        "iat": timestamp,
        "exp": timestamp + timedelta(hours=24)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return token

###
# Routing the application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/users/<user_id>', methods=['GET'])
@login_required
#@requires_auth
def getUserDetails(user_id):
    user = Users.query.filter_by(id=user_id).first()
    
    data = {
        "id": user.id,
        "username": user.username,
        "firstname": user.first_name,
        "lastname": user.last_name,
        "email": user.email,
        "location": user.location,
        "biography": user.biography,
        "profile_photo": "/api/v1/photos/{}".format(user.profile_photo),
        "joined_on": user.joined_on
    }
    return jsonify(data)

@app.route('/api/v1/posts', methods=['GET'])
@login_required
@requires_auth
def allPosts():
    posts = Post.query.all()
    postLst = []

    for post in posts:
        #likes = Likes.query.filter_by(post_id=post.id).all() #Waiting to be implemented
        postLst.append({
            "id": post.id,
            "user_id": post.user_id,
            "photo": "/api/v1/photos/{}".format(post.photo),
            "caption": post.caption,
            "created_on": post.created_on
            #"likes": likes
        })
    
    data = {"posts": postLst}
    return jsonify(data)

@app.route('/api/v1/currentuser', methods=['GET'])
def get_user():  
    response = '' 
    if current_user.is_authenticated:
        user = current_user
        response = {'message': user.get_id()}      
    else:    
        response = {'Error': 'User is not logged in'}

    return jsonify(response)

@app.route('/api/v1/users/<user_id>/posts', methods=['GET'])
@login_required
@requires_auth
def userPosts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    postLst = []

    for post in posts:
        postLst.append({
            "id": post.id,
            "user_id": post.user_id,
            "photo": "/api/v1/photos/{}".format(post.photo),
            "description": post.caption,
            "created_on": post.created_on
        })
    
    data = {"posts": postLst}
    return jsonify(data)

@app.route('/api/v1/users/<user_id>/posts', methods=['POST'])
@login_required
@requires_auth
def addPost(user_id):
    form = PostForm()

    if form.validate_on_submit():
        caption = form.caption.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)

        newPost = Post(caption, filename, user_id)
        db.session.add(newPost)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
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


@app.route('/api/v1/posts/<postID>/like', methods = ['POST'])
@login_required
@requires_auth
def like(postID):
    response = ''
    
    user_id = current_user.id
    post_id = postID
    
    like= Likes(post_id, user_id)
    
    #  add like to database
    
    db.session.add(like)
    db.session.commit()
    
    response = {'message': 'Successfully liked post'}

    return response

##Added by Shadean
@app.route('/api/v1/register',methods=["POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        username =form.username.data
        password = form.password.data
        first_name = form.firstName.data
        last_name = form.lastName.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = form.photo.data
        filename = secure_filename(profile_photo.filename)

        user = Users(username, password, first_name, last_name, email, location, biography, filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        db.session.add(user)
        db.session.commit()

        return jsonify({'message': f"Account was successfully created for {username}!!"})
    
    else:
        db.session.rollback()
        formErrors = form_errors(form)
        errors = {
            "errors": formErrors
        }
        return jsonify(errors)

@app.route('/api/v1/users/<user_id>/follow', methods=['GET'])
@login_required
@requires_auth
def getFollowers(user_id):
    
    if request.method == 'GET':
        
        # count = 0
    
        followers = Follow.query.filter_by(target_id=user_id).all()
        followersLst = []

        for follow in followers:
            # count += 1
            followersLst.append(follow.user_id)
            
        
        
        data = {"followers": followersLst}
        return jsonify(data)
    
@app.route('/api/v1/users/<user_id>/follow', methods=['POST'])
@login_required
@requires_auth
def follow(user_id):
    if request.method == 'POST':
        response = request.get_json()
        target_id = response['target_id']
        target_user = Users.query.filter_by(target_id=target_id).all()

        if target_id == user_id:
            return jsonify({'message': "You cannot follow your self"})

        follow = Follow.query.filter_by(user_id=response['user_id'], target_id=response['target_id'])
        if follow != None:
            return jsonify({'message' : "You are already following this user"})

        follow = Follow(response['user_id'], response['target_id'])
        db.session.add(follow)
        db.session.commit()

        return jsonify({'message' : f'You are now following {target_user.username}'})
    

# Login route
@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    
    form = LoginForm()
    
    message = ''
    
    if request.method == "POST":
        if form.validate_on_submit():
            
            # Get the username and password values from the form.
            
            username = form.username.data
            password = form.password.data
            
            
            user = db.session.execute(db.select(Users).filter_by(username=username)).scalar()
            
            if user is not None and (check_password_hash(user.password, password)):
                # Gets user id, load into session
                login_user(user)

                message = {'token': generate_token()}
                
            else:
                
                message = {'errors': ['Username or password not correct']}
                
        else:
            errors = form_errors(form)
        
            if (errors):
                
                error_list = {"errors": []}
                
                error_list['errors'] = errors
                
                message = error_list
                
        
        return jsonify(message)  
        
   
#Logout route


@app.route("/api/v1/auth/logout", methods=['POST'])
@requires_auth
@login_required
def logout():
    
    logout_user()
    
    message = {'success':'Successfully logged out'}
    
    return jsonify(message)
     

@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(Users).filter_by(id=id)).scalar()




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


# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404