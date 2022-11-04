from flask import Blueprint, request
from sqlalchemy.orm import joinedload
from flask_login import current_user, login_required

from app.models import db, Post, Response, Clap
from app.utils.error_messages import couldnt_be_found, forbidden, deleted
from app.api.auth_routes import validation_errors_to_error_messages
from app.forms.clap_form import ClapForm

clap_routes = Blueprint("clap", __name__)

# -------------- UPDATE A CLAP -------------- #
@clap_routes.route('/<int:clap_id>', methods=["PUT"])
@login_required
def update_clap_by_id(clap_id):
    clap_by_id = Clap.query.get(clap_id)

    if clap_by_id is None:
        return couldnt_be_found("Clap")

    if clap_by_id.user_id != current_user.id:
        return forbidden()

    form = ClapForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        form_data = form.data
        clap_by_id.amount = form_data["amount"]
        db.session.commit()

        clap_by_id_dict = clap_by_id.to_dict()
        clap_by_id_dict["user"] = current_user.to_dict()
        del clap_by_id_dict["userId"]

        return clap_by_id_dict

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400