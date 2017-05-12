from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person_old = Table('person_old', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('start_date', DATE),
    Column('end_date', DATE),
    Column('last_name', VARCHAR(length=255)),
    Column('first_name', VARCHAR(length=255)),
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
    Column('email', VARCHAR(length=255)),
    Column('room', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['person_old'].columns['room'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['person_old'].columns['room'].create()
