from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from model.common import metadata


class Channel(object):
    pass


channel_table = Table('Channel', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('name', String),
                      Column('channel_id', Integer),
                      Column('user_id', Integer)
                      )
mapper(Channel, channel_table)
