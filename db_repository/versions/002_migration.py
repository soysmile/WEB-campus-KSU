from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
hostels = Table('hostels', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('adress', String(length=140)),
)

persons = Table('persons', post_meta,
    Column('user_id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=30)),
    Column('last_name', String(length=30)),
    Column('department', String(length=50)),
    Column('group', Integer),
    Column('rooms_id', Integer),
)

rooms = Table('rooms', post_meta,
    Column('hostel_id', Integer),
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nummbers_of_person', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hostels'].create()
    post_meta.tables['persons'].create()
    post_meta.tables['rooms'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hostels'].drop()
    post_meta.tables['persons'].drop()
    post_meta.tables['rooms'].drop()
