from app import db, login_manager
from datetime import datetime


class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(10))
    email = db.Column('email', db.String(50), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)


class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String(140))
    rooms = db.relationship('Room', backref='hostel', lazy='dynamic')


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numbers_of_person = db.Column(db.Integer())
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
    person = db.relationship('Person', backref='room', lazy='dynamic')


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    department = db.Column(db.String(50))
    group = db.Column(db.Integer)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    birthday = db.Column(db.Date)
    speciality = db.Column(db.String(30))
    p_series = db.Column(db.String(2))
    p_number = db.Column(db.Integer)
    date_of_issue = db.Column(db.Date)
    issue = db.Column(db.String(50))
    phone_number = db.Column(db.Integer)


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    temperature = db.Column(db.Integer)
