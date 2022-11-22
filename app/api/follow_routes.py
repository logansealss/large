from flask import Blueprint
from sqlalchemy.orm import aliased
from flask_login import current_user, login_required

from app.models import db, User
from app.utils.error_messages import couldnt_be_found

follow_routes = Blueprint("follow", __name__)

# ----------------- GET CURRENT USER'S FOLLOWERS ----------------- #

@follow_routes.route('/current')
@login_required
def followers_for_user():

    user_alias = aliased(User)
    followers = User.query.join(User.following.of_type(user_alias))     \
        .filter(user_alias.id == current_user.id).all()

    return { follower.id: follower.to_dict() for follower in followers }




# ----------------- FOLLOW ANOTHER USER ----------------- #

@follow_routes.route('/<int:user_id>', methods=['PUT'])
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

@follow_routes.route('/<int:user_id>', methods=['DELETE'])
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

