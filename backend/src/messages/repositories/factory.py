from src.db.mysql import MySQL
from src.db.postgres import PostgresSQL
from src.db.sqlite import SQLite
from src.messages.repositories.mysql_repository import MySQLRepository
from src.messages.repositories.postgres_repository import PostgresRepository
from src.messages.repositories.repository import Repository
from src.messages.repositories.sqlite_repository import SQLiteRepository


class RepositoryFactory:
    def __init__(self, db):
        self.db = db
        self.databases = {
            type(MySQL()): MySQLRepository(db=db),
            type(SQLite()): SQLiteRepository(db=db),
            type(PostgresSQL()): PostgresRepository(db=db),
        }

    def get_db(self) -> Repository:
        keys = list(self.databases.keys())

        for key in keys:
            if type(self.db) == key:
                return self.databases[key]
        return None
