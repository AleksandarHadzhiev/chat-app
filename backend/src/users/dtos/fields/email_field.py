from src.users.dtos.base import BaseDTO


class EmailField(BaseDTO):
    def __init__(self, data, settings):
        self.email = data
        self.settings = settings


    def validate_data(self):
        if self.email.replace(" ", "") == "":
            return {"fail": "Empty email"}
        elif "@" not in self.email:
            return {"fail": "Invalid email"}
        return {"email": self.email}