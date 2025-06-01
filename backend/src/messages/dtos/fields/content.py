from src.messages.dtos.fields.base import BaseField

#  message = {
#                 "user_id": int(admin_id),
#                 "author": "GGC",
#                 "content": text,
#                 "group_id": 1,
#                 "code": f"1-1-{self.generate_special_code()}",
#                 "created_at": f"{str(datetime.datetime.now())}"
#             }


class ContentField(BaseField):
    def __init__(self, data, settings):
        self.content = data
        self.settings = settings
        self.forbitten_words = [  # Not actually offensive but an example.
            "offensive",
            "word",
            "offensive word",
            "offensive_word",
        ]

    def validate_data(self):
        if self.content.replace(" ", "") == "" or self.content is None:
            return "empty-content"
        return self.check_for_offensive_words()

    def check_for_offensive_words(self):
        words = self.content.split()
        if set(self.forbitten_words).isdisjoint(set(words)):
            return {"content": self.content}
        return "offensive-speech"
