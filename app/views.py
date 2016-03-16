from flask import render_template, request, flash, redirect, url_for, g
from flask_login import logout_user, login_user, current_user, login_required
from app import app, db, models
from sqlalchemy import desc, asc


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = models.Post.query.order_by(desc(models.Post.timestamp)).limit(100).all()
        return render_template('index.html', posts=posts)
    login()


@app.route('/hostels', methods=['GET', 'POST'])
@login_required
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
    if request.method == 'GET':
        return render_template('register.html')
    user = models.User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = models.User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember=remember_me)
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/user/<username>')
@login_required
def user(username):
    user = models.User.query.filter_by(username=username).first()
    if user == None:
        flash('User %s not found.' % username)
        return redirect(url_for('index'))
    return render_template('profile.html', user=user)


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == "GET":
        return render_template('new.html')
    else:
        post = models.Post(request.form['title'], request.form['body'])
        db.session.add(post)
        db.session.commit()
        flash('Todo item was successfully created')
        return redirect(url_for('index'))


@app.route('/plot')
def plot():
    normal_t = 15
    buffer = []
    values = models.Temperature.query.order_by(asc(models.Temperature.date)).limit(31).all()
    for value in values:
        buffer.append({"date": value.date.strftime('%Y-%m-%d'), "temperature": value.temperature})
    return render_template('plot.html', values=buffer, NORMAL_T=normal_t)
