from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views, models

admin = Admin(app)
admin.add_view(ModelView(models.Post, db.session))
admin.add_view(ModelView(models.Hostel, db.session))
admin.add_view(ModelView(models.Room, db.session))
admin.add_view(ModelView(models.Person, db.session))
admin.add_view(ModelView(models.Temperature, db.session))
