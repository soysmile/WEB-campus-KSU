from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
temperature = Table('temperature', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('hostel_id', Integer),
    Column('date', Date),
    Column('temperature', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['temperature'].columns['hostel_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['temperature'].columns['hostel_id'].drop()
