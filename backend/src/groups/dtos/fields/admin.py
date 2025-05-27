from src.groups.dtos.fields.base import BaseField

class AdminField(BaseField):
    def __init__(self, data, settings):
        self.admin = data
        self.settings = settings

    def validate_data(self):
        if (str(self.admin).replace(" ", "") == ""):
            return "empty-admin"
        if int(self.admin) == 0 or self.admin is None:
            return "invalid-admin"
        return {"admin": self.admin}