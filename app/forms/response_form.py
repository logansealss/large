from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class ResponseForm(FlaskForm):
    response = StringField('title', validators=[DataRequired(), Length(1, 255)])