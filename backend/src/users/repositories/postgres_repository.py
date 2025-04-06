from src.users.repositories.repository import Repository


class PostgresRepository(Repository):
    def __init__(self, db):
        self.db = db

    
    def register(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        create_user = "INSERT INTO users (email, password, username)"
        create_user += f" VALUES ('{data["email"]}', '{data["password"]}', '{data["username"]}')"
        cursor.execute(create_user)
        _db.commit()


    def login(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_user = "SELECT * FROM users"
        get_user += f" WHERE email = '{data["email"]}'"
        get_user += f" AND password = '{data["password"]}'"
        get_user += f" AND verified = true;"
        cursor.execute(get_user)
        users = cursor.fetchall()
        if len(users) > 0:
            user = {
                "id": users[0][0],
                "email": users[0][1],
                "password": users[0][2],
                "usename": users[0][3],
                "verified": users[0][4]
            }
            return user
        return None


    def reset_password(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        verify_user = f"UPDATE users SET password = '{data["password"]}"
        verify_user += f" WHERE email = '{data["email"]}'"
        verify_user += f" WHERE verified = true;"
        cursor.execute(verify_user)
        _db.commit()


    def verify(self, email):
        _db = self.db.get_db()
        cursor = _db.cursor()
        verify_user = "UPDATE users SET verified = true"
        verify_user += f" WHERE email = '{email}'"
        cursor.execute(verify_user)
        _db.commit()
    

    def get_by_email(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_user = "SELECT * FROM users"
        get_user += f" WHERE email = '{data["email"]}';"
        cursor.execute(get_user)
        users = cursor.fetchall()
        if len(users) > 0:
            user = {
                "id": users[0][0],
                "email": users[0][1],
                "password": users[0][2],
                "usename": users[0][3],
                "verified": users[0][4]
            }
            return user
        return None
