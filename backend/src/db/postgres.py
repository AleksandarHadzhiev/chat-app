import psycopg2

from src.db.db import DB


class PostgresSQL(DB):
    """Postgresql database."""

    def set(self, settings):
        """Initialize the database."""
        self.settings = settings


    def create_db_and_tables(self):
        """Create the database and tables."""
        self._connect()
        # TODO:
        # With the introduction of real modules, replace the code with the actual modules
        query = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)


    def _connect(self):
        self.connection = psycopg2.connect(
            database=self.settings.DATABASE_DB,
            host=self.settings.HOST,
            user=self.settings.USERNAME,
            port=self.settings.DATABASE_PORT,
            password=self.settings.PASSWORD,
        )

    def get_db(self):
        """Get the created database."""
        return self.cursor
