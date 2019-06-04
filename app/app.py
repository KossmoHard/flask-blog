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
mail = Mail(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


### Flask Login ###

login_manager = LoginManager()

### Flask-security ###
from users.models import *

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
