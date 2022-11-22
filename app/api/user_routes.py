from flask import Blueprint
from sqlalchemy.orm import joinedload, aliased
from flask_login import current_user, login_required

from app.models import db, User, Post
from app.utils.error_messages import couldnt_be_found

user_routes = Blueprint('users', __name__)

# ----------------- GET CURRENT USER'S POSTS ----------------- #

@user_routes.route('/<int:id>/posts')
def get_posts_by_user(id):

    user = User.query.get(id)

    if user is None:
        return couldnt_be_found("User")

    user_posts = Post.query.filter(Post.writer_id == id)                \
        .options(joinedload(Post.writer)).all()
    return { post.id: post.preview_to_dict() for post in user_posts }

# ----------------- GET CURRENT USER'S FOLLOWERS ----------------- #

@user_routes.route('/current/followers')
@login_required
def followers_for_user():

    user_alias = aliased(User)
    followers = User.query.join(User.following.of_type(user_alias))     \
        .filter(user_alias.id == current_user.id).all()

    return { follower.id: follower.to_dict() for follower in followers }

# ----------------- GET FOLLOWERS FOR USER BY USER'S ID ----------------- #

@user_routes.route('/<int:user_id>/followers')
@login_required
def followers_for_user_by_id(user_id):

    user_by_id = User.query.get(user_id)

    if user_by_id is None:
        return couldnt_be_found("User")

    user_alias = aliased(User)
    followers = User.query.join(User.following.of_type(user_alias))     \
        .filter(user_alias.id == user_id).all()

    return { follower.id: follower.to_dict() for follower in followers }

# ----------------- GET CURRENT USER'S FOLLOWING ----------------- #

@user_routes.route('/current/following')
@login_required
def following_for_user():

    user = User.query.options(joinedload(User.following)).get(current_user.id)

    return { following.id: following.id for following in user.following}



# ----------------- FOLLOW ANOTHER USER ----------------- #

@user_routes.route('/<int:user_id>/follow', methods=['POST'])
@login_required
def follow_user_by_id(user_id):
    if user_id == current_user.id:
        return {
            "message": "Cannot follow yourself",
            "statusCode": 403
        }, 403

    user_by_id = User.query.get(user_id)

    if user_by_id is None:
        return couldnt_be_found("User")

    user_by_id.followers.append(current_user)

    db.session.commit()

    return {
        "message": "Successfully followed user",
        "statusCode": 200
    }

# ----------------- UNFOLLOW ANOTHER USER ----------------- #

@user_routes.route('/<int:user_id>/follow', methods=['DELETE'])
@login_required
def unfollow_user_by_id(user_id):
    user_by_id = User.query.get(user_id)

    if user_by_id is None:
        return couldnt_be_found("User")

    if(current_user not in user_by_id.followers):
        return {
            "message": "Not following the provided user",
            "statusCode": 403
        }, 403

    user_by_id.followers.remove(current_user)
    db.session.commit()

    return {
        "message": "Successfully unfollowed user",
        "statusCode": 200
    }