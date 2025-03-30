from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from src.db.db import DB


class PostgresSQL(DB):
    def __init__(self, url):
        self.url = url
        self.engine = create_engine(self.url)


    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)


    def get_db(self):
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        db = SessionLocal()
        try:
            return db
        finally:
            db.close()
