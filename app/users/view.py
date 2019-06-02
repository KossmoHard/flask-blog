from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)

from app import db
from .models import User, Role


users = Blueprint('users', __name__, template_folder='templates')


# @users.route('/login')
# def index():
#     return render_template('user/login.html')

