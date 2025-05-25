import asyncio

from src.messages.repositories.repository import Repository
from src.messages.dtos.base import BaseDTO
from src.messages.dtos.fields.user_id import UserIdField
from src.messages.dtos.fields.author import AuthorField
from src.messages.dtos.fields.content import ContentField
from src.messages.dtos.fields.group_id import GroupIdField
from src.messages.dtos.fields.created_at import CreatedAtField
from src.messages.dtos.fields.code import CodeField

class MessageDTO(BaseDTO):
    def set(self, data, settings, rep: Repository=None):
        self.settings = settings
        self.errors = []
        self.data = data
        self.rep = rep

    async def set_user_id(self):
        response = UserIdField(
            data=self.data["user_id"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: self.user_id = response["user_id"]

    async def set_group_id(self):
        response = GroupIdField(
            data=self.data["group_id"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: self.group_id = response["group_id"]


    async def set_author(self):
        response = AuthorField(
            data=self.data["author"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: self.author = response["author"]

    async def set_content(self):
        response = ContentField(
            data=self.data["content"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.content = response["content"]

    async def set_created_at(self):
        response = CreatedAtField(
            data=self.data["created_at"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: self.created_at = response["created_at"]

    async def set_code(self):
        response = CodeField(
            data=self.data["code"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: self.code = response["code"]
        
    async def check_if_is_member(self):
        await asyncio.gather(self.set_group_id(), self.set_user_id())
        if (self.user_id and self.group_id):
            is_part = await self.rep.is_part_of_group(self.user_id, self.group_id)
            if is_part is False:
                self.errors.append("is-not-member")
        else: self.errors.append("is-not-member")

    async def validate_data(self):
        await asyncio.gather(self.check_if_is_member(), self.set_author(), self.set_code(), self.set_content(), self.set_created_at())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "content": self.content,
            "code": self.code,
            "content": self.author,
            "code": self.created_at,
            "user_id": self.user_id,
            "group_id": self.group_id,
            }

    async def execute_validation(self):
        return await self.validate_data()