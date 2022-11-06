from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange

class ClapForm(FlaskForm):
    amount = IntegerField('amount', validators=[DataRequired(), NumberRange(1, 50)])