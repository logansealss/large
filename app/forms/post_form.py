from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Length

class CreatePostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(1, 100)])
    subtitle = StringField('subtitle', validators=[Length(0, 100)])
    image_url = StringField('image url', [Length(0, 255)])
    post = StringField('post', validators=[DataRequired()])

class UpdatePostForm(FlaskForm):
    title = StringField('title', validators=[Length(0, 100)])
    subtitle = StringField('subtitle', validators=[Length(0, 100)])
    image_url = StringField('image url', [Length(0, 255)])
    post = StringField('post')