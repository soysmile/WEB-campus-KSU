from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
hostels = Table('hostels', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('adress', VARCHAR(length=140)),
)

persons = Table('persons', pre_meta,
    Column('user_id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=30)),
    Column('last_name', VARCHAR(length=30)),
    Column('department', VARCHAR(length=50)),
    Column('group', INTEGER),
    Column('rooms_id', INTEGER),
)

rooms = Table('rooms', pre_meta,
    Column('hostel_id', INTEGER),
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nummbers_of_person', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['hostels'].drop()
    pre_meta.tables['persons'].drop()
    pre_meta.tables['rooms'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['hostels'].create()
    pre_meta.tables['persons'].create()
    pre_meta.tables['rooms'].create()
