import json
import logging

from src.users.repositories.repository import Repository


class PostgresRepository(Repository):
    def __init__(self, db):
        self.db = db

    def create(self, data):
        try:
            user_id = data["userId"]
            group_id = data["groupId"]
            is_part_of_group = self._is_part_of_group(
                user_id=user_id, group_id=group_id
            )
            if is_part_of_group:
                _db = self.db.get_db()
                cursor = _db.cursor()
                create_message = f"""
                    INSERT INTO messages
                    (author, user_id, content, group_id)
                    VALUES
                    (
                        '{data['author']}', 
                        {user_id}, 
                        '{data['content']}', 
                        {group_id}
                    );"""
                cursor.execute(create_message)
                _db.commit()
                logging.info("Message created")
            else:
                logging.info("Not part of group")
        except Exception as e:
            logging.exception(e)

    def _is_part_of_group(self, user_id, group_id):
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
        print(groups)
        if len(groups) > 0:
            return True
        return False

    def get_all(self, group_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_messages = f"""
            SELECT * FROM messages
            WHERE messages.group_id = {group_id};
        """
        cursor.execute(get_messages)
        messages = cursor.fetchall()
        if len(messages) > 0:
            return self._format_messages(messages=messages)
        return []

    def _format_messages(self, messages):
        formatted_messages = []
        for message in messages:
            formatted_message = {
                "id": message[0],
                "author": message[1],
                "user_id": message[2],
                "content": message[3],
                "group_id": message[4],
            }
            formatted_messages.append(formatted_message)
        return formatted_messages

    def edit(self, data):
        pass

    def delete(self, message_id):
        pass
