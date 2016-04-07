from app import db


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
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'))
    person = db.relationship('Person', backref='room', lazy='dynamic')

    def __str__(self):
        # костыль
        if self.hostel_id == 1:
            hostel = 4
        elif self.hostel_id == 2:
            hostel = 3
        return str(hostel) + '_' + str(self.room_number)


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

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __init__(self, first_name, last_name, department, group, birthday, speciality, p_series, p_number,
                 date_of_issue, issue, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.group = group
        self.birthday = birthday
        self.speciality = speciality
        self.p_series = p_series
        self.p_number = p_number
        self.date_of_issue = date_of_issue
        self.issue = issue
        self.phone_number = phone_number


class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=True)
    temperature = db.Column(db.Integer)
