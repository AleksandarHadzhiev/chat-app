from src.messages.dtos.fields.base import BaseField


class UserIdField(BaseField):
    def __init__(self, data, settings):
        self.user_id = data
        self.settings = settings

    def validate_data(self):
        if type(self.user_id) is int and self.user_id > 0:
            return {"user_id": self.user_id}
        return "undefined-user"
