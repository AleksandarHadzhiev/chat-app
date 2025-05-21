from src.messages.dtos.fields.base import BaseField
class AuthorField(BaseField):
    def __init__(self, data, settings):
        self.author = data
        self.settings = settings

    def validate_data(self):
        if self.author.replace(" ", "") == "" or self.author is None:
            return "empty-author"
        return {"author": self.author}