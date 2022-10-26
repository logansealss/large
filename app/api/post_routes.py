from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required

from app.models import db, Post, Response, Clap
from app.forms.post_form import PostForm
from app.api.auth_routes import validation_errors_to_error_messages

AVG_READING_SPEED = 250

post_routes = Blueprint("post", __name__)

# -------------- GET ALL POSTS -------------- #

@post_routes.route('')
def get_all_posts():
    posts = Post.query.options(joinedload(Post.writer)).all()
    return {post.id: post.preview_to_dict() for post in posts}

# -------------- GET ALL POSTS FOR LOGGED IN USER -------------- #

@post_routes.route('/current')
@login_required
def get_user_posts():
    user_id = current_user.id
    user_posts = Post.query.filter(Post.writer_id == user_id).all()
    return {post.id: post.writer_to_dict() for post in user_posts}

# -------------- GET POST BY ID -------------- #

@post_routes.route('/<int:post_id>')
def get_post_by_id(post_id):
    post_by_id = Post.query.get(post_id)

    if post_by_id is None:
        return {
            "message": "Post couldn't be found",
            "statusCode": 404}, 404

    num_claps = Post.query.join(Clap)           \
        .filter(Post.id == post_id)             \
        .count()

    num_responses = Post.query.join(Response)   \
        .filter(Post.id == post_id)             \
        .count()

    post_dict = post_by_id.to_dict()
    post_dict["numClaps"] = num_claps
    post_dict["numResponses"] = num_responses

    return post_dict

# -------------- CREATE POST -------------- #

@post_routes.route('', methods=["POST"])
def create_post():
    form = PostForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        form_data = form.data
        read_time = len(form_data["post"].split(' ')) // AVG_READING_SPEED
        new_post = Post(writer_id=current_user.id,
                        read_time=read_time,
                        title=form_data["title"],
                        subtitle=form_data["subtitle"],
                        image_url=form_data["image_url"],
                        post=form_data["post"])

        db.session.add(new_post)
        db.session.commit()

        return new_post.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400
