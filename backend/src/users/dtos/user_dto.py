from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.email_field import EmailField
from src.users.dtos.fields.username_field import UsernameField
from src.users.dtos.fields.password_field import PasswordField

class UserDTO(BaseDTO):
    def set(self, data, settings):
        self.settings = settings
        self.set_email(data=data)
        self.set_username(data=data)
        self.set_password(data=data)
        self.errors = []


    def set_email(self, data):
        response = EmailField(data=data["email"], settings=self.settings).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.email = response["email"]


    def set_username(self, data):
        response = UsernameField(data=data["username"],  settings=self.settings).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.username = response["username"]


    def set_password(self, data):
        response = PasswordField(data=data["password"],  settings=self.settings).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.password = response["password"]


    def validate_data(self):
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "email": self.email,
            "username": self.username,
            "password": self.password
        }