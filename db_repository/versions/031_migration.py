from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person = Table('person', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
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
    Column('invite', String(length=255), default=ColumnDefault('3a1687a6-b092-4426-b6b1-97b0e81d6f30')),
    Column('room', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['email'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].columns['email'].drop()
