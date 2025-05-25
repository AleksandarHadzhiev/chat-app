from src.messages.repositories.factory import RepositoryFactory
from src.messages.dtos.factory import DTOFactory

class MessagesService:
    def __init__(self, db, settings):
        self.settings = settings
        self.rep = RepositoryFactory(db=db).get_db()

    def get_all(self, group_id):
        group_id_is_passed = group_id is not None and str(group_id).replace(" ", "") != ""
        if group_id_is_passed:
            response = self.rep.get_all(group_id=group_id)
            return response
        return {"fail": "missing-id"}

    async def create(self, data):
        factory = DTOFactory(data=data, settings=self.settings, rep=self.rep)
        dto = factory.get_dto()
        response = await dto.execute_validation()
        if "fail" in response:
            return response
        else :
            self.rep.create(data=data)
            return {"message": "success"}

    def get_last_message(self, group_id):
        group_id_is_passed = group_id is not None and str(group_id).replace(" ", "") != ""
        if group_id_is_passed:
            response = self.rep.get_last_message(group_id=group_id)
            return response
        return {"fail": "missing-id"}

    async def edit(self, data):
        factory = DTOFactory(data=data, settings=self.settings, rep=self.rep)
        dto = factory.get_dto()
        response = await dto.execute_validation()
        if "fail" in response:
            return response
        else :
            self.rep.edit(data=data)
            return {"message": "success"}


    def delete(self, code, group_id, user_id):
        code_is_passed = type(code) is str and code is not None and code.replace(" ", "") != ""
        group_id_is_passed = group_id is not None and str(group_id).replace(" ", "") != ""
        user_id_is_passed = user_id is not None and str(user_id).replace(" ", "") != ""
        if (code_is_passed and group_id_is_passed and user_id_is_passed):
            return self.rep.delete(code=code, group_id=group_id, user_id=user_id)
        return {"fail": "Incorrect data"}
