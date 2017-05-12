from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
register_main = Table('register_main', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('room_type', String(length=25)),
    Column('reason', String(length=50)),
    Column('first_name', String(length=50)),
    Column('last_name', String(length=50)),
    Column('middle_name', String(length=50)),
    Column('birthday', Date),
    Column('department', String(length=50)),
    Column('specialty', String(length=50)),
    Column('group', String(length=50)),
    Column('work', String(length=50)),
    Column('s_passport', String(length=50)),
    Column('n_passport', String(length=50)),
    Column('d_passport', Date),
    Column('k_passport', String(length=50)),
    Column('phone_number', String(length=50)),
    Column('lived_hostel', String(length=50)),
    Column('lived_room', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['register_main'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['register_main'].drop()
