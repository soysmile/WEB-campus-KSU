from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
logger = Table('logger', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('url', String(length=255)),
    Column('remote_addr', String(length=255)),
    Column('method', String(length=255)),
    Column('user_agent', String(length=255)),
    Column('datetime', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['logger'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['logger'].drop()
