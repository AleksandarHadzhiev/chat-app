from src.messages.dtos.fields.base import BaseField


class CodeField(BaseField):
    def __init__(self, data, settings):
        self.code = data
        self.settings = settings

    def validate_data(self):
        if self.code.replace(" ", "") == "" or self.code is None:
            return "empty-code"
        return {"code": self.code}
