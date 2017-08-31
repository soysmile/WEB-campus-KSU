# -*- coding: utf-8 -*-

import os
import platform


WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
basedir = os.path.abspath(os.path.dirname(__file__))
if platform.node() == 'DESKTOP-FANOEFQ':
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/hostel'
elif platform.node() == 'MacBook-Pro-George.local':
    SQLALCHEMY_DATABASE_URI = 'postgresql://george:55555555@localhost/hostel'
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://hostel:hostelsp@localhost/hostel'

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'ksu.studgorodok'
MAIL_PASSWORD = 'studgorodok.ksu'
MAIL_DEFAULT_SENDER = 'ksu.studgorodok@gmail.com'


UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

