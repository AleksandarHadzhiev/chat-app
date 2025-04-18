from src.users.repositories.repository import Repository


class MySQLRepository(Repository):
    def __init__(self, db):
        self.db = db

    def create(self, data):
        cursor = self.db.cursor()
        create_user = "INSERT INTO users (email, password, username)"
        create_user += f" VALUES ({data.email}, {data.password}, {data.username})"
        cursor.execute(create_user)
        self.db.commit()

    def login(self, data):
        pass

    def get_by_email(self, data):
        pass

    def reset_password(self, data):
        pass

    def verify(self, email):
        pass
