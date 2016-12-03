# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request, abort
from sqlalchemy import desc, asc
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime, timedelta
from app import app, models, db, forms
from uuid import uuid4
from flask_mobility.decorators import mobile_template

NORMAL_T = 25


@mobile_template('{mobile/}index.html')
@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.order_by(desc(models.Post.timestamp)).limit(100).all()
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    registered_user = models.User.query.filter_by(login=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('index'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout/')
def logout_view():
    logout_user()
    return redirect(url_for('index'))


@app.route('/registration', methods=['POST'])
def invite_reg():
    person = models.Person.query.filter_by(invite=request.form['invite']).first()
    if person:
        return render_template('reg_user.html', user=person)
    else:
        return abort(404)


@app.route('/add_user', methods=['POST'])
def add_user():
    person = models.Person.query.filter_by(id=request.form['id']).first()
    login = request.form['login']
    email = request.form['email']
    password = request.form['password']
    db.session.add(models.User(login=login, email=email, password=password, person_id=person.id))
    db.session.commit()
    registered_user = models.User.query.filter_by(login=login, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('invite_reg'))
    login_user(registered_user)
    person.invite = None
    db.session.commit()
    flash('Logged in successfully')
    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    paypay = {'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0, 'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
              'Jul': 0, 'Aug': 0}
    person = models.Person.query.filter_by(id=current_user.person_id).first()
    payment = models.Payment.query.filter_by(person=person.id).all()
    for pay in payment:
        if pay.date.month == 9:
            paypay['Sep'] = 1
            paypay['Sep_price'] = pay.price
        elif pay.date.month == 10:
            paypay['Oct'] = 1
            paypay['Oct_price'] = pay.price
        elif pay.date.month == 11:
            paypay['Nov'] = 1
            paypay['Nov_price'] = pay.price
        elif pay.date.month == 12:
            paypay['Dec'] = 1
            paypay['Dec_price'] = pay.price
        elif pay.date.month == 1:
            paypay['Jan'] = 1
            paypay['Jan_price'] = pay.price
        elif pay.date.month == 2:
            paypay['Feb'] = 1
            paypay['Feb_price'] = pay.price
        elif pay.date.month == 3:
            paypay['Mar'] = 1
            paypay['Mar_price'] = pay.price
        elif pay.date.month == 4:
            paypay['Apr'] = 1
            paypay['Apr_price'] = pay.price
        elif pay.date.month == 5:
            paypay['May'] = 1
            paypay['May_price'] = pay.price
        elif pay.date.month == 6:
            paypay['Jun'] = 1
            paypay['Jun_price'] = pay.price
        elif pay.date.month == 7:
            paypay['Jul'] = 1
            paypay['Jul_price'] = pay.price
        elif pay.date.month == 8:
            paypay['Aug'] = 1
            paypay['Aug_price'] = pay.price

    work = models.Work.query.filter_by(person=person.id).all()
    hours = timedelta()
    for w in work:
        hours += w.end - w.start

    violations = models.Violation.query.filter_by(person=person.id).all()
    return render_template('profile.html', person=person, payment=paypay, hours=hours, work=work, violations=violations)


@login_required
@app.route('/washing', methods=['GET', 'POST'])
def washing():
    hostel_id = models.Room.query.filter_by(
        id=models.Person.query.filter_by(id=current_user.person_id).first().room).first().hostel_id
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=0, minute=0,
                     second=0, microsecond=1)
    end = start + timedelta(days=6 - start.weekday(), hours=23, minutes=59, seconds=59, microseconds=59)
    days = start.weekday()
    washing = models.Washing.query.filter(models.Washing.start > str(start)).filter(
        models.Washing.end < str(end)).filter(models.Washing.hostel == hostel_id).all()
    washing_ = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [],
                'Sunday': []}
    for wash in washing:
        washing_[wash.start.strftime("%A")].append([wash.start, wash.end, models.Person.query.filter_by(
            id=wash.person).first().last_name + ' ' + models.Person.query.filter_by(id=wash.person).first().first_name])
    return render_template('washing.html', washing=washing_, days=days, days_list=days_list)


@app.route('/post/<id>')
def detail_view_post(id):
    post = models.Post.query.filter_by(id=id).first()
    if post:
        return render_template('post.html', post=post)
    else:
        abort(404)


@app.route('/hostels', methods=['GET', 'POST'])
def rooms():
    form = forms.SearchForm(request.form)
    form2 = forms.SearchForm2(request.form)
    if request.method == 'GET':
        hostels = models.Hostel.query.all()
        return render_template('hostels.html', hostels=hostels, form=form, form2=form2)
    elif request.method == 'POST':
        if request.form['button'] == 'secondS':
            return redirect(url_for('room_detail', hostel=form2.hostel_id.data, room=form2.room_id.data))
        elif request.form['button'] == 'firstS':
            kwargs = {form.radio.data: form.value.data}
            search_result = models.Person.query.filter_by(**kwargs).all()
            return render_template('search_person.html', result=search_result)


@app.route('/hostels/<hostel>')
def hostel_detail(hostel):
    hostel_number = hostel
    hostel = models.Hostel.query.filter_by(number=hostel).first().id
    if int(hostel_number) == 2:
        _rooms = models.Room.query.filter_by(hostel_id=hostel).all()
        floors = models.Room.query.order_by(models.Room.floor).filter_by(hostel_id=hostel).group_by(
            models.Room.floor).all()
        return render_template('hostel_view.html', hostel_number=hostel_number, rooms=_rooms, floors=floors)
    else:
        blocks = models.Block.query.filter_by(hostel_id=hostel)
        floors = models.Block.query.order_by(models.Block.floor).filter_by(hostel_id=hostel).group_by(
            models.Block.floor).all()
    return render_template('blocks.html', hostel_number=hostel_number, blocks=blocks, floors=floors)


@app.route('/hostel/<hostel>/<block>')
def block_view(hostel, block):
    hostel_number = hostel
    block_number = block
    hostel_id = models.Hostel.query.filter_by(number=hostel).first().id
    block_id = models.Block.query.filter_by(number=block_number).first().id
    rooms = models.Room.query.filter_by(hostel_id=hostel_id, block_id=block_id).all()
    return render_template('block_view.html', hostel_number=hostel_number, rooms=rooms)


@app.route('/hostels/<hostel>/free')
def hostel_detail_free(hostel):
    places = models.Room.query.filter_by(hostel_id=hostel).all()
    places_free = []
    for place in places:
        person_buffer = models.Person.query.filter_by(hostel_id=hostel, room_id=place.room_number).all()
        room_buffer = models.Room.query.filter_by(hostel_id=hostel, room_number=place.room_number).first()
        if room_buffer.numbers_of_person is None:
            room_buffer.numbers_of_person = 0
        if int(room_buffer.numbers_of_person) - len(person_buffer) > 0:
            places_free.append(room_buffer)
    floors = models.Room.query.order_by(models.Room.floor).filter_by(hostel_id=hostel).group_by(models.Room.floor).all()

    return render_template('free.html', hostel=hostel, places_free=places_free, floors=floors)


@app.route('/rooms/<hostel>/<room>')
def room_detail(hostel, room):
    hostel_number = hostel
    hostel = models.Hostel.query.filter_by(number=hostel).first().id
    room = models.Room.query.filter_by(hostel_id=hostel, room_number=room).first().id
    persons = models.Person.query.filter_by(room=room).all()
    places = models.Room.query.filter_by(hostel_id=hostel, id=room).first()
    if places is not None:
        return render_template('room_view.html', hostel_number=hostel_number, persons=persons, places=places)
    else:
        abort(404)


@app.route('/fix')
def fix():
    persons = models.Person.query.all()
    for person in persons:
        room = models.Room.query.filter_by(hostel_id=person.hostel_id, id=person.room_id).first().id
        person.invite = str(uuid4())
        db.session.commit()
    return 'ok'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        person = models.Register(form.first_name.data, form.last_name.data, form.middle_name.data, form.department.data,
                                 form.group.data, form.form_of_education.data, form.birthday.data, form.passport.data,
                                 form.parents.data, form.index.data, form.region.data, form.district.data,
                                 form.settlement.data, form.street.data, form.phone_number.data,
                                 form.phone_number_parent.data, form.note.data)
        db.session.add(person)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/plot')
def plot():
    buffer2 = []
    buffer3 = []
    buffer4 = []
    values2 = models.Temperature.query.filter_by(hostel_id=2).order_by(asc(models.Temperature.date)).all()
    values3 = models.Temperature.query.filter_by(hostel_id=3).order_by(asc(models.Temperature.date)).all()
    values4 = models.Temperature.query.filter_by(hostel_id=4).order_by(asc(models.Temperature.date)).all()
    for value in values2:
        buffer2.append({"date": value.date.strftime('%Y-%m-%d'), "temperature": value.temperature})

    for value in values3:
        buffer3.append({"date": value.date.strftime('%Y-%m-%d'), "temperature": value.temperature})

    for value in values4:
        buffer4.append({"date": value.date.strftime('%Y-%m-%d'), "temperature": value.temperature})

    return render_template('plot.html', values2=buffer2, values3=buffer3, values4=buffer4, NORMAL_T=NORMAL_T)


@app.route('/person/<id>')
def person(id):
    person_ = models.Person.query.filter_by(id=id).first()
    return render_template('person.html', person=person_)


@app.route('/stat', methods=['GET', 'POST'])
def stat():
    if request.method == 'POST':
        last = models.Statistics.query.order_by(desc(models.Statistics.date)).first()
        if last.date == datetime.date(datetime.now()):
            flash('Сегодя уже было обновление!')
            return redirect('stat')
        else:
            free_1 = 0
            free_2 = 0
            free_3 = 0
            free_4 = 0
            places_all = models.Room.query.all()
            places2 = models.Room.query.filter_by(hostel_id=2).all()
            places3 = models.Room.query.filter_by(hostel_id=3).all()
            places4 = models.Room.query.filter_by(hostel_id=4).all()
            for places in places_all:
                person_buffer = models.Person.query.filter_by(hostel_id=places.hostel_id,
                                                              room_id=places.room_number).all()
                room_buffer = models.Room.query.filter_by(hostel_id=places.hostel_id,
                                                          room_number=places.room_number).first()
                if room_buffer.numbers_of_person is None:
                    room_buffer.numbers_of_person = 0
                if int(room_buffer.numbers_of_person) - len(person_buffer) == 1:
                    free_1 += 1
                elif int(room_buffer.numbers_of_person) - len(person_buffer) == 2:
                    free_2 += 1
                elif int(room_buffer.numbers_of_person) - len(person_buffer) == 3:
                    free_3 += 1
                elif int(room_buffer.numbers_of_person) - len(person_buffer) == 4:
                    free_4 += 1
            stats = models.Statistics(datetime.date(datetime.now()), len(places_all), len(places2), len(places3),
                                      len(places3), free_1, free_2, free_3, free_4)
            db.session.add(stats)
            db.session.commit()
            return redirect('stat')
    elif request.method == 'GET':
        stats = models.Statistics.query.order_by(desc(models.Statistics.date)).first()
        return render_template('stat.html', stats=stats)


@app.route('/future/hostels/<hostel>')
def future_hostel_query(hostel):
    return hostel

# TODO: графическое представление. Canvas or png.
