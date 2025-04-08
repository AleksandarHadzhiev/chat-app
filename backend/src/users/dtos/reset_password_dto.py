from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.email_field import EmailField
from src.users.dtos.fields.code_field import CodeField
from src.users.dtos.fields.password_field import PasswordField

class ResetPasswordDTO(BaseDTO):
    def set(self, data, settings):
        self.settings = settings
        self.set_email(data=data)
        self.set_code(data=data)
        self.set_password(data=data)
        self.errors = []


    def set_password(self, data):
        response = PasswordField(data=data["password"],  settings=self.settings).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.password = response["password"]


    def set_email(self, data):
        response = EmailField(data=data["email"],  settings=self.settings).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.email = response["email"]


    def set_code(self, data):
        response = CodeField(data=data["code"],  settings=self.settings).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.code = response["code"]


    def validate_data(self):
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "password": self.password,
            "email": self.email,
            "code": self.code,
        }