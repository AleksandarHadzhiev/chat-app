from src.users.repositories.repository import Repository


class SQLiteRepository(Repository):
    def __init__(self, db):
        self.db = db

    def register(self, data):
        pass

    def login(self, data):
        pass

    def get_by_email(self, data):
        pass

    def reset_password(self, data):
        pass

    def verify(self, email):
        pass
