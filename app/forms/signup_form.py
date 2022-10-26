from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists, Length(8, 40)])
    email = StringField('email', validators=[DataRequired(), user_exists])
    first_name = StringField('first name', validators=[DataRequired(), Length(1, 50)])
    last_name = StringField('last name', validators=[DataRequired(), Length(1, 50)])
    about = StringField('about', validators=[Length(0, 200)])
    password = StringField('password', validators=[DataRequired()])
