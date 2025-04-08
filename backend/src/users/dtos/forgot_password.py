from src.users.dtos.base import BaseDTO
from src.users.dtos.fields.email_field import EmailField


class ForgotPasswordDTO(BaseDTO):
    def set(self, data, settings):
        self.settings = settings
        self.set_email(data=data)
        self.errors = []


    def set_email(self, data):
        response = EmailField(data=data["email"], settings=self.settings).validate_data()
        if "fail" in response:
            self.errors.append(response)
        else:
            self.email = response["email"]



    def validate_data(self):
        if len(self.errors) > 0:
            return {"fail": self.errors}
        return {
            "email": self.email
        }