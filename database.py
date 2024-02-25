from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.common import metadata
from config import load_config

config = load_config()
mysql = config.coze_discord.mysql


class Database:
    def __init__(self):
        self.url = f"mysql+pymysql://{mysql.username}:{mysql.password}@{mysql.host}:{str(mysql.port)}/{mysql.database}"
        self.engine = create_engine(self.url)
        metadata.create_all(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)

    def connect(self):
        return self.session()

    def close(self):
        self.session().close()
