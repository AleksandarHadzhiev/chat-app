import logging

from src.users.repositories.repository import Repository

def break_down_long_messages(message: str, is_last_message=False):
        if len(message) > 50 and is_last_message:
            return message[:49] + "..."
        return message

class PostgresRepository(Repository):
    def __init__(self, db):
        self.db = db

    def create(self, data):
        try:
            user_id = data["user_id"]
            group_id = data["group_id"]
            _db = self.db.get_db()
            cursor = _db.cursor()
            create_message = f"""
                    INSERT INTO messages
                    (author, user_id, content, group_id, code, created_at)
                    VALUES
                    (
                        '{data['author']}', 
                        {user_id}, 
                        '{data['content']}', 
                        {group_id},
                        '{data["code"]}',
                        '{data["created_at"]}'
                    );"""
            cursor.execute(create_message)
            _db.commit()
            logging.info("Message created")
        except Exception as e:
            logging.exception(e)

    async def is_part_of_group(self, user_id, group_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_all = f"""
            SELECT * FROM groups
            INNER JOIN members ON members.group_id = groups.id
            WHERE members.user_id = {user_id}
            AND members.group_id = {group_id}
        """
        cursor.execute(get_all)
        groups = cursor.fetchall()
        if len(groups) > 0:
            return True
        return False

    async def is_author(self, user_id, code):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_all = f"""
            SELECT * FROM messages
            WHERE messages.user_id = {user_id}
            AND messages.code = '{code}'
        """
        cursor.execute(get_all)
        groups = cursor.fetchall()
        if len(groups) > 0:
            return True
        return False

    def get_all(self, group_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_messages = f"""
            SELECT * FROM messages
            WHERE messages.group_id = {group_id}
            ORDER BY messages.created_at;
        """
        cursor.execute(get_messages)
        messages = cursor.fetchall()
        if len(messages) > 0:
            return self._format_messages(messages=messages)
        return []

    def get_last_message(self, group_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_messages = f"""
            SELECT * FROM messages
            WHERE messages.group_id = {group_id}
            ORDER BY messages.created_at
            DESC
            LIMIT 1;
        """
        cursor.execute(get_messages)
        messages = cursor.fetchall()
        if len(messages) > 0:
            return self._format_messages(messages=messages, is_last_message=True)
        return []

    def _format_messages(self, messages, is_last_message=False):
        formatted_messages = []
        for message in messages:
            formatted_message = {
                "id": message[0],
                "author": message[1],
                "user_id": message[2],
                "content": break_down_long_messages(message[3], is_last_message),
                "group_id": message[4],
                "code": message[5],
                "created_at": message[6],
            }
            formatted_messages.append(formatted_message)
        return formatted_messages

    def edit(self, data):
        try:
            _db = self.db.get_db()
            cursor = _db.cursor()
            edit_message = f"""
                UPDATE messages
                SET content = '{data["content"]}'
                WHERE code = '{data["code"]}';
            """
            cursor.execute(edit_message)
            _db.commit()
            return {"message": "success"}
        except Exception as e:
            return {"fail": e}


    def delete(self, code, group_id, user_id):
        try:
            _db = self.db.get_db()
            cursor = _db.cursor()
            delete_message = f"""
                DELETE FROM messages
                WHERE messages.code = '{code}'
                AND messages.user_id = {user_id}
                AND messages.group_id = {group_id};
            """
            cursor.execute(delete_message)
            _db.commit() 
            return {"message": "success"}
        except Exception as e:
            logging.error(e.args)
            return {"fail": e} 
