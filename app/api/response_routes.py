from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required

from app.models import db, Response
from app.utils.error_messages import couldnt_be_found, forbidden, deleted
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms.response_form import ResponseForm

response_routes = Blueprint("response", __name__)

# -------------- GET ALL RESPONSES FOR LOGGED IN USER -------------- #

@response_routes.route('/current')
@login_required
def get_user_response():
    user_id = current_user.id
    user_responses = Response.query                     \
        .filter(Response.user_id == user_id)            \
        .options(joinedload(Response.user))             \
        .all()
    
    return {response.id: response.to_dict_with_user() for response in user_responses}

# -------------- GET A RESPONSE BY ID -------------- #

@response_routes.route('/<int:response_id>')
@login_required
def get_response_by_id(response_id):
    response_by_id = Response.query             \
        .options(joinedload(Response.user))     \
        .get(response_id)                       \

    if response_by_id is None:
        return couldnt_be_found("Response")

    return response_by_id.to_dict_with_user()

# -------------- UPDATE A RESPONSE -------------- #

@response_routes.route('/<int:response_id>', methods=["PUT"])
@login_required
def update_response_by_id(response_id):
    response_by_id = Response.query.get(response_id)

    if response_by_id is None:
        return couldnt_be_found("Response")

    if response_by_id.user_id != current_user.id:
        return forbidden()

    form = ResponseForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        form_data = form.data
        response_by_id.response = form_data["response"]
        db.session.commit()

        return response_by_id.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# -------------- DELETE A RESPONSE -------------- #

@response_routes.route('/<int:response_id>', methods=["DELETE"])
@login_required
def delete_response_by_id(response_id):
    response_by_id = Response.query.get(response_id)

    if response_by_id is None:
        return couldnt_be_found("Response")

    if response_by_id.user_id != current_user.id:
        return forbidden()

    db.session.delete(response_by_id)
    db.session.commit()

    return deleted()