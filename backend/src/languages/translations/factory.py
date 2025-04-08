from src.languages.translations.base import Base
from src.languages.translations.English.login import LoginTranlsations
from src.languages.translations.English.registration import RegistrationTranslations
from src.languages.translations.English.reset_password import ResetPasswordTranslations
from src.languages.translations.English.forgot_password import ForgotPasswordTranslations

from src.languages.translations.Dutch.login import DutchLoginTranlsations
from src.languages.translations.Dutch.registration import DutchRegistrationTranslations
from src.languages.translations.Dutch.reset_password import DutchResetPasswordTranslations
from src.languages.translations.Dutch.forgot_password import DutchForgotPasswordTranslations

class TranslationsFactory():
    def __init__(self, data):
        self.data = data
        self.translations = [
            [{"language": "EN", "file": "login"}, LoginTranlsations()],
            [{"language": "EN", "file": "registration"}, RegistrationTranslations()],
            [{"language": "EN", "file": "reset_password"}, ResetPasswordTranslations()],
            [{"language": "EN", "file": "forgot_password"}, ForgotPasswordTranslations()],
            [{"language": "NL", "file": "login"}, DutchLoginTranlsations()],
            [{"language": "NL", "file": "registration"}, DutchRegistrationTranslations()],
            [{"language": "NL", "file": "forgot_password"}, DutchForgotPasswordTranslations()],
            [{"language": "NL", "file": "reset_password"}, DutchResetPasswordTranslations()],
        ]


    def get_translations(self) -> Base:
        for tranlsation in self.translations:
            if tranlsation[0] == self.data:
                return tranlsation[1]
        return None