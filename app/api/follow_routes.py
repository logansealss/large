from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required

from app.models import db, User
from app.utils.error_messages import couldnt_be_found, forbidden, deleted
from app.api.auth_routes import validation_errors_to_error_messages

follow_routes = Blueprint("follow", __name__)

# ----------------- FOLLOW ANOTHER USER ----------------- #

@follow_routes.route('/<int:user_id>', methods=['PUT'])
@login_required
def follow_user_by_id(user_id):
    user_by_id = User.query.get(user_id)

    if user_by_id is None:
        return couldnt_be_found("User")

    user_by_id.followers.append(current_user)

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

    user_by_id.followers.remove(current_user)

    return {
        "message": "Successfully unfollowed user",
        "statusCode": 200
    }