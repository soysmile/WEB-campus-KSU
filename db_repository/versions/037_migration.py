from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
room = Table('room', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('room_number', Integer),
    Column('note', String(length=30)),
    Column('numbers_of_person', Integer),
    Column('floor', Integer),
    Column('windows', Boolean),
    Column('service', Boolean),
    Column('econom', Boolean),
    Column('block_id', Integer),
    Column('hostel_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['room'].columns['econom'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['room'].columns['econom'].drop()
