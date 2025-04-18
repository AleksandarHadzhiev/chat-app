from src.groups.repositories.factory import RepositoryFactory


class GroupsService():
    def __init__(self, db, settings):
        self.settings = settings
        self.factory = RepositoryFactory(db=db)
        self.rep = self.factory.get_db()


    def create(self, incoming_data):
        self.rep.create(data=incoming_data)
        return {"message": "Created a group"}


    def get_all_for_user(self, user_id):
        if (int(user_id) < 1):
            return []
        return self.rep.get_all_for_user(user_id=user_id)


    def get_all(self):
        return self.rep.get_all()


    def join(self, user_id, group_id):
        data =  {"group_id": group_id, "user_id": user_id}
        response = self.rep.join(data=data)
        return response