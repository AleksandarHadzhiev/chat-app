from src.db.db import DB
from src.db.postgres import PostgresSQL
from src.db.sqlite import SQLite


class DBFactory:
    def __init__(self, url):
        self.url: str = url
        self.databases = {
            "postgresql": PostgresSQL(self.url),
            "sqllite": SQLite(self.url),
        }

    def get_db(self) -> DB:
        keys = list(self.databases.keys())

        for key in keys:
            if self.url.startswith(key):
                return self.databases[key]
        return None
