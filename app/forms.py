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
    room_type = fields.RadioField('Тип комнаты', choices=[('place', 'Место в комнате'), ('room', 'Отдельную комнату'),
                                                          ('family', 'Семейную комнату')],
                                  default='place')
    reason = fields.TextAreaField('Причина')

    first_name = fields.StringField('Имя', validators=[validators.required()])
    last_name = fields.StringField('Фамилия', validators=[validators.required()])
    middle_name = fields.StringField('Отчество', validators=[validators.required()])
    birthday = fields.DateField('Дата рождения', validators=[validators.required()])
    department = fields.StringField('Факультет')
    specialty = fields.StringField('Специальность')
    group = fields.IntegerField('Группа')
    work = fields.StringField('Место работы и должность')
    s_passport = fields.StringField('Серия паспорта', validators=[validators.required()])
    n_passport = fields.StringField('Номер паспорта', validators=[validators.required()])
    d_passport = fields.DateField('Дата выдачи', validators=[validators.required()])
    k_passport = fields.StringField('Кем выдан', validators=[validators.required()])
    phone_number = fields.StringField('Контактные номера телефонов', validators=[validators.required()])
    email = fields.StringField('Электронная почта')

    lived_radio = fields.RadioField('Жил ли раньше в общежитиии',
                                    choices=[('lived', 'Раньше жил'), ('nolived', 'Не жил')],
                                    default='nolived')
    lived_hostel = fields.StringField('В общежитии')
    lived_room = fields.StringField('В комнате')

    form_of_education = fields.RadioField('Форма обучения', choices=[('b', 'Бюджет'), ('k', 'Контракт')], default='b')

    family_radio = fields.RadioField('Семейный студент?',
                                     choices=[('y', 'Да'), ('n', 'Нет'), ('o', 'Ничего из перечисленного')],
                                     default='o')
    father = fields.StringField('Отец')
    father_work = fields.StringField('Место работы')
    mother = fields.StringField('Мать')
    mother_work = fields.StringField('Место работы')
    brothers_sisters = fields.TextAreaField('Братья и сестры до 16 (указать возраст)')
    parents_street = fields.StringField('Улица')
    parents_home = fields.StringField('Дом')
    parents_apartment = fields.StringField('Квартира')
    parents_settlement = fields.StringField('Город/село')
    parents_district = fields.StringField('Район')
    parents_region = fields.StringField('Область')
    parents_index = fields.StringField('Индекс')
    parents_landline_phone = fields.StringField('Стационарный телефон')
    parents_mobile_phone = fields.StringField('Мобильный телефон')

    husband_wife = fields.StringField('Муж/жена')
    husband_wife_work = fields.StringField('Место работы')
    husband_wife_birthday = fields.DateField('Дата рождения', validators=[validators.Optional()])
    husband_wife_s_passport = fields.StringField('Серия паспорта')
    husband_wife_n_passport = fields.StringField('Номер паспорта')
    husband_wife_d_passport = fields.DateField('Дата выдачи', validators=[validators.Optional()])
    husband_wife_k_passport = fields.StringField('Кем выдан')
    husband_wife_form_of_education = fields.RadioField('Форма обучения (для студентов ХГУ)',
                                                       choices=[('b', 'Бюджет'), ('k', 'Контракт')], default='b')
    husband_wife_lived = fields.RadioField('Жил ли раньше в общежитиии',
                                           choices=[('lived', 'Раньше жил'), ('nolived', 'Не жил')],
                                           default='nolived')
    husband_wife_lived_hostel = fields.StringField('В общежитии')
    husband_wife_lived_room = fields.StringField('В комнате')
    childrens = fields.TextAreaField('Дети(с указанием даты рождения)')
    children_live = fields.RadioField('Ребёнок будет жить в общежитии', choices=[('y', 'Да'), ('n', 'Нет')],
                                      default='n')


class SearchForm(form.Form):
    value = fields.StringField()
    radio = fields.RadioField(choices=[('first_name', 'Имя'), ('last_name', 'Фамилия')], default='first_name')


class SearchForm2(form.Form):
    hostel_id = fields.IntegerField()
    room_id = fields.IntegerField()
