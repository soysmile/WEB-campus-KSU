from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
statistics = Table('statistics', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', Date),
    Column('places_all', Integer),
    Column('places2', Integer),
    Column('places3', Integer),
    Column('places4', Integer),
    Column('free_1', Integer),
    Column('free_2', Integer),
    Column('free_3', Integer),
    Column('free_4', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['statistics'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['statistics'].drop()
