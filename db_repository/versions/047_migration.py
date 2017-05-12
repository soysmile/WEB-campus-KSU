from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
repair = Table('repair', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', Date),
    Column('description', String(length=255)),
    Column('tag', String(length=255)),
    Column('fix', Boolean),
    Column('person', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['repair'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['repair'].drop()
