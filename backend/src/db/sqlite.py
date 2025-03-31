from sqlmodel import Session, SQLModel, create_engine

from src.db.db import DB


class SQLite(DB):
    def __init__(self, url):
        self.sqlite_file_name = "database.db"
        self.url = f"{url}{self.sqlite_file_name}"
        self.engine = create_engine(self.url)


    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)


    def get_session(self):
        with Session(self.engine) as session:
            return session
