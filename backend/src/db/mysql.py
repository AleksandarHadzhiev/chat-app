import mysql.connector
from src.db.db import DB


class MySQL(DB):
    
    def set(self, settings):
        super().set(settings)
        self.settings = settings
        self.connection = mysql.connector.connect(
            host=self.settings.HOST,
            user=self.settings.DATABASE_USER,
            database=self.settings.DATABASE_NAME,
            password=self.settings.DATABASE_PASSWORD,
        )


    def create_db_and_tables(self):
        self.cursor = self.connection.cursor()
        # TODO:
        # With the introduction of real modules, replace the code with the actual modules
        self.cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


    def get_db(self):
        return self.cursor