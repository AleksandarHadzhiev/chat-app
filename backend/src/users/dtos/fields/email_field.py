from src.users.dtos.base import BaseDTO


class EmailField(BaseDTO):
    def __init__(self, data, settings):
        self.email = data
        self.settings = settings


    def validate_data(self):
        if self.email.replace(" ", "") == "":
            return "empty-email"
        elif "@" not in self.email:
            return "empty-email"
        return {"email": self.email}