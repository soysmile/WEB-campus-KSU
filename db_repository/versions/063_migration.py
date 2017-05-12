from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person_old = Table('person_old', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('start_date', Date),
    Column('end_date', Date),
    Column('last_name', String(length=255)),
    Column('first_name', String(length=255)),
    Column('middle_name', String(length=255)),
    Column('department', String(length=50)),
    Column('group', Integer),
    Column('form_of_education', String(length=255)),
    Column('hostel_id', Integer),
    Column('room_id', Integer),
    Column('birthday', String(length=255)),
    Column('passport', String(length=255)),
    Column('parents', String(length=255)),
    Column('index', Integer),
    Column('region', String(length=255)),
    Column('district', String(length=255)),
    Column('settlement', String(length=255)),
    Column('street', String(length=255)),
    Column('phone_number_parent', String(length=255)),
    Column('phone_number', String(length=255)),
    Column('note', String(length=255)),
    Column('email', String(length=255)),
    Column('invite', String(length=255), default=ColumnDefault('6adb8ac4-de6e-4204-b76f-087febf9791e')),
)

person = Table('person', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('start_date', Date),
    Column('last_name', String(length=255)),
    Column('first_name', String(length=255)),
    Column('middle_name', String(length=255)),
    Column('department', String(length=50)),
    Column('group', Integer),
    Column('form_of_education', String(length=255)),
    Column('hostel_id', Integer),
    Column('room_id', Integer),
    Column('birthday', String(length=255)),
    Column('passport', String(length=255)),
    Column('parents', String(length=255)),
    Column('index', Integer),
    Column('region', String(length=255)),
    Column('district', String(length=255)),
    Column('settlement', String(length=255)),
    Column('street', String(length=255)),
    Column('phone_number_parent', String(length=255)),
    Column('phone_number', String(length=255)),
    Column('note', String(length=255)),
    Column('email', String(length=255)),
    Column('invite', String(length=255), default=ColumnDefault('4e7acd69-1b40-4286-b098-5b8936ce94cf')),
    Column('room', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person_old'].create()
    post_meta.tables['person'].columns['start_date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person_old'].drop()
    post_meta.tables['person'].columns['start_date'].drop()
