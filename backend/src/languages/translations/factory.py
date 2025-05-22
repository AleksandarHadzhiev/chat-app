from src.languages.translations.base import Base
from src.languages.translations.Dutch.forgot_password import \
    DutchForgotPasswordTranslations
from src.languages.translations.Dutch.login import DutchLoginTranlsations
from src.languages.translations.Dutch.registration import \
    DutchRegistrationTranslations
from src.languages.translations.Dutch.reset_password import \
    DutchResetPasswordTranslations
from src.languages.translations.English.forgot_password import \
    ForgotPasswordTranslations
from src.languages.translations.English.login import LoginTranlsations
from src.languages.translations.English.registration import \
    RegistrationTranslations
from src.languages.translations.English.reset_password import \
    ResetPasswordTranslations
from src.languages.translations.English.groups import GroupsEnglishTranlsations 
from src.languages.translations.Dutch.groups import GroupsDutchTranlsations
from src.languages.translations.English.navigation import NavigationEnglishTranlsations
from src.languages.translations.Dutch.navigation import NavigationDutchTranlsations
from src.languages.translations.English.messages import MessagesEnglishTranlsations
from src.languages.translations.Dutch.messages import MessagesDutchTranlsations
from src.languages.translations.English.emails import EnglishEmailsTranslations
from src.languages.translations.Dutch.emails import DutchEmailsTranslations

class TranslationsFactory:
    def __init__(self, data):
        self.data = data
        self.translations = [
            [{"language": "EN", "file": "login"}, LoginTranlsations()],
            [{"language": "EN", "file": "emails"}, EnglishEmailsTranslations()],
            [{"language": "EN", "file": "registration"}, RegistrationTranslations()],
            [{"language": "EN", "file": "reset_password"}, ResetPasswordTranslations()],
            [
                {"language": "EN", "file": "forgot_password"},
                ForgotPasswordTranslations(),
            ],            [
                {"language": "EN", "file": "groups"},
                GroupsEnglishTranlsations(),
            ],[
                {"language": "EN", "file": "navigation"},
                NavigationEnglishTranlsations(),
            ],[
                {"language": "EN", "file": "messages"},
                MessagesEnglishTranlsations(),
            ],
            [{"language": "NL", "file": "login"}, DutchLoginTranlsations()],
            [{"language": "NL", "file": "emails"}, DutchEmailsTranslations()],
            [
                {"language": "NL", "file": "registration"},
                DutchRegistrationTranslations(),
            ],
            [
                {"language": "NL", "file": "forgot_password"},
                DutchForgotPasswordTranslations(),
            ],
            [
                {"language": "NL", "file": "reset_password"},
                DutchResetPasswordTranslations(),
            ],
            [
                {"language": "NL", "file": "groups"},
                GroupsDutchTranlsations(),
            ],
            [
                {"language": "NL", "file": "navigation"},
                NavigationDutchTranlsations(),
            ],
            [
                {"language": "NL", "file": "messages"},
                MessagesDutchTranlsations(),
            ],
        ]

    def get_translations(self) -> Base:
        for tranlsation in self.translations:
            if tranlsation[0] == self.data:
                return tranlsation[1]
        return None
