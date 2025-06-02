import asyncio

from src.groups.dtos.base import BaseDTO
from src.groups.dtos.fields.admin import AdminField
from src.groups.dtos.fields.title import TitleField
from src.groups.repositories.repository import Repository


# Needs users.repository and not groups.repository
class CreateGroupDTO(BaseDTO):
    def set(self, data, settings, rep: Repository = None):
        self.settings = settings
        self.errors = []
        self.data = data

    async def set_title(self):
        response = TitleField(
            data=self.data["title"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.title = response["title"]

    async def set_admin(self):
        response = AdminField(
            data=self.data["admin"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.admin = self.data["admin"]

    async def validate_data(self):
        await asyncio.gather(self.set_admin(), self.set_title())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {"title": self.title, "admin": self.admin}
