from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_security import SQLAlchemyUserDatastore, Security
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


### Flask Login ###

login_manager = LoginManager()
login_manager.init_app(app)

from users.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

