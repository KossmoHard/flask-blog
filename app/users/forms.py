from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators


class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=4, max=255)])


class RegistrationForm(FlaskForm):
    username = StringField('Login', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=4, max=255)])
