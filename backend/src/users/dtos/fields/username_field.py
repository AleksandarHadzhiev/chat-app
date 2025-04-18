from src.users.dtos.base import BaseDTO


class UsernameField(BaseDTO):
    def __init__(self, data, settings):
        self.username = data
        self.settings = settings

    def validate_data(self):
        if self.username.replace(" ", "") == "":
            return "empty-username"
        return {"username": self.username}
