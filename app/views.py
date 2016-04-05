from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import desc, asc
from app import app, models, db
from datetime import date
from app import forms


@app.route('/')
@app.route('/index')
def index():
    # добавить пагинацию
    posts = models.Post.query.order_by(desc(models.Post.timestamp)).limit(100).all()
    return render_template('index.html', posts=posts)


@app.route('/post/<id>')
def detail_view_post(id):
    post = models.Post.query.filter_by(id=id).first()
    return render_template('post.html', post=post)


@app.route('/hostels', methods=['GET', 'POST'])
def rooms():
    hostels = models.Hostel.query.all()
    return render_template('hostels.html', hostels=hostels)


@app.route('/hostels/<hostel>')
def hostel_detail(hostel):
    rooms = models.Room.query.filter_by(hostel_id=hostel).all()
    return render_template('hostel_view.html', rooms=rooms)


@app.route('/rooms/<room>')
def room_detail(room):
    persons = models.Person.query.filter_by(room_id=room).all()
    return render_template('room_view.html', persons=persons)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        person = models.Person(form.first_name.data, form.last_name.data, form.department.data,
                               form.group.data, form.birthday.data, form.speciality.data,
                               form.p_series.data, form.p_number.data, form.date_of_issue.data,
                               form.issue.data, form.phone_number.data)
        print(person)
        db.session.add(person)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/user/<username>')
def user(username):
    user_ = models.User.query.filter_by(username=username).first()
    if user_ is None:
        flash('User %s not found.' % username)
        return redirect(url_for('index'))
    return render_template('profile.html', user=user_)


@app.route('/plot')
def plot():
    normal_t = 50
    buffer = []
    values = models.Temperature.query.order_by(asc(models.Temperature.date)).limit(31).all()
    for value in values:
        buffer.append({"date": value.date.strftime('%Y-%m-%d'), "temperature": value.temperature})
    return render_template('plot.html', values=buffer, NORMAL_T=normal_t)
