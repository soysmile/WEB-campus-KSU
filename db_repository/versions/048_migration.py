from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
repair = Table('repair', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('date', DATE),
    Column('description', VARCHAR(length=255)),
    Column('tag', VARCHAR(length=255)),
    Column('fix', BOOLEAN),
    Column('person', INTEGER),
)

repair = Table('repair', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('open_date', Date),
    Column('description', String(length=255)),
    Column('tag', String(length=255)),
    Column('fix', Boolean),
    Column('close_date', Date),
    Column('person', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['repair'].columns['date'].drop()
    post_meta.tables['repair'].columns['close_date'].create()
    post_meta.tables['repair'].columns['open_date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['repair'].columns['date'].create()
    post_meta.tables['repair'].columns['close_date'].drop()
    post_meta.tables['repair'].columns['open_date'].drop()
