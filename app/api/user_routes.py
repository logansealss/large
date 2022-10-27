from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Post

user_routes = Blueprint('users', __name__)

@user_routes.route('/<int:id>/posts')
def user(id):
    user_posts = Post.query.filter(Post.writer_id == id).all()
    return { post.id: post.writer_to_dict() for post in user_posts }
