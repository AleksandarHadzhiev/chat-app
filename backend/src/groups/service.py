from src.groups.repositories.factory import RepositoryFactory
from src.groups.dtos.factory import DTOFactory

MINIMUM_REQUIRED_ELEMENTS_FOR_A_LIST_TO_NOT_BE_EMPTY = 1

class GroupsService:
    def __init__(self, db, settings):
        self.settings = settings
        self.factory = RepositoryFactory(db=db)
        self.rep = self.factory.get_db()

    async def create(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings, repository=self.rep)
        dto = factory.get_dto()
        if dto:
            response = await dto.validate_data()
            if ("fail" in response):
                return response
            self.rep.create(data=incoming_data)
            return {"message": "created group"}
        return {"fail": "unsupported"}

    def get_all_for_user(self, user_id: str):
        if user_id.isnumeric() is False:
            return {"fail": "invalid"}
        elif int(user_id) < MINIMUM_REQUIRED_ELEMENTS_FOR_A_LIST_TO_NOT_BE_EMPTY:
            return []
        return self.rep.get_all_for_user(user_id=user_id)

    def get_all(self):
        return self.rep.get_all()

    def join(self, user_id, group_id):
        incoming_data = {"group_id": group_id, "user_id": user_id}
        factory = DTOFactory(data=incoming_data, settings=self.settings, repository=self.rep)
        dto = factory.get_dto()
        if dto:
            response = dto.validate_data()
            if ("fail" in response):
                return response
            return self.rep.join(data=incoming_data)
        return {"fail": "unsupported"}

    async def leave(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings, repository=self.rep)
        dto = factory.get_dto()
        if dto:
            response = dto.validate_data()
            if ("fail" in response):
                return response
            return self.rep.leave(data=incoming_data)
        return {"fail": "unsupported"}

    async def kick_member_out(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings, repository=self.rep)
        dto = factory.get_dto()
        if dto:
            response = dto.validate_data()
            if ("fail" in response):
                return response
            return self.rep.kick_member_out(data=incoming_data)
        return {"fail": "unsupported"}

    async def delete(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings, repository=self.rep)
        dto = factory.get_dto()
        if dto:
            response = dto.validate_data()
            if ("fail" in response):
                return response
            return self.rep.delete(data=incoming_data)
        return {"fail": "unsupported"}

    async def edit(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings, repository=self.rep)
        dto = factory.get_dto()
        if dto:
            response = dto.validate_data()
            if ("fail" in response):
                return response
            return self.rep.edit(data=incoming_data)
        return {"fail": "unsupported"}

    async def get_group(self, incoming_data):
        factory = DTOFactory(data=incoming_data, settings=self.settings)
        dto = factory.get_dto()
        if dto:
            response = dto.validate_data()
            if ("fail" in response):
                return response
            return self.rep.get_group(data=incoming_data)
        return {"fail": "unsupported"}
