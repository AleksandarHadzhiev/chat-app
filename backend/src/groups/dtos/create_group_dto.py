import asyncio

from src.groups.dtos.base import BaseDTO
from src.groups.dtos.fields.admin import AdminField
from src.groups.dtos.fields.title import TitleField
# Needs users.repository and not groups.repository
class CreateGroupDTO(BaseDTO):
    def set(self, data, settings,):
        self.settings = settings
        self.errors = []
        self.data = data
        self.set_title(data=data)
        self.set_admin(data=data)

    async def set_title(self, data):
        response = TitleField(
            data=data["title"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.title = response["title"]

    async def set_admin(self, data):
        response = AdminField(
            data=data["admin"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: self.user_exists(data=data["admin"])

    async def user_exists(self, data):
        # Find a way to get Users.Repository here to do the checking
        user = self.rep.get_by_id(user_id = data)
        if "user" in user:
            self.errors.append("user-not-found")
        else: self.admin = data

    async def validate_data(self):
        await asyncio.gather(self.set_admin(), self.set_title())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "title": self.title,
            "admin": self.admin
        }