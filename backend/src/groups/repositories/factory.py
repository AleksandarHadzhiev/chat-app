from src.db.postgres import PostgresSQL
from src.groups.repositories.postgres_repository import PostgresRepository
from src.groups.repositories.repository import Repository


class RepositoryFactory:
    def __init__(self, db):
        self.db = db
        self.databases = {
            type(PostgresSQL()): PostgresRepository(db=db),
        }

    def get_db(self) -> Repository:
        keys = list(self.databases.keys())

        for key in keys:
            if type(self.db) == key:
                return self.databases[key]
        return None
