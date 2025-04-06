from src.db.mysql import MySQL
from src.db.postgres import PostgresSQL
from src.db.sqlite import SQLite


class DBFactory:
    def __init__(self, env, settings):
        self.env: str = env
        self.settings = settings
        self.databases = {
            "docker": MySQL(),
            "test": SQLite(),
            "dev": PostgresSQL(),
        }

    def get_db(self):
        keys = list(self.databases.keys())

        for key in keys:
            if self.env.startswith(key):
                db = self.databases[key]
                print(db)
                db.set(self.settings)
                return db
        return None
