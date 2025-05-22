import asyncio

from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.email_field import EmailField
from src.users.dtos.fields.password_field import PasswordField
from src.users.dtos.fields.username_field import UsernameField
from src.users.repositories.repository import Repository

class UserDTO(BaseDTO):
    def set(self, data, settings, rep: Repository=None):
        self.settings = settings
        self.rep=rep
        self.verified = None
        self.errors = []
        self.data = data

    async def set_email(self):
        print("RUNNING SET EMAIL")
        response = EmailField(
            data=self.data["email"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            await self._user_validation()

    async def set_username(self):
        print("RUNNING SET USERNAME")
        response = UsernameField(
            data=self.data["username"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.username = response["username"]

    async def _user_validation(self):
        print("RUNNING _user_validation")
        email = {"email": self.data["email"]}
        user = await self.rep.get_by_email(email)
        print("FINISHED GET USER FROM DB")
        if user is None:
            self.email = self.data["email"]
        else: await self._is_already_verified(user)

    async def _is_already_verified(self, user):
        print("RUNNING _is_already_verified")
        if user["verified"] is True:
            self.errors.append("user-exists")
        else:
            self.verified = user
            self.email = self.data["email"]

    async def set_password(self):
        print("RUNNING set_password")
        response = PasswordField(
            data=self.data["password"], settings=self.settings
        ).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.password = response["password"]

    async def validate_data(self):
        print("RUNNING validate_data")
        await asyncio.gather(self.set_email(), self.set_password(), self.set_username())
        if len(self.errors) > 0:
            return {"fail": self.errors}
        elif self.verified is not None:
            return {"unverified": False,
                    "id": self.verified["id"],
                    "email": self.verified["email"],
                    "username": self.data["username"],
                    "password": self.data["password"],
                    }
        return {
            "email": self.email,
            "username": self.username,
            "password": self.password,
        }

    async def execute_validation(self):
        return await self.validate_data()
