from flask import render_template, flash, redirect, url_for, request, abort, g
from sqlalchemy import desc, asc
from flask_login import login_user, logout_user, current_user, login_required

from app import app, models, db, forms

NORMAL_T = 25


@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.order_by(desc(models.Post.timestamp)).limit(100).all()
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = models.User.query.filter_by(login=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout/')
def logout_view():
    logout_user()
    return redirect(url_for('index'))


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
        #     persons = models.Person.query.filter_by(hostel_id=form2.hostel_id.data, room_id=form2.room_id.data).all()
        #     places = models.Room.query.filter_by(hostel_id=form2.hostel_id.data, room_number=form2.room_id.data).first()
        #     return render_template('room_view.html', persons=persons, places=places)
        elif request.form['button'] == 'firstS':
            kwargs = {form.radio.data: form.value.data}
            search_result = models.Person.query.filter_by(**kwargs).all()
            return render_template('search_person.html', result=search_result)


@app.route('/hostels/<hostel>')
def hostel_detail(hostel):
    _rooms = models.Room.query.filter_by(hostel_id=hostel).all()
    floors = models.Room.query.order_by(models.Room.floor).filter_by(hostel_id=hostel).group_by(models.Room.floor).all()
    persons = models.Person.query.filter_by(hostel_id=hostel).all()
    return render_template('hostel_view.html', rooms=_rooms, floors=floors, persons=persons)


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
    persons = models.Person.query.filter_by(hostel_id=hostel, room_id=room).all()
    places = models.Room.query.filter_by(hostel_id=hostel, room_number=room).first()
    if places is not None:
        return render_template('room_view.html', persons=persons, places=places)
    else:
        abort(404)


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
    buffer = []
    values = models.Temperature.query.order_by(asc(models.Temperature.date)).limit(31).all()
    for value in values:
        buffer.append({"date": value.date.strftime('%Y-%m-%d'), "temperature": value.temperature})
    return render_template('plot.html', values=buffer, NORMAL_T=NORMAL_T)


@app.route('/person/<id>')
def person(id):
    person_ = models.Person.query.filter_by(id=id).first()
    return render_template('person.html', person=person_)


@app.route('/stat')
def stat():
    free_1 = 0
    free_2 = 0
    free_3 = 0
    free_4 = 0
    places_all = models.Room.query.all()
    places2 = models.Room.query.filter_by(hostel_id=2).all()
    places3 = models.Room.query.filter_by(hostel_id=3).all()
    places4 = models.Room.query.filter_by(hostel_id=4).all()
    for places in places_all:
        person_buffer = models.Person.query.filter_by(hostel_id=places.hostel_id, room_id=places.room_number).all()
        room_buffer = models.Room.query.filter_by(hostel_id=places.hostel_id, room_number=places.room_number).first()
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

    stats = {'Всего комнат': len(places_all), 'Всего комнат в 2 общежитии': len(places2),
             'Всего комнат в 3 общежитии': len(places3), 'Всего комнат в 4 общежитии': len(places4)}
    return render_template('stat.html', stats=stats, free_1=free_1, free_2=free_2, free_3=free_3, free_4=free_4)
