from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('register_id', INTEGER),
    Column('children_live', BOOLEAN),
    Column('childrens', VARCHAR(length=255)),
    Column('husband_wife', VARCHAR(length=255)),
    Column('husband_wife_birthday', DATE),
    Column('husband_wife_d_passport', DATE),
    Column('husband_wife_form_of_education', VARCHAR(length=255)),
    Column('husband_wife_k_passport', VARCHAR(length=255)),
    Column('husband_wife_lived', VARCHAR(length=255)),
    Column('husband_wife_lived_hostel', VARCHAR(length=255)),
    Column('husband_wife_lived_room', VARCHAR(length=255)),
    Column('husband_wife_n_passport', INTEGER),
    Column('husband_wife_s_passport', VARCHAR(length=255)),
    Column('husband_wife_work', VARCHAR(length=255)),
)

register_student = Table('register_student', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('register_id', Integer),
    Column('father', String(length=255)),
    Column('father_work', String(length=255)),
    Column('mother', String(length=255)),
    Column('mother_work', String(length=255)),
    Column('brothers_sisters', String(length=255)),
    Column('parents_street', String(length=255)),
    Column('parents_home', String(length=255)),
    Column('parents_apartment', String(length=255)),
    Column('parents_settlement', String(length=255)),
    Column('parents_district', String(length=255)),
    Column('parents_region', String(length=255)),
    Column('parents_index', Integer),
    Column('parents_landline_phone', String(length=255)),
    Column('parents_mobile_phone', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['register_student'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['register_student'].drop()
