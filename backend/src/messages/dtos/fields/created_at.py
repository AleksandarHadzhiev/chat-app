from src.messages.dtos.fields.base import BaseField
class CreatedAtField(BaseField):
    def __init__(self, data, settings):
        self.created_at = data
        self.settings = settings

    def validate_data(self):
        if self.created_at.replace(" ", "") == "" or self.created_at is None:
            return "empty-created_at"
        return {"created_at": self.created_at}