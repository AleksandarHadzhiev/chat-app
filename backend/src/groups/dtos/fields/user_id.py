from src.groups.dtos.fields.base import BaseField


class UserIdField(BaseField):
    def __init__(self, data, settings):
        self.user_id = data
        self.settings = settings

    def validate_data(self):
        if int(self.user_id) == 0 or self.user_id is None:
            return "invalid-user_id"
        return {"user_id": self.user_id}
