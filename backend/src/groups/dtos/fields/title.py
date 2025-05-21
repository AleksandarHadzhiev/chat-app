from src.groups.dtos.fields.base import BaseField

class TitleField(BaseField):
    def __init__(self, data, settings):
        self.title = data
        self.settings = settings

    def validate_data(self):
        if self.title.replace(" ", "") == "" or self.title is None:
            return "empty-title"
        return {"title": self.title}