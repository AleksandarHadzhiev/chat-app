from src.groups.dtos.fields.base import BaseField

class MemberIdField(BaseField):
    def __init__(self, data, settings):
        self.member_id = data
        self.settings = settings

    def validate_data(self):
        if int(self.member_id) == 0 or self.member_id is None:
            return "invalid-member_id"
        return {"member_id": self.member_id}