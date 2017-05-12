from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
news__slider = Table('news__slider', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=255)),
    Column('previewtext', String(length=255)),
    Column('body', Text),
    Column('timestamp', DateTime),
    Column('path', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['news__slider'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['news__slider'].drop()
