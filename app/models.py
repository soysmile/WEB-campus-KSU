# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import event
import datetime
from uuid import uuid4
from flask_security import UserMixin, RoleMixin
from flask import flash

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), unique=True)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, first_name=None, last_name=None, login=None, email=None, password=None, person_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.email = email
        self.password = password
        self.person_id = person_id

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __str__(self):
        return self.login


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, id=None, title=None, body=None, timestamp=None):
        print(id, title, body, timestamp)
        self.title = title
        self.body = body


class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    address = db.Column(db.String(140))
    blocks = db.relationship('Block', backref='hostel', lazy='dynamic')
    rooms = db.relationship('Room', backref='hostel', lazy='dynamic')
    washings = db.relationship('Washing', backref='hostel_washing', lazy='dynamic')

    def __str__(self):
        return str(self.number)


class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
    number = db.Column(db.String(50))
    hot_water = db.Column(db.Boolean)
    rooms = db.relationship('Room', backref='block', lazy='dynamic')
    floor = db.Column(db.Integer)
    sex = db.Column(db.String(2))

    def __str__(self):
        return str(Hostel.query.filter_by(id=self.hostel_id).first().number) + '_' + str(self.number)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer)
    note = db.Column(db.String(30))
    numbers_of_person = db.Column(db.Integer)
    floor = db.Column(db.Integer)
    windows = db.Column(db.Boolean)
    service = db.Column(db.Boolean)
    block_id = db.Column(db.Integer, db.ForeignKey('block.id'))
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
    person = db.relationship('Person', backref='person_room', lazy='dynamic')
    register = db.relationship('Register', backref='register_room', lazy='dynamic')

    def __str__(self):
        hostel_number = Hostel.query.filter_by(id=self.hostel.id).first().number
        return str(hostel_number) + '_' + str(self.room_number)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    department = db.Column(db.String(50))
    group = db.Column(db.Integer)
    form_of_education = db.Column(db.String(255))
    hostel_id = db.Column(db.Integer)
    room_id = db.Column(db.Integer)
    birthday = db.Column(db.String(255))
    passport = db.Column(db.String(255))
    parents = db.Column(db.String(255))
    index = db.Column(db.Integer)
    region = db.Column(db.String(255))
    district = db.Column(db.String(255))
    settlement = db.Column(db.String(255))
    street = db.Column(db.String(255))
    phone_number_parent = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    note = db.Column(db.String(255))
    email = db.Column(db.String(255))
    invite = db.Column(db.String(255), index=True, default=str(uuid4()))
    room = db.Column(db.Integer, db.ForeignKey('room.id'))
    user = db.relationship('User', backref='person_user', lazy='dynamic')
    payment = db.relationship('Payment', backref='person_payment', lazy='dynamic')
    work = db.relationship('Work', backref='person_work', lazy='dynamic')
    washing = db.relationship('Washing', backref='person_washing', lazy='dynamic')
    violation = db.relationship('Violation', backref='person_violation', lazy='dynamic')

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def set_invite(self):
        self.invite = str(uuid4())

        # def __init__(self):
        #     self.set_invite()


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    department = db.Column(db.String(50))
    group = db.Column(db.Integer)
    form_of_education = db.Column(db.String(255))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    birthday = db.Column(db.String(255))
    passport = db.Column(db.String(255))
    parents = db.Column(db.String(255))
    index = db.Column(db.Integer)
    region = db.Column(db.String(255))
    district = db.Column(db.String(255))
    settlement = db.Column(db.String(255))
    street = db.Column(db.String(255))
    phone_number_parent = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    email = db.Column(db.String(255))
    note = db.Column(db.String(255))

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.birthday

    def __init__(self, first_name=None, last_name=None, middle_name=None, department=None, group=None,
                 form_of_education=None, birthday=None, passport=None, parents=None, index=None, region=None,
                 district=None, settlement=None, street=None, phone_number=None, phone_number_parent=None, note=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.department = department
        self.group = group
        self.form_of_education = form_of_education
        self.birthday = birthday
        self.passport = passport
        self.parents = parents
        self.index = index
        self.region = region
        self.district = district
        self.settlement = settlement
        self.street = street
        self.phone_number_parent = phone_number_parent
        self.phone_number = phone_number
        self.note = note


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    temperature = db.Column(db.Float)
    hostel_id = db.Column(db.Integer)

    def __init__(self, date=None, temperature=None, hostel_id=None):
        self.date = date
        self.temperature = temperature
        self.hostel_id = hostel_id


class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    places_all = db.Column(db.Integer)  # Всего комнат в общежитиях
    places2 = db.Column(db.Integer)  # Всего комнат во 2 общежитии
    places3 = db.Column(db.Integer)  # Всего комнат в 3 общежитии
    places4 = db.Column(db.Integer)  # Всего комнат в 4 общежитии
    free_1 = db.Column(db.Integer)  # Одна свободная комната
    free_2 = db.Column(db.Integer)  # Две свободных комнат
    free_3 = db.Column(db.Integer)  # Три свободных комнат
    free_4 = db.Column(db.Integer)  # Четыре свободные комнаты

    def __init__(self, date=None, places_all=None, places2=None, places3=None, places4=None, free1=None, free2=None,
                 free3=None, free4=None):
        self.date = date
        self.places_all = places_all
        self.places2 = places2
        self.places3 = places3
        self.places4 = places4
        self.free_1 = free1
        self.free_2 = free2
        self.free_3 = free3
        self.free_4 = free4


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    price = db.Column(db.Float)
    person = db.Column(db.Integer, db.ForeignKey('person.id'))


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    person = db.Column(db.Integer, db.ForeignKey('person.id'))


class Washing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    person = db.Column(db.Integer, db.ForeignKey('person.id'))
    hostel = db.Column(db.Integer, db.ForeignKey('hostel.id'))


class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(255))
    person = db.Column(db.Integer, db.ForeignKey('person.id'))


@event.listens_for(Person, 'before_insert')
def before_insert(*args):
    if args[2].room:
        room = Room.query.filter_by(id=args[2].room).first()
        if room.numbers_of_person < len(Person.query.filter_by(room=args[2].room).all()) + 1:
            flash('В этой комнате уже проживает %s жильцов. Комната не установлена' % room.numbers_of_person)
            args[2].room = None
            raise BufferError


@event.listens_for(Person, 'after_insert')
def after_insert(*args):
    if args[2].email and args[2].room:
        from app import mail
        from flask_mail import Message
        from config import MAIL_DEFAULT_SENDER
        print(args[2].first_name, args[2].room, args[2].invite)
        msg = Message('Поселення', sender=MAIL_DEFAULT_SENDER, recipients=[args[2].email])
        msg.html = """<b>Привіт, {0}!</b><br/>
        Вітаємо, твоя кімната для проживання <b>{1}</b><br/>
        Для активації особистого кабінету на сайті перейди за <a href='ksu-hostel.herokuapp.com/{2}'>посиланням</a>""".format(
            args[2].first_name, args[2].room, args[2].invite)
        mail.send(msg)


@event.listens_for(Register, 'before_update')
def before_update(*args):
    if args[2].room_id:
        session = db.create_scoped_session()
        p = Person(last_name=args[2].last_name,
                   first_name=args[2].first_name,
                   middle_name=args[2].middle_name,
                   department=args[2].department,
                   group=args[2].group,
                   form_of_education=args[2].form_of_education,
                   birthday=args[2].birthday,
                   passport=args[2].passport,
                   parents=args[2].parents,
                   index=args[2].index,
                   region=args[2].region,
                   district=args[2].district,
                   settlement=args[2].settlement,
                   street=args[2].street,
                   phone_number_parent=args[2].phone_number_parent,
                   phone_number=args[2].phone_number,
                   note=args[2].note,
                   email=args[2].email,
                   room=args[2].room_id)
        try:
            session.add(p)
            session.commit()
        except BufferError:
            args[2].room_id = None


@event.listens_for(Register, 'after_update')
def after_update(*args):
    Register.query.filter_by(id=args[2].id).delete()
