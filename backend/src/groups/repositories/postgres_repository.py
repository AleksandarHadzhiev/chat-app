import datetime
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
            for group in groups:
                id = group[0]
                join_data = {"group_id": id, "user_id": data["admin"]}
                self.join(join_data)
                self._creeate_message_for_creating_chat(id=id, admin_id=data["admin"])


    def _creeate_message_for_creating_chat(self, id, admin_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        create_message = f"""
            INSERT INTO messages
                (author, user_id, content, group_id, code, created_at)
                VALUES
                (
                    'Administrator', 
                    {admin_id}, 
                    'Chat has been created', 
                    {id},
                    '{admin_id}-{id}-{self._generate_special_code()}',
                    '{str(datetime.datetime.now())}'
                );"""
        cursor.execute(create_message)
        _db.commit()

    def _generate_special_code(self):
        initial_state = str(datetime.datetime.now())
        without_space = initial_state.replace(" ", "-")
        without_column = without_space.replace(":","-")
        return without_column


    def get_all_for_user(self, user_id):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_all = f"""
            SELECT groups.id, groups.admin_id, groups.title, members.user_id, users.username FROM groups
            INNER JOIN members ON members.group_id = groups.id
            INNER JOIN users ON users.id = members.user_id
            WHERE members.user_id = {user_id}
            ORDER BY groups.id;
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
            SELECT groups.id, groups.admin_id, groups.title, members.user_id, users.username FROM groups
            INNER JOIN members ON members.group_id = groups.id
            INNER JOIN users ON users.id = members.user_id
            ORDER BY groups.id;
        """
        cursor.execute(get_all)
        groups = cursor.fetchall()
        if len(groups) > 0:
            return self._format_groups_data(groups=groups)
        return []


    def _format_groups_data(self, groups):
        formatted_groups = []
        group_id = 0
        members = []
        for group in groups:
            if group_id != group[0]:
                group_id = group[0]
                members = []
                formatted_group = {
                    "id": group_id,
                    "title": group[2],
                    "admin_id": group[1],
                }
            if (len(group) >3 ):
                member = {
                    "id": group[3],
                    "name": group[4]
                }
                members.append(member)
                formatted_group["members"] = members
            if formatted_group not in formatted_groups:
                formatted_groups.append(formatted_group)
        return formatted_groups


    def join(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        is_member = self._check_if_already_a_member(data=data)
        if is_member:
            return {"fail": "already a member"}
        join_group = f"""
            INSERT INTO members
            (group_id, user_id)
            VALUES 
            ('{data["group_id"]}','{data["user_id"]}')
        """
        cursor.execute(join_group)
        _db.commit()
        return {"message": "joined"}


    def _check_if_already_a_member(self, data):
        _db = self.db.get_db()
        cursor = _db.cursor()
        get_all = f"""
            SELECT * FROM members
            WHERE members.user_id = {data["user_id"]}
            AND members.group_id = {data["group_id"]}
        """
        cursor.execute(get_all)
        members = cursor.fetchall()
        print(members)
        if len(members) > 0:
            return True
        return False


    def leave(self, data):
        try:
            _db = self.db.get_db()
            cursor = _db.cursor()
            is_member = self._check_if_already_a_member(data=data)
            if is_member:
                admin_in_group = self.get_group(data=data)
                if admin_in_group:
                    self.delete(data=data)
                else:
                    leave_group = f"""
                    DELETE FROM members
                    WHERE members.user_id = {data["user_id"]}
                    AND members.group_id = {data["group_id"]};
                    """
                    cursor.execute(leave_group)
                _db.commit() 
                return {"message": "left"}
            else: return {"fail": "not-member"}
        except Exception as e:
            return {"fail": e}       


    def kick_member_out(self, data):
        try:
            _db = self.db.get_db()
            cursor = _db.cursor()
            group = self.get_group(data=data)
            if group:
                is_member = self._check_if_already_a_member(data={"group_id": data["group_id"], "user_id": data["member_id"]})
                print(data)
                print(is_member)
                if is_member:
                    if (data["member_id"] == data["user_id"]):
                        self.delete(data)
                    else:
                        kick_from_group = f"""
                            DELETE FROM members
                            WHERE members.user_id = {data["member_id"]}
                            AND members.group_id = {data["group_id"]};
                        """
                        cursor.execute(kick_from_group)
                        _db.commit() 
                    return {"message": "kicked"}
                else: return {"fail": "not-member"}
            return {"fail": "Unauthorized to remove member from group"}
        except Exception as e:
            return {"fail": e}    


    def get_group(self, data):
        _db = self.db.get_db() 
        cursor = _db.cursor()
        get_all = f"""
            SELECT * FROM groups
            WHERE groups.admin_id = {data["user_id"]}
            AND groups.id = {data["group_id"]};
        """
        cursor.execute(get_all)
        groups = cursor.fetchall()
        if len(groups) > 0:
            return self._format_groups_data(groups=groups)
        return []


    def edit(self, data):
        try:
            _db = self.db.get_db()
            cursor = _db.cursor()
            edit_group = f"""
                UPDATE groups
                SET title = '{data["title"]}'
                WHERE id = {data["group_id"]}
                AND admin_id = {data["admin"]};
            """
            cursor.execute(edit_group)
            _db.commit()  
            return {"message": "edited"}
        except Exception as e:
            return {"fail": e}


    def delete(self, data):
        try:
            _db = self.db.get_db()
            cursor = _db.cursor()
            delete_groups = f"""
                DELETE FROM groups
                WHERE groups.id = {data["group_id"]}
                AND groups.admin_id = {data["user_id"]};
            """
            cursor.execute(delete_groups)
            kick_members = f"""
                    DELETE FROM members
                    WHERE members.group_id = {data["group_id"]};
                """
            cursor.execute(kick_members)
            _db.commit() 
            return {"message": "deleted"}
        except Exception as e:
            return {"fail": e}       
