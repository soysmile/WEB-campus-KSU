# -*- coding: utf-8 -*-

import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

MAIL_SERVER = 'smtp.yandex.ru'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'ksu.studgorodok'
MAIL_PASSWORD = 'studgorodok.ksu'
MAIL_DEFAULT_SENDER = 'ksu.studgorodok@yandex.ru'
