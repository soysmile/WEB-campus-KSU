# -*- coding: utf-8 -*-


from flask import Flask
from flask.ext.mobility import Mobility
from flask_login import LoginManager
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)

from app import views, models
from app.forms import LoginForm
from .admin import admin_panel




user_datastore = SQLAlchemyUserDatastore(db, models.User, models.User)
security = Security(app, user_datastore)

# Initialize flask-login

def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(models.User).get(user_id)
init_login()
