from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
register = Table('register', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=255)),
    Column('last_name', VARCHAR(length=255)),
    Column('middle_name', VARCHAR(length=255)),
    Column('department', VARCHAR(length=50)),
    Column('group', INTEGER),
    Column('form_of_education', VARCHAR(length=255)),
    Column('hostel_id', INTEGER),
    Column('room_id', INTEGER),
    Column('birthday', VARCHAR(length=255)),
    Column('passport', VARCHAR(length=255)),
    Column('parents', VARCHAR(length=255)),
    Column('index', INTEGER),
    Column('region', VARCHAR(length=255)),
    Column('district', VARCHAR(length=255)),
    Column('settlement', VARCHAR(length=255)),
    Column('street', VARCHAR(length=255)),
    Column('phone_number_parent', VARCHAR(length=255)),
    Column('phone_number', VARCHAR(length=255)),
    Column('note', VARCHAR(length=255)),
)

register = Table('register', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=255)),
    Column('last_name', String(length=255)),
    Column('middle_name', String(length=255)),
    Column('department', String(length=50)),
    Column('group', Integer),
    Column('form_of_education', String(length=255)),
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
    Column('email', String(length=255)),
    Column('note', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['register'].columns['hostel_id'].drop()
    post_meta.tables['register'].columns['email'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['register'].columns['hostel_id'].create()
    post_meta.tables['register'].columns['email'].drop()
