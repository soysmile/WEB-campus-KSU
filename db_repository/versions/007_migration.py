from sqlalchemy import *

pre_meta = MetaData()
post_meta = MetaData()
hostel = Table('hostel', post_meta,
               Column('id', Integer, primary_key=True, nullable=False),
               Column('number', Integer),
               Column('adress', String(length=140)),
               )


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hostel'].columns['number'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hostel'].columns['number'].drop()
