import psycopg2

from src.db.db import Database


class PostgresSQL(Database):
    """Postgresql database."""

    def set(self, settings):
        """Initialize the database."""
        self.settings = settings

    def connect(self):
        self.connection = psycopg2.connect(
            database=self.settings.DATABASE_DB,
            host=self.settings.HOST,
            user=self.settings.USERNAME,
            port=self.settings.DATABASE_PORT,
            password=self.settings.PASSWORD,
        )

    def get_db(self):
        """Get the created database."""
        return self.connection
