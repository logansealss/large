from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required

from app.models import db, Post, Response, Clap
from app.forms.post_form import CreatePostForm, UpdatePostForm
from app.forms.response_form import ResponseForm
from app.forms.clap_form import ClapForm
from app.api.auth_routes import validation_errors_to_error_messages
from app.utils.reading_speed import read_time_from_string
from app.utils.error_messages import couldnt_be_found, forbidden, deleted

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
    user_posts = Post.query.filter(Post.writer_id == user_id)       \
        .options(joinedload(Post.writer)).all()
    return {post.id: post.preview_to_dict() for post in user_posts}

# -------------- GET POST BY ID -------------- #

@post_routes.route('/<int:post_id>')
def get_post_by_id(post_id):
    post_by_id = Post.query.get(post_id)

    if post_by_id is None:
        return couldnt_be_found("Post")

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

# -------------- GET ALL RESPONSES TO A POST -------------- #

@post_routes.route('/<int:post_id>/responses')
def get_post_responses(post_id):
    post_responses = Response.query.filter(Response.post_id == post_id)     \
        .options(joinedload(Response.user)).all()
    return {response.id: response.to_dict_with_user() for response in post_responses}

# -------------- GET ALL CLAPS FOR A POST -------------- #

@post_routes.route('/<int:post_id>/claps')
def get_post_claps(post_id):
    post_claps = Clap.query.filter(Clap.post_id == post_id)     \
        .options(joinedload(Clap.user)).all()
    return {clap.id: clap.to_dict_with_user() for clap in post_claps}

# -------------- CREATE A POST -------------- #

@post_routes.route('', methods=["POST"])
@login_required
def create_post():
    form = CreatePostForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        form_data = form.data
        read_time = read_time_from_string(form_data["post"])
        new_post = Post(writer_id=current_user.id,
                        read_time=read_time,
                        title=form_data["title"],
                        subtitle=form_data["subtitle"],
                        image_url=form_data["image_url"],
                        post=form_data["post"])

        db.session.add(new_post)
        db.session.commit()

        new_post_dict = new_post.writer_to_dict()
        new_post_dict['writer'] = current_user.to_dict()
        del new_post_dict['writerId']

        return new_post_dict

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# -------------- CREATE A RESPONSE -------------- #

@post_routes.route('<int:post_id>/responses', methods=["POST"])
@login_required
def create_response(post_id):

    post_by_id = Post.query.get(post_id)

    if post_by_id is None:
        return couldnt_be_found("Post")

    form = ResponseForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        form_data = form.data

        new_response = Response(user_id=current_user.id,
                                post_id=post_id,
                                response=form_data["response"])

        db.session.add(new_response)
        db.session.commit()

        new_response_dict = new_response.to_dict()
        new_response_dict["user"] = current_user.to_dict()
        del new_response_dict["userId"]

        return new_response_dict

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# -------------- CREATE A CLAP -------------- #

@post_routes.route('<int:post_id>/claps', methods=["POST"])
@login_required
def create_clap(post_id):

    post_by_id = Post.query.get(post_id)

    if post_by_id is None:
        return couldnt_be_found("Post")

    clap_for_post_from_user = Clap.query                                        \
        .filter(Clap.post_id == post_id, Clap.user_id == current_user.id)       \
        .first()

    print(clap_for_post_from_user)

    if clap_for_post_from_user:
        return {
            "message": "User already has a clap for this post",
            "statusCode": 403
            }, 403

    form = ClapForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        form_data = form.data

        new_clap = Clap(user_id=current_user.id,
                                post_id=post_id,
                                amount=form_data["amount"])

        db.session.add(new_clap)
        db.session.commit()

        new_clap_dict = new_clap.to_dict()
        new_clap_dict["user"] = current_user.to_dict()
        del new_clap_dict["userId"]

        return new_clap_dict

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# -------------- UPDATE A POST -------------- #

@post_routes.route('/<int:post_id>', methods=["PUT"])
@login_required
def update_post_by_id(post_id):
    post_by_id = Post.query.get(post_id)

    if post_by_id is None:
        return couldnt_be_found("Post")

    if post_by_id.writer_id != current_user.id:
        return forbidden()

    form = UpdatePostForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        form_data = form.data

        if form_data["title"]:
            post_by_id.title = form_data["title"]

        if form_data["subtitle"] is not None:
            if form_data["subtitle"] == "":
                post_by_id.subtitle = None
            else:
                post_by_id.subtitle = form_data["subtitle"]

        if form_data["post"]:
            post_by_id.post = form_data["post"]
            read_time = read_time_from_string(form_data["post"])
            post_by_id.read_time = read_time

        if form_data["image_url"] is not None:
            if form_data["image_url"] == "":
                post_by_id.image_url = None
            else:
                post_by_id.image_url = form_data["image_url"]

        db.session.commit()

        post_by_id_dict = post_by_id.writer_to_dict()
        post_by_id_dict["writer"] = current_user.to_dict()
        del post_by_id_dict["writerId"]

        return post_by_id_dict

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# -------------- DELETE A POST -------------- #

@post_routes.route('/<int:post_id>', methods=["DELETE"])
@login_required
def delete_post_by_id(post_id):
    post_by_id = Post.query.get(post_id)

    if post_by_id is None:
        return couldnt_be_found("Post")

    if post_by_id.writer_id != current_user.id:
        return forbidden()

    db.session.delete(post_by_id)
    db.session.commit()

    return deleted()