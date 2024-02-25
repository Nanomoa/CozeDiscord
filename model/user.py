from sqlalchemy import Table, Column, Integer, String, Date
from sqlalchemy.orm import mapper
from model.common import metadata


class User(object):
    pass


user_table = Table('User', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('username', String),
                   Column('password', String),
                   Column('email', String),
                   Column('reg_data', Date),
                   Column('is_active', Integer)
                   )
mapper(User, user_table)
