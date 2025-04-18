from src.languages.languages.dutch import Dutch
from src.languages.languages.english import English
from src.languages.translations.factory import TranslationsFactory


class LanguagesService:
    def __init__(self, db, settings):
        self.settings = settings
        self.db = db
        self.languages = [Dutch().get_data(), English().get_data()]

    def get_languages(self):
        return {"languages": self.languages}

    def add_language(self, incoming_data):
        pass

    def get_translations(self, data):
        factory = TranslationsFactory(data=data)
        tranlsations = factory.get_translations()
        return {"translations": tranlsations.get_translations()}

    def add_translations(self, email):
        pass
