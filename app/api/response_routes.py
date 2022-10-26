from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required

from app.models import db, Post, Response
from app.utils.error_messages import couldnt_be_found, forbidden, deleted
from app.api.auth_routes import validation_errors_to_error_messages

response_routes = Blueprint("response", __name__)

# -------------- GET ALL RESPONSES FOR LOGGED IN USER -------------- #

@response_routes.route('/current')
@login_required
def get_user_response():
    user_id = current_user.id
    user_responses = Response.query.filter(Response.user_id == user_id).all()
    return {response.id: response.to_dict() for response in user_responses}

# -------------- GET A RESPONSE BY ID -------------- #

@response_routes.route('/<int:response_id>')
@login_required
def get_response_by_id(response_id):
    response_by_id = Response.query.get(response_id)

    if response_by_id is None:
        return couldnt_be_found("Response")

    return response_by_id.to_dict()