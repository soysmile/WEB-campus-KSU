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
    previewtext = db.Column(db.String(50))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    path = db.Column(db.String(255))

    def __init__(self, id=None, title=None, body=None, timestamp=None, path=None):
        self.title = title
        self.body = body
        self.path = path

        # Одна батарейка, що була викинута...


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
    econom = db.Column(db.Boolean)
    block_id = db.Column(db.Integer, db.ForeignKey('block.id'))
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
    person = db.relationship('Person', backref='person_room', lazy='dynamic')
    register = db.relationship('Register', backref='register_room', lazy='dynamic')
    free_places_id = db.relationship('Room_free', backref='room_free', lazy='dynamic')

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
    repair = db.relationship('Repair', backref='person_repair', lazy='dynamic')

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

    def set_invite(self):
        self.invite = str(uuid4())

        # def __init__(self):
        #     self.set_invite()


class Register_main(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(25))
    reason = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    birthday = db.Column(db.Date)
    department = db.Column(db.String(50))
    specialty = db.Column(db.String(50))
    group = db.Column(db.String(50))
    work = db.Column(db.String(50))
    s_passport = db.Column(db.String(50))
    n_passport = db.Column(db.String(50))
    d_passport = db.Column(db.Date)
    k_passport = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    lived_hostel = db.Column(db.String(50))
    lived_room = db.Column(db.String(50))
    form_of_education = db.Column(db.String(50))
    register_family = db.relationship('Register_family', backref='register_family', lazy='dynamic')
    register_student = db.relationship('Register_student', backref='register_student', lazy='dynamic')

    def __init__(self, room_type, reason, first_name, last_name, middle_name, birthday, department, specialty, group,
                 work, s_passport, n_passport, d_passport, k_passport, phone_number, lived_hostel, lived_room,
                 form_of_education):
        self.room_type = room_type
        self.reason = reason
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.department = department
        self.specialty = specialty
        self.group = group
        self.work = work
        self.s_passport = s_passport
        self.n_passport = n_passport
        self.d_passport = d_passport
        self.k_passport = k_passport
        self.phone_number = phone_number
        self.lived_hostel = lived_hostel
        self.lived_room = lived_room
        self.form_of_education = form_of_education


class Register_student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    register_id = db.Column(db.Integer, db.ForeignKey('register_main.id'))
    father = db.Column(db.String(255))
    father_work = db.Column(db.String(255))
    mother = db.Column(db.String(255))
    mother_work = db.Column(db.String(255))
    brothers_sisters = db.Column(db.String(255))
    parents_street = db.Column(db.String(255))
    parents_home = db.Column(db.String(255))
    parents_apartment = db.Column(db.String(255))
    parents_settlement = db.Column(db.String(255))
    parents_district = db.Column(db.String(255))
    parents_region = db.Column(db.String(255))
    parents_index = db.Column(db.Integer)
    parents_landline_phone = db.Column(db.String(255))
    parents_mobile_phone = db.Column(db.String(255))

    def __init__(self, register_id, father, father_work, mother, mother_work, brothers_sisters, parents_street,
                 parents_home, parents_apartment, parents_settlement, parents_district, parents_region, parents_index,
                 parents_landline_phone, parents_mobile_phone):
        self.register_id = register_id
        self.father = father
        self.father_work = father_work
        self.mother = mother
        self.mother_work = mother_work
        self.brothers_sisters = brothers_sisters
        self.parents_street = parents_street
        self.parents_home = parents_home
        self.parents_apartment = parents_apartment
        self.parents_settlement = parents_settlement
        self.parents_district = parents_district
        self.parents_region = parents_region
        self.parents_index = parents_index
        self.parents_landline_phone = parents_landline_phone
        self.parents_mobile_phone = parents_mobile_phone


class Register_family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    register_id = db.Column(db.Integer, db.ForeignKey('register_main.id'))
    husband_wife = db.Column(db.String(255))
    husband_wife_work = db.Column(db.String(255))
    husband_wife_birthday = db.Column(db.Date)
    husband_wife_s_passport = db.Column(db.String(255))
    husband_wife_n_passport = db.Column(db.Integer)
    husband_wife_d_passport = db.Column(db.Date)
    husband_wife_k_passport = db.Column(db.String(255))
    husband_wife_form_of_education = db.Column(db.String(255))
    husband_wife_lived = db.Column(db.String(255))
    husband_wife_lived_hostel = db.Column(db.String(255))
    husband_wife_lived_room = db.Column(db.String(255))
    childrens = db.Column(db.String(255))
    children_live = db.Column(db.Boolean)

    def __init__(self, register_id, husband_wife, husband_wife_work, husband_wife_birthday, husband_wife_s_passport,
                 husband_wife_n_passport, husband_wife_d_passport, husband_wife_k_passport,
                 husband_wife_form_of_education, husband_wife_lived, husband_wife_lived_hostel, husband_wife_lived_room,
                 childrens, children_live):
        self.register_id = register_id
        self.husband_wife = husband_wife
        self.husband_wife_work = husband_wife_work
        self.husband_wife_birthday = husband_wife_birthday
        self.husband_wife_s_passport = husband_wife_s_passport
        self.husband_wife_n_passport = husband_wife_n_passport
        self.husband_wife_d_passport = husband_wife_d_passport
        self.husband_wife_k_passport = husband_wife_k_passport
        self.husband_wife_form_of_education = husband_wife_form_of_education
        self.husband_wife_lived = husband_wife_lived
        self.husband_wife_lived_hostel = husband_wife_lived_hostel
        self.husband_wife_lived_room = husband_wife_lived_room
        self.childrens = childrens
        self.children_live = children_live


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


class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    open_date = db.Column(db.Date)
    description = db.Column(db.String(255))
    tag = db.Column(db.String(255))
    fix = db.Column(db.Boolean)
    close_date = db.Column(db.Date)
    person = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, description=None, tag=None, person=None):
        self.open_date = datetime.datetime.now()
        self.description = description
        self.tag = tag
        self.fix = False
        self.person = person


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    path = db.Column(db.String(255), unique=True)


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


@event.listens_for(Repair, 'before_update')
def after_update(*args):
    if args[2].fix:
        args[2].close_date = datetime.datetime.now()


class Room_free(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.Integer)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

    def __init__(self, places=None, room_id=None):
        self.places = places
        self.room_id = room_id


class Video_slider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime)
    url = db.Column(db.String(255))
    active = db.Column(db.Boolean)
