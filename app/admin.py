import os.path as op
from os import mkdir

import flask_admin as admin
import flask_login as login
from flask import url_for, redirect, request
from flask.ext.security import url_for_security
from flask_admin import form
from flask_admin import helpers, expose
from flask_admin.consts import ICON_TYPE_GLYPH
from flask_admin.contrib import sqla
from jinja2 import Markup
from wtforms import TextAreaField
from wtforms.widgets import TextArea

from app import models, db, app
from app.forms import LoginForm

file_path = op.join(op.dirname(__file__), 'static/files')
try:
    mkdir(file_path)
except OSError:
    pass


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


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


def get_current_user():
    from flask.ext.security import current_user
    try:
        return models.User.objects.get(id=current_user.id)
    except Exception as e:
        return current_user


def is_accessible(roles_accepted=None, user=None):
    user = user or get_current_user()
    if user.is_authenticated:
        if roles_accepted:
            accessible = any(
                [user.has_role(role) for role in roles_accepted]
            )
            return accessible
        return True


class Roled(object):
    def is_accessible(self):
        roles_accepted = getattr(self, 'roles_accepted', None)
        return is_accessible(roles_accepted=roles_accepted, user=login.current_user)

    def _handle_view(self, name, *args, **kwargs):
        if not login.current_user.is_authenticated:
            return redirect(url_for_security('login', next="/admin"))
        if not self.is_accessible():
            return "<p>Access denied</p>"


class MyModelView(Roled, sqla.ModelView):
    list_template = 'admin/list.html'
    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    def __init__(self, *args, **kwargs):
        self.roles_accepted = kwargs.pop('roles_accepted', list())
        super(MyModelView, self).__init__(*args, **kwargs)

        # def is_accessible(self):
        #     if login.current_user.is_authenticated:
        #         return login.current_user.has_role('admin')


class MyPersonView(MyModelView):
    """Just for test"""
    column_exclude_list = ('id', 'parents', 'index', 'note', 'invite', 'phone_number_parent', 'street', 'passport')
    column_searchable_list = ('first_name', 'last_name')
    edit_modal = True
    create_modal = True
    can_export = True
    export_types = ['xlsx']
    column_export_exclude_list = ['Person Room', 'person_room', 'person room']
    column_editable_list = ['first_name', 'last_name']
    column_labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'middle_name': 'Отчество'}


class MyPostView(MyModelView):
    form_overrides = dict(body=CKTextAreaField)

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s" height="180px">' % url_for('static', filename='files/' + form.thumbgen_filename(model.path)))

    def _body_slice(view, context, model, name):
        return model.body[:10]

    def _preview_slice(view, context, model, name):
        return model.previewtext[:10]

    column_formatters = {
        'path': _list_thumbnail,
        'body': _body_slice,
        'previewtext': _preview_slice
    }

    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=file_path,
                                      endpoint='static',
                                      thumbnail_size=(360, 240, True))
    }


class MyTemperatureView(MyModelView):
    can_export = True


class MyRepairView(MyModelView):
    column_editable_list = ['fix']


class MyRoomView(MyModelView):
    column_editable_list = ['econom', 'service', 'windows']


class MyNewsSliderView(MyModelView):
    form_overrides = dict(body=CKTextAreaField)

    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static', filename='files/' + form.thumbgen_filename(model.path)))

    def _body_slice(view, context, model, name):
        return model.body[:100]

    column_formatters = {
        'path': _list_thumbnail,
        'body': _body_slice
    }

    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=file_path,
                                      endpoint='static',
                                      thumbnail_size=(360, 240, True))
    }


admin_panel = admin.Admin(app, 'Студгородок ХДУ', index_view=MyAdminIndexView(), base_template='layout.html',
                          template_mode='bootstrap3')
admin_panel.add_view(MyModelView(models.User, db.session, name='Пользователи',  menu_icon_type=ICON_TYPE_GLYPH, menu_icon_value='glyphicon-user',roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Hostel, db.session, name='Общежития', menu_icon_type=ICON_TYPE_GLYPH, menu_icon_value='glyphicon-home', roles_accepted=['admin']))
admin_panel.add_view(MyRoomView(models.Room, db.session,  name='Комнаты', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Block, db.session, name='Блоки', roles_accepted=['admin']))
admin_panel.add_view(MyPersonView(models.Person, db.session, name='Жильцы', roles_accepted=['admin']))
admin_panel.add_view(MyTemperatureView(models.Temperature, db.session, name='Температура', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Statistics, db.session, name='Статистика', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Payment, db.session, name='Оплата', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Work, db.session, name='Отработки', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Washing, db.session, name='Стирка', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Violation, db.session, name='Нарушения', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Role, db.session, name='Роли', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Register_main, db.session, name='Заявки. Основное', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Register_student, db.session, name='Заявки. Студентны', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Register_family, db.session, name='Заявкию Семейные', roles_accepted=['admin']))
admin_panel.add_view(MyRepairView(models.Repair, db.session, name='Ремонт', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Room_free, db.session, name='Свободные комнаты', roles_accepted=['admin']))
admin_panel.add_view(MyModelView(models.Logger, db.session, name='Логи', roles_accepted=['admin']))
admin_panel.add_view(MyPostView(models.Post, db.session, name='Новости', roles_accepted=['admin', 'editor']))
admin_panel.add_view(MyModelView(models.Video_slider, db.session, name='Сладер видео', roles_accepted=['admin', 'editor']))
admin_panel.add_view(MyNewsSliderView(models.News_Slider, db.session, name='Слайдер новостей', roles_accepted=['admin', 'editor']))
