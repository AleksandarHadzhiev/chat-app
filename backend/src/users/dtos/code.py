import asyncio
from src.users.repositories.repository import Repository
from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.code_field import CodeField
from src.users.dtos.fields.email_field import EmailField


class CodeDTO(BaseDTO):
    def set(self, data, settings, rep: Repository = None):
        self.settings = settings
        self.errors = []
        self.data = data
        self.rep = rep

    async def set_email(self):
        response = EmailField(
            data=self.data["email"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: await self._check_if_user_exists()

    async def _check_if_user_exists(self):
        email = {"email": self.data["email"]}
        user = await self.rep.get_by_email(data=email)
        if "user" in user:
            self.errors.append("user-not-found")
        else: self.email = email["email"]

    async def set_code(self):
        response = CodeField(data=self.data["code"], settings=self.settings).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.code = response["code"]

    async def validate_data(self):
        await asyncio.gather(self.set_email(), self.set_code())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {"email": self.email, "code": self.code}

    async def execute_validation(self):
        return await self.validate_data()
