# -*- coding: utf-8 -*-

import flask_admin as admin
import flask_login as login
from flask import Flask, url_for, redirect, request, abort
from flask_admin import helpers, expose
from flask_admin.contrib import sqla
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_security import current_user, login_required, RoleMixin, Security, SQLAlchemyUserDatastore, UserMixin, utils
from flask.ext.mobility import Mobility

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mail = Mail(app)
Mobility(app)

from app import views, models
from app.forms import LoginForm

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


# Create customized model view class
class MyModelView(sqla.ModelView):
    def is_accessible(self):
        if login.current_user.is_authenticated:
            return login.current_user.has_role('admin')


class MyPersonView(MyModelView):
    """Just for test"""
    column_exclude_list = ('id', 'parents', 'index', 'note', 'invite', 'phone_number_parent', 'street', 'passport')
    column_searchable_list = ('first_name', 'last_name')
    edit_modal = True
    create_modal = True
    can_export = True
    column_editable_list = ['first_name', 'last_name']
    # column_labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'middle_name': 'Отчество'}


class MyTemperatureView(MyModelView):
    can_export = True


class MyRoomView(MyModelView):
    column_editable_list = ['econom', 'service', 'windows']


# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Initialize flask-login
init_login()

# Create admin
admin_panel = admin.Admin(app, 'Admin', index_view=MyAdminIndexView(), base_template='my_master.html')
# admin_panel.add_view(MyModelView(models.User, db.session, 'Пользователи'))
admin_panel.add_view(MyModelView(models.Hostel, db.session))
admin_panel.add_view(MyRoomView(models.Room, db.session))
admin_panel.add_view(MyPersonView(models.Person, db.session))
admin_panel.add_view(MyModelView(models.Post, db.session))
admin_panel.add_view(MyTemperatureView(models.Temperature, db.session))
admin_panel.add_view(MyModelView(models.Register, db.session))
admin_panel.add_view(MyModelView(models.Statistics, db.session))
admin_panel.add_view(MyModelView(models.Block, db.session))
admin_panel.add_view(MyModelView(models.Payment, db.session))
admin_panel.add_view(MyModelView(models.Work, db.session))
admin_panel.add_view(MyModelView(models.Washing, db.session))
admin_panel.add_view(MyModelView(models.Violation, db.session))
admin_panel.add_view(MyModelView(models.Role, db.session))
