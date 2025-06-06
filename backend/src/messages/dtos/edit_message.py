import asyncio

from src.messages.dtos.base import BaseDTO
from src.messages.dtos.fields.code import CodeField
from src.messages.dtos.fields.content import ContentField
from src.messages.dtos.fields.group_id import GroupIdField
from src.messages.dtos.fields.user_id import UserIdField
from src.messages.repositories.repository import Repository


class EditMessageDTO(BaseDTO):
    def set(self, data, settings, rep: Repository = None):
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
        else:
            self.user_id = response["user_id"]

    async def set_group_id(self):
        response = GroupIdField(
            data=self.data["group_id"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.group_id = response["group_id"]

    async def set_content(self):
        response = ContentField(
            data=self.data["content"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.content = response["content"]

    async def check_if_author(self):
        await asyncio.gather(self.set_user_id(), self.set_code())
        if "empty-code" not in self.errors or "undefined-user" not in self.errors:
            is_author = await self.rep.is_author(self.user_id, self.code)
            if is_author is False:
                self.errors.append("is-not-author")
        else:
            self.errors.append("is-not-author")

    async def set_code(self):
        response = CodeField(
            data=self.data["code"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.code = response["code"]

    async def check_if_is_member(self):
        await asyncio.gather(self.set_group_id(), self.set_user_id())
        print(self.errors)
        if "undefined-group" not in self.errors or "undefined-user" not in self.errors:
            is_part = await self.rep.is_part_of_group(self.user_id, self.group_id)
            if is_part is False:
                self.errors.append("is-not-member")
        else:
            self.errors.append("is-not-member")

    async def validate_data(self):
        await asyncio.gather(
            self.check_if_is_member(), self.check_if_author(), self.set_content()
        )
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "content": self.content,
            "code": self.code,
            "user_id": self.user_id,
            "group_id": self.group_id,
        }

    async def execute_validation(self):
        return await self.validate_data()
