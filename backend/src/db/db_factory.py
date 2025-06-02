from src.db.postgres import PostgresSQL


class DBFactory:
    def __init__(self, env, settings):
        self.env: str = env
        self.settings = settings
        self.databases = {
            "docker": PostgresSQL(),  # just switch the database by adding new module of database.
            "test": PostgresSQL(),
            "dev": PostgresSQL(),
        }

    def get_db(self):
        keys = list(self.databases.keys())

        for key in keys:
            if self.env.startswith(key):
                db = self.databases[key]
                db.set(self.settings)
                return db
        return None
