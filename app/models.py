from app import db, app
import sys


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

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
    def __unicode__(self):
        return self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)


class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    adress = db.Column(db.String(140))
    rooms = db.relationship('Room', backref='hostel', lazy='dynamic')

    def __str__(self):
        return str(self.number)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer)
    numbers_of_person = db.Column(db.Integer())
    floor = db.Column(db.Integer)
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
    person = db.relationship('Person', backref='room', lazy='dynamic')


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    department = db.Column(db.String(50))
    group = db.Column(db.Integer)
    form_of_education = db.Column(db.String(255))
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
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
    note = db.Column(db.String(255))

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.birthday

    def __init__(self, first_name=None, last_name=None, department=None, group=None, birthday=None, phone_number=None,
                 middle_name=None, form_of_education=None, hostel_id=None, room_id=None, passport=None, parents=None,
                 index=None, region=None, district=None, street=None, settlement=None, phone_number_parent=None,
                 note=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.department = department
        self.group = group
        self.form_of_education = form_of_education
        self.hostel_id = hostel_id
        self.room_id = room_id
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


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    department = db.Column(db.String(50))
    group = db.Column(db.Integer)
    form_of_education = db.Column(db.String(255))
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
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
    note = db.Column(db.String(255))

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.birthday

    def __init__(self, first_name=None, last_name=None, department=None, group=None, birthday=None, phone_number=None,
                 middle_name=None, form_of_education=None,  passport=None, parents=None,
                 index=None, region=None, district=None, street=None, settlement=None, phone_number_parent=None,
                 note=None):
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
    date = db.Column(db.Date, unique=True)
    temperature = db.Column(db.Integer)
