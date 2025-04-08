from src.users.dtos.base import BaseDTO


class PasswordField(BaseDTO):
    def __init__(self, data, settings):
        self.password = data
        self.settings = settings


    def validate_data(self):
        if self.password.replace(" ", "") == "":
            return "empty-password"
        return {"password": self.password}