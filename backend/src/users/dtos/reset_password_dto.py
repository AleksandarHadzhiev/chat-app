import asyncio
from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.code_field import CodeField
from src.users.dtos.fields.email_field import EmailField
from src.users.dtos.fields.password_field import PasswordField
from src.users.repositories.repository import Repository


class ResetPasswordDTO(BaseDTO):
    def set(self, data, settings, rep: Repository=None):
        self.settings = settings
        self.errors = []
        self.rep = rep
        self.data= data

    async def set_password(self):
        response = PasswordField(
            data=self.data["password"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.password = response["password"]

    async def set_email(self):
        response = EmailField(
            data=self.data["email"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else: await self._user_exists()    

    async def _user_exists(self):
        email = {"email": self.data["email"]}
        user = await self.rep.get_by_email(data=email)
        if "user" in user:
            self.errors.append("user-not-found")
        elif user["verified"] != True:
            self.errors.append("unverified")
        else: self.email = email["email"]        

    async def set_code(self):
        response = CodeField(data=self.data["code"], settings=self.settings).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.code = response["code"]

    async def validate_data(self):
        await asyncio.gather(self.set_email(), self.set_code(), self.set_password())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "password": self.password,
            "email": self.email,
            "code": self.code,
        }

    async def execute_validation(self):
        return await self.validate_data()