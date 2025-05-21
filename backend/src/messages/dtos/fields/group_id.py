from src.messages.dtos.fields.base import BaseField

class GroupIdField(BaseField):
    def __init__(self, data, settings):
        self.group_id = data
        self.settings = settings

    def validate_data(self):
        if 