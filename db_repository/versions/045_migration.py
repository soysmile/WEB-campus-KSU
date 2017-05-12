from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
register_student = Table('register_student', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('register_id', Integer),
    Column('husband_wife', String(length=255)),
    Column('husband_wife_work', String(length=255)),
    Column('husband_wife_birthday', Date),
    Column('husband_wife_s_passport', String(length=255)),
    Column('husband_wife_n_passport', Integer),
    Column('husband_wife_d_passport', Date),
    Column('husband_wife_k_passport', String(length=255)),
    Column('husband_wife_form_of_education', String(length=255)),
    Column('husband_wife_lived', String(length=255)),
    Column('husband_wife_lived_hostel', String(length=255)),
    Column('husband_wife_lived_room', String(length=255)),
    Column('childrens', String(length=255)),
    Column('children_live', Boolean),
)

register_family = Table('register_family', post_meta,
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
    post_meta.tables['register_student'].columns['children_live'].create()
    post_meta.tables['register_student'].columns['childrens'].create()
    post_meta.tables['register_student'].columns['husband_wife'].create()
    post_meta.tables['register_student'].columns['husband_wife_birthday'].create()
    post_meta.tables['register_student'].columns['husband_wife_d_passport'].create()
    post_meta.tables['register_student'].columns['husband_wife_form_of_education'].create()
    post_meta.tables['register_student'].columns['husband_wife_k_passport'].create()
    post_meta.tables['register_student'].columns['husband_wife_lived'].create()
    post_meta.tables['register_student'].columns['husband_wife_lived_hostel'].create()
    post_meta.tables['register_student'].columns['husband_wife_lived_room'].create()
    post_meta.tables['register_student'].columns['husband_wife_n_passport'].create()
    post_meta.tables['register_student'].columns['husband_wife_s_passport'].create()
    post_meta.tables['register_student'].columns['husband_wife_work'].create()
    post_meta.tables['register_family'].columns['brothers_sisters'].create()
    post_meta.tables['register_family'].columns['father'].create()
    post_meta.tables['register_family'].columns['father_work'].create()
    post_meta.tables['register_family'].columns['mother'].create()
    post_meta.tables['register_family'].columns['mother_work'].create()
    post_meta.tables['register_family'].columns['parents_apartment'].create()
    post_meta.tables['register_family'].columns['parents_district'].create()
    post_meta.tables['register_family'].columns['parents_home'].create()
    post_meta.tables['register_family'].columns['parents_index'].create()
    post_meta.tables['register_family'].columns['parents_landline_phone'].create()
    post_meta.tables['register_family'].columns['parents_mobile_phone'].create()
    post_meta.tables['register_family'].columns['parents_region'].create()
    post_meta.tables['register_family'].columns['parents_settlement'].create()
    post_meta.tables['register_family'].columns['parents_street'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['register_student'].columns['children_live'].drop()
    post_meta.tables['register_student'].columns['childrens'].drop()
    post_meta.tables['register_student'].columns['husband_wife'].drop()
    post_meta.tables['register_student'].columns['husband_wife_birthday'].drop()
    post_meta.tables['register_student'].columns['husband_wife_d_passport'].drop()
    post_meta.tables['register_student'].columns['husband_wife_form_of_education'].drop()
    post_meta.tables['register_student'].columns['husband_wife_k_passport'].drop()
    post_meta.tables['register_student'].columns['husband_wife_lived'].drop()
    post_meta.tables['register_student'].columns['husband_wife_lived_hostel'].drop()
    post_meta.tables['register_student'].columns['husband_wife_lived_room'].drop()
    post_meta.tables['register_student'].columns['husband_wife_n_passport'].drop()
    post_meta.tables['register_student'].columns['husband_wife_s_passport'].drop()
    post_meta.tables['register_student'].columns['husband_wife_work'].drop()
    post_meta.tables['register_family'].columns['brothers_sisters'].drop()
    post_meta.tables['register_family'].columns['father'].drop()
    post_meta.tables['register_family'].columns['father_work'].drop()
    post_meta.tables['register_family'].columns['mother'].drop()
    post_meta.tables['register_family'].columns['mother_work'].drop()
    post_meta.tables['register_family'].columns['parents_apartment'].drop()
    post_meta.tables['register_family'].columns['parents_district'].drop()
    post_meta.tables['register_family'].columns['parents_home'].drop()
    post_meta.tables['register_family'].columns['parents_index'].drop()
    post_meta.tables['register_family'].columns['parents_landline_phone'].drop()
    post_meta.tables['register_family'].columns['parents_mobile_phone'].drop()
    post_meta.tables['register_family'].columns['parents_region'].drop()
    post_meta.tables['register_family'].columns['parents_settlement'].drop()
    post_meta.tables['register_family'].columns['parents_street'].drop()
