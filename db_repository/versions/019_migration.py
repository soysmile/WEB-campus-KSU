from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('first_name', VARCHAR(length=100)),
    Column('last_name', VARCHAR(length=100)),
    Column('login', VARCHAR(length=80)),
    Column('email', VARCHAR(length=120)),
    Column('password', VARCHAR(length=64)),
    Column('person_id', INTEGER),
    Column('permission', VARCHAR(length=5)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['first_name'].drop()
    pre_meta.tables['user'].columns['last_name'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['first_name'].create()
    pre_meta.tables['user'].columns['last_name'].create()
