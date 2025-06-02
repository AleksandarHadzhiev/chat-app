from src.groups.dtos.fields.base import BaseField


class GroupIdField(BaseField):
    def __init__(self, data, settings):
        self.group_id = data
        self.settings = settings

    def validate_data(self):
        if int(self.group_id) == 0 or self.group_id is None:
            return "invalid-group_id"
        return {"group_id": self.group_id}
