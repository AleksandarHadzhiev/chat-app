from src.users.dtos.base import BaseDTO


class CodeField(BaseDTO):
    def __init__(self, data, settings):
        self.code: str = data
        self.settings = settings


    def validate_data(self):
        if self.code.replace(" ", "") == "":
            return {"fail": "Empty code"}
        elif len(self.code) != self.settings.CODE_LENGTH:
            return {"fail": "Invalid code format"}
        return {"code": self.code}