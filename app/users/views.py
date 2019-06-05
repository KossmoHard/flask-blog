from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

from app import db
from .models import User, Role
from .forms import LoginForm, RegistrationForm

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:
        form = LoginForm()
        error = None
        email = form.email.data
        password = form.password.data

        if request.method == 'POST' and form.validate():
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                if login_user(user):
                    return redirect(url_for('posts.index'))
            error = 'Invalid username or password.'

        return render_template('users/login.html', form=form, error=error)
    else:
        return redirect(url_for('posts.admin_panel'))


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('posts.index'))


@users.route('/register', methods=['GET', 'POST'])
def registration():
    if not current_user.is_authenticated:
        form = RegistrationForm()
        error = None
        if request.method == 'POST' and form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if not user:
                new_user = User(email=email, username=username, password=generate_password_hash(password))
                db.session.add(new_user)
                db.session.commit()

                return redirect(url_for('users.login'))
            error = "User with this login or email already exists"

        return render_template('users/registration.html', form=form, error=error)
    else:
        return redirect(url_for('posts.admin_panel'))
