import logging

from src.users.repositories.repository import Repository


class PostgresRepository(Repository):
    def __init__(self, db):
        self.db = db

    def create(self, data):
        try:
            _db = self.db.get_db()
            cursor = _db.cursor()
            create_group = "INSERT INTO groups (title, admin_id)"
            create_group += f" VALUES ('{data["title"]}', {data["admin"]})"
            cursor.execute(create_group)
            _db.commit()
            self._add_as_a_member(data=data)
            logging.info("Created a group")
        except Exception as e:
            logging.exception(e)

    def _add_as_a_member(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_created_group_to_join = f"""
            SELECT id FROM groups
            WHERE groups.admin_id = {data["admin"]}
            AND groups.title = '{data["title"]}'
        """
        cursor.execute(get_created_group_to_join)
        groups = cursor.fetchall()
        if len(groups) > 0:
            print(groups)
            for group in groups:
                print(group)
                id = group[0]
                join_data = {"group_id": id, "user_id": data["admin"]}
                self.join(join_data)
                self._creeate_message_for_creating_chat(id=id, title=data["title"])

    def _creeate_message_for_creating_chat(self, id, title):
        _db = self.db.get_db()
        cursor = _db.cursor()
        create_message = f"""
            INSERT INTO messages
                (author, user_id, content, group_id)
                VALUES
                (
                    '{title}', 
                    {0}, 
                    'Chat has been created', 
                    {id}
                );"""
        cursor.execute(create_message)
        _db.commit()

    def get_all_for_user(self, user_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        print(user_id)
        get_all = f"""
            SELECT * FROM groups
            INNER JOIN members ON members.group_id = groups.id
            WHERE members.user_id = {user_id}
        """
        cursor.execute(get_all)
        groups = cursor.fetchall()
        if len(groups) > 0:
            return self._format_groups_data(groups=groups)
        return []

    def get_all(self):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_all = f"""
            SELECT * FROM groups
        """
        cursor.execute(get_all)
        groups = cursor.fetchall()
        if len(groups) > 0:
            return self._format_groups_data(groups=groups)
        return []

    def _format_groups_data(self, groups):
        formatted_groups = []
        for group in groups:
            print(group)
            formatted_group = {
                "id": group[0],
                "title": group[1],
            }
            if formatted_group not in formatted_groups:
                formatted_groups.append(formatted_group)
        return formatted_groups

    def join(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        is_member = self._check_if_already_a_member(data=data)
        if is_member:
            return {"message": "Already a member"}
        join_group = f"""
            INSERT INTO members
            (group_id, user_id)
            VALUES 
            ('{data["group_id"]}','{data["user_id"]}')
        """
        cursor.execute(join_group)
        _db.commit()
        return {"message": "Joined group"}

    def _check_if_already_a_member(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_all = f"""
            SELECT * FROM groups
            INNER JOIN members ON members.group_id = groups.id
            WHERE members.user_id = {data["user_id"]}
            AND members.group_id = {data["group_id"]}
        """
        cursor.execute(get_all)
        groups = cursor.fetchall()
        if len(groups) > 0:
            return True
        return False

    def leave(self, data):
        pass

    def kick_member_out(self, data):
        pass

    def get_group(self, data):
        pass

    def edit(self, data):
        pass

    def delete(self, email):
        pass
