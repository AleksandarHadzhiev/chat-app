from src.users.dtos.fields.email_field import EmailField
from src.users.dtos.fields.code_field import CodeField
from src.users.dtos.base import BaseDTO


class CodeDTO(BaseDTO):
    def set(self, data, settings):
        self.set_email(data=data)
        self.set_code(data=data)
        self.errors = []
        self.settings = settings


    def set_email(self, data):
        response = EmailField(data=data["email"]).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.email = response["email"]


    def set_code(self, data):
        response = CodeField(data=data["code"]).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.code = response["code"]


    def validate_data(self):
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "email": self.email,
            "code": self.code
        }