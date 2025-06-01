import asyncio

from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.email_field import EmailField
from src.users.repositories.repository import Repository


class ForgotPasswordDTO(BaseDTO):
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
        else:
            await self._user_exists()

    async def _user_exists(self):
        email = {"email": self.data["email"]}
        user = await self.rep.get_by_email(data=email)
        if "user" in user:
            self.errors.append("user-not-found")
        elif user["verified"] != True:
            self.errors.append("unverified")
        else:
            self.email = email["email"]

    async def validate_data(self):
        await asyncio.gather(self.set_email())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {"email": self.email}

    async def execute_validation(self):
        return await self.validate_data()
