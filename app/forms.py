# -*- coding: utf-8 -*-

from wtforms import form, fields, validators
from app import db, models


class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(models.User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    first_name = fields.StringField(validators=[validators.required()])
    last_name = fields.StringField(validators=[validators.required()])
    middle_name = fields.StringField(validators=[validators.required()])
    department = fields.StringField(validators=[validators.required()])
    group = fields.IntegerField(validators=[validators.required()])
    form_of_education = fields.StringField(validators=[validators.required()])
    birthday = fields.DateField(validators=[validators.required()])
    passport = fields.StringField(validators=[validators.required()])
    parents = fields.StringField(validators=[validators.required()])
    index = fields.IntegerField(validators=[validators.required()])
    region = fields.StringField(validators=[validators.required()])
    district = fields.StringField(validators=[validators.required()])
    settlement = fields.StringField(validators=[validators.required()])
    street = fields.StringField(validators=[validators.required()])
    phone_number = fields.StringField(validators=[validators.required()])
    phone_number_parent = fields.StringField(validators=[validators.required()])
    note = fields.StringField(validators=[validators.required()])


class SearchForm(form.Form):
    value = fields.StringField()
    radio = fields.RadioField(choices=[('first_name', 'Имя'), ('last_name', 'Фамилия')], default='first_name')


class SearchForm2(form.Form):
    hostel_id = fields.IntegerField()
    room_id = fields.IntegerField()
