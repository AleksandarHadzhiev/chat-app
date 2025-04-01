from src.db.db import DB
import psycopg2

class PostgresSQL(DB):
    """Postgresql database."""
    def set(self, settings):
        """Initialize the database."""
        self.settings = settings
        self.connection = psycopg2.connect(
            database=settings.DATABASE_DB,
            host=settings.HOST,
            user=settings.USERNAME,
            port=settings.DATABASE_PORT,
            password=settings.PASSWORD,
        )

    def create_db_and_tables(self):
        """Create the database and tables."""
        # TODO:
        # With the introduction of real modules, replace the code with the actual modules
        query = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)


    def get_db(self):
        """Get the created database."""
        return self.cursor
