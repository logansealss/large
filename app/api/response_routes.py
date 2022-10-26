from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required

from app.models import db, Post, Response
from app.api.auth_routes import validation_errors_to_error_messages

response_routes = Blueprint("response", __name__)

# -------------- GET ALL RESPONSES FOR LOGGED IN USER -------------- #

@response_routes.route('/current')
@login_required
def get_user_response():
    user_id = current_user.id
    user_responses = Response.query.filter(Response.user_id == user_id).all()
    return {response.id: response.to_dict() for response in user_responses}