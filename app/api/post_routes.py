from flask import Blueprint, jsonify, session, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required
from app.models import db, Post, Response

post_routes = Blueprint("post", __name__)

@post_routes.route('')
def get_all_posts():

    posts = Post.query.options(joinedload(Post.writer)).all()
    return {post.id: post.to_dict() for post in posts}

@post_routes.route('/current')
@login_required
def get_user_posts():

    user_id = current_user.id
    user_posts = Post.query.filter(Post.writer_id == user_id).all()
    return {post.id: post.writer_to_dict() for post in user_posts}

# @post_routes.route('')