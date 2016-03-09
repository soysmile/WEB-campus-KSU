from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
hostel = Table('hostel', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('adress', String(length=140)),
)

person = Table('person', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=30)),
    Column('last_name', String(length=30)),
    Column('department', String(length=50)),
    Column('group', Integer),
    Column('room_id', Integer),
)

room = Table('room', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('numbers_of_person', Integer),
    Column('hostel_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hostel'].create()
    post_meta.tables['person'].create()
    post_meta.tables['room'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hostel'].drop()
    post_meta.tables['person'].drop()
    post_meta.tables['room'].drop()
