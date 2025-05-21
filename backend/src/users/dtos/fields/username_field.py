from src.users.dtos.base import BaseDTO


class UsernameField(BaseDTO):
    def __init__(self, data, settings):
        self.username = data
        self.settings = settings
        self.forbitten_names = [ 
            "offensive_name",
            "offensive name",
            "offensive Name",
            "Offensive Name",
            "Offensive name",
        ]

    def validate_data(self):
        if self.username.replace(" ", "") == "":
            return "empty-username"
        return self.check_for_offensive_words()

    def check_for_offensive_words(self):
        words = self.username.split()
        if set(self.forbitten_names).isdisjoint(set(words)):
            return {"username": self.username}
        return "offensive-speech"
