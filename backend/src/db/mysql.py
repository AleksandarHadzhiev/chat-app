import mysql.connector

from src.db.db import Database


class MySQL(Database):

    def set(self, settings):
        super().set(settings)
        self.settings = settings

    def create_db_and_tables(self):
        self._connect()
        self.cursor = self.connection.cursor()
        # TODO:
        # With the introduction of real modules, replace the code with the actual modules
        self.cursor.execute(
            "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
        )
        self.connection.commit()

    def _connect(self):
        self.connection = mysql.connector.connect(
            host=self.settings.HOST,
            user=self.settings.DATABASE_USER,
            database=self.settings.DATABASE_NAME,
            password=self.settings.DATABASE_PASSWORD,
        )

    def get_db(self):
        return self.connection
