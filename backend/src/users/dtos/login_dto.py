import asyncio
from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.email_field import EmailField
from src.users.dtos.fields.password_field import PasswordField
from src.users.repositories.repository import Repository


class LoginDTO(BaseDTO):
    def set(self, data, settings, rep: Repository=None):
        self.rep = rep
        self.settings = settings
        self.errors = []
        self.data = data

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
        elif user["verified"] is not True:
            self.errors.append("unverified")
        else: self.email = email["email"]

    async def set_password(self):
        response = PasswordField(
            data=self.data["password"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.password = response["password"]

    async def validate_data(self):
        await asyncio.gather(self.set_email(), self.set_password())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {"email": self.email, "password": self.password}

    async def execute_validation(self):
        return await self.validate_data()