from src.messages.dtos.fields.base import BaseField

class GroupIdField(BaseField):
    def __init__(self, data, settings):
        self.group_id = data
        self.settings = settings

    def validate_data(self):
        if type(self.group_id) is int and self.group_id > 0:
            return {"group_id": self.group_id}
        return "undefined-group"