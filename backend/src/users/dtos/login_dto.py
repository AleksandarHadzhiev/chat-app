from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.email_field import EmailField
from src.users.dtos.fields.password_field import PasswordField

class LoginDTO(BaseDTO):
    def set(self, data, settings):
        self.settings = settings
        self.errors = []
        self.set_email(data=data)
        self.set_password(data=data)


    def set_email(self, data):
        response = EmailField(data=data["email"], settings=self.settings).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.email = response["email"]


    def set_password(self, data):
        response = PasswordField(data=data["password"], settings=self.settings).validate_data()
        if type(response) == str:
            self.errors.append(response)
        else:
            self.password = response["password"]


    def validate_data(self):
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "email": self.email,
            "password": self.password
        }