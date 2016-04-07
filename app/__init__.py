from flask import Flask, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import flask_login as login
import flask_admin as admin
from flask_login import LoginManager
from flask_admin.contrib import sqla
from flask_admin import helpers, expose

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
from app.forms import LoginForm


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
        return login.current_user.is_authenticated


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
admin_panel.add_view(MyModelView(models.User, db.session))
admin_panel.add_view(MyModelView(models.Hostel, db.session))
admin_panel.add_view(MyModelView(models.Room, db.session))
admin_panel.add_view(MyModelView(models.Person, db.session))
admin_panel.add_view(MyModelView(models.Post, db.session))
admin_panel.add_view(MyModelView(models.Temperature, db.session))


if __name__ == '__main__':
    app.run(debug=True)
