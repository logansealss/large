from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required
from app.models import db, Post, Response, Clap

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
    form = TaskForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form_data = form.data
        new_task = Task(user_id=current_user.id,
                        name=form_data["name"],
                        priority=form_data["priority"],
                        start_date=form_data["start_date"],
                        due_date=form_data["due_date"],
                        duration=form_data["duration"],
                        list_id=form_data["list_id"],
                        note=form_data["note"],
                        completed=form_data["completed"])

        db.session.add(new_task)
        db.session.commit()

        return new_task.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400
