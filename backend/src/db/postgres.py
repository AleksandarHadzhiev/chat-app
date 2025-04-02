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
        create_users_table = "CREATE TABLE users (id SERIAL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, username VARCHAR(255))"
        create_groups_table = (
            "CREATE TABLE groups (id SERIAL, title VARCHAR(255) NOT NULL)"
        )
        create_connection_between_users_and_groups_table = "CREATE TABLE groups_users (group_id integer NOT NULL, user_id integer NOT NULL)"
        create_messages_table = "CREATE TABLE messages (id SERIAL, author VARCHAR(255) NOT NULL, user_id integer NOT NULL, content VARCHAR, group_id integer NOT NULL)"

        self.cursor = self.connection.cursor()
        self.cursor.execute(create_users_table)
        self.cursor.execute(create_groups_table)
        self.cursor.execute(create_connection_between_users_and_groups_table)
        self.cursor.execute(create_messages_table)
        self.connection.commit()

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
