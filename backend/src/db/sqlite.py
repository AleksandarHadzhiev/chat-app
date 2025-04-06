from sqlmodel import Session, SQLModel, create_engine

from src.db.db import Database


class SQLite(Database):
    def set(self, settings):
        self.sqlite_file_name = "database.db"
        self.url = f"{settings.DATABASE_URL}{self.sqlite_file_name}"
        print(self.url)
        self.engine = create_engine(self.url, echo=True)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self):
        with Session(self.engine) as session:
            return session
