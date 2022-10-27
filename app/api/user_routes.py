from flask import Blueprint
from sqlalchemy.orm import joinedload

from app.models import User, Post
from app.utils.error_messages import couldnt_be_found


user_routes = Blueprint('users', __name__)

@user_routes.route('/<int:id>/posts')
def user(id):

    user = User.query.get(id)

    if user is None:
        return couldnt_be_found("User")

    user_posts = Post.query.filter(Post.writer_id == id)                \
        .options(joinedload(Post.writer)).all()
    return { post.id: post.preview_to_dict() for post in user_posts }
