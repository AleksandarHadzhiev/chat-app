from src.groups.repositories.factory import RepositoryFactory

MINIMUM_REQUIRED_ELEMENTS_FOR_A_LIST_TO_NOT_BE_EMPTY = 1

class GroupsService:
    def __init__(self, db, settings):
        self.settings = settings
        self.factory = RepositoryFactory(db=db)
        self.rep = self.factory.get_db()


    def create(self, incoming_data):
        self.rep.create(data=incoming_data)
        return {"message": "created group"}


    def get_all_for_user(self, user_id):
        if int(user_id) < MINIMUM_REQUIRED_ELEMENTS_FOR_A_LIST_TO_NOT_BE_EMPTY:
            return []
        return self.rep.get_all_for_user(user_id=user_id)


    def get_all(self):
        return self.rep.get_all()


    def join(self, user_id, group_id):
        data = {"group_id": group_id, "user_id": user_id}
        response = self.rep.join(data=data)
        return response


    async def leave(self, incoming_data):
        print(type(incoming_data))
        if "user_id" not in incoming_data or "group_id" not in incoming_data:
            return {"fail":"Insufficient information"}
        return self.rep.leave(data=incoming_data)


    async def kick_member_out(self, incoming_data):
        print(incoming_data)
        if "user_id" not in incoming_data or "group_id" not in incoming_data:
            return {"fail":"Insufficient information"}
        return self.rep.kick_member_out(data=incoming_data)
        

    async def delete(self, incoming_data):
        print(incoming_data)
        if "user_id" not in incoming_data or "group_id" not in incoming_data:
            return {"fail":"Insufficient information"}
        return self.rep.delete(data=incoming_data)


    async def edit(self, incoming_data):
        print(incoming_data)
        if "admin" not in incoming_data or "group_id" not in incoming_data or "title" not in incoming_data:
            return {"fail":"Insufficient information"}
        return self.rep.edit(data=incoming_data)
    
        
    async def get_group(self, incoming_data):
        print(incoming_data)
        if "user_id" not in incoming_data or "group_id" not in incoming_data:
            return {"fail":"Insufficient information"}
        return self.rep.get_group(data=incoming_data)
