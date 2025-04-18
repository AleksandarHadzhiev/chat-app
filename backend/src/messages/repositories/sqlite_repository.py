from src.users.repositories.repository import Repository

class SQLiteRepository(Repository):
    def __init__(self, db):
        self.db = db


    def create(self, data):
        pass


    def get_all(self, group_id):
        pass


    def edit(self, data):
        pass


    def delete(self, message_id):
        pass