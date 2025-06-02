import logging

from src.users.repositories.repository import Repository


class PostgresRepository(Repository):
    def __init__(self, db):
        self.db = db

    def register(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        create_user = "INSERT INTO users (email, password, username)"
        create_user += (
            f" VALUES ('{data["email"]}', '{data["password"]}', '{data["username"]}')"
        )
        cursor.execute(create_user)
        _db.commit()
        self._join_general_chat_on_registration(data=data, cursor=cursor)
        _db.commit()

    def _join_general_chat_on_registration(self, data, cursor):
        user = self._get_user(data=data, cursor=cursor)
        if user:
            join_general = f"""
                INSERT INTO members
                (group_id, user_id)
                VALUES
                (1, {user['id']})
            """
            cursor.execute(join_general)
        else:
            logging.exception("User does not exist")

    def _get_user(self, data, cursor):
        get_user = "SELECT * FROM users"
        get_user += f" WHERE email = '{data["email"]}'"
        get_user += f" AND password = '{data["password"]}';"
        cursor.execute(get_user)
        users = cursor.fetchall()
        user = None
        if len(users) > 0:
            user = {
                "id": users[0][0],
                "email": users[0][1],
                "password": users[0][2],
                "username": users[0][3],
                "verified": users[0][4],
            }
        return user

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
                "username": users[0][3],
                "verified": users[0][4],
            }
            return user
        return None

    def reset_password(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        reset_password = f"UPDATE users SET password = '{data["password"]}'"
        reset_password += f" WHERE email = '{data["email"]}'"
        reset_password += f" AND verified = true;"
        cursor.execute(reset_password)
        _db.commit()

    def verify(self, email):
        _db = self.db.get_db()
        cursor = _db.cursor()
        verify_user = "UPDATE users SET verified = true"
        verify_user += f" WHERE email = '{email}'"
        cursor.execute(verify_user)
        _db.commit()

    async def update_user(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        update_user = f"UPDATE users SET password = '{data["password"]}', "
        update_user += f"username = '{data["username"]}'"
        update_user += f" WHERE id = {data["id"]}"
        cursor.execute(update_user)
        _db.commit()

    async def get_by_email(self, data):
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
                "username": users[0][3],
                "verified": users[0][4],
            }
            return user
        return {"user": "no"}

    async def get_by_id(self, user_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_user = "SELECT * FROM users"
        get_user += f" WHERE id = {user_id};"
        cursor.execute(get_user)
        users = cursor.fetchall()
        if len(users) > 0:
            user = {
                "id": users[0][0],
                "email": users[0][1],
                "password": users[0][2],
                "username": users[0][3],
                "verified": users[0][4],
            }
            return user
        return {"user": "no"}
