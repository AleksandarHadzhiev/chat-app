import asyncio
from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.code_field import CodeField
from src.users.dtos.fields.email_field import EmailField


class CodeDTO(BaseDTO):
    def set(self, data, settings, rep = None):
        self.settings = settings
        self.errors = []
        self.data = data

    async def set_email(self):
        response = EmailField(
            data=self.data["email"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.email = response["email"]

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
