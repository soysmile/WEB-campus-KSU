# -*- coding: utf-8 -*-


from flask import Flask
from flask import g
from flask_login import LoginManager
from flask_mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)
engine = create_engine('postgresql://postgres:root@localhost/hostel')
# engine = create_engine('postgresql://hostel:hostelsp@localhost/hostel')
db_session = scoped_session(sessionmaker(bind=engine))
db.create_all()

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
        g.user = db_session.query(models.User).get(user_id)
        return db_session.query(models.User).get(user_id)


init_login()

if __name__ == "__main__":
    app.run(debug=True)
