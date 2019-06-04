from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired, length
from models import Tag


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired("Please enter title.")])
    description = TextAreaField('Description', validators=[DataRequired(), length(min=20)])
    tags = QuerySelectMultipleField('Tags', query_factory=lambda: Tag.query.all())


class TagForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
