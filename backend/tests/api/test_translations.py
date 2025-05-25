import json
import pytest
from src.languages.translations.base import Base
from tests.global_fixtures.boot_up import client
from src.languages.translations.English.emails import EnglishEmailsTranslations
from src.languages.translations.Dutch.emails import DutchEmailsTranslations
from src.languages.translations.English.login import LoginTranlsations
from src.languages.translations.Dutch.login import DutchLoginTranlsations
from src.languages.translations.English.registration import RegistrationTranslations
from src.languages.translations.Dutch.registration import DutchRegistrationTranslations
from src.languages.translations.English.reset_password import ResetPasswordTranslations
from src.languages.translations.Dutch.reset_password import DutchResetPasswordTranslations
from src.languages.translations.Dutch.forgot_password import DutchForgotPasswordTranslations
from src.languages.translations.English.forgot_password import ForgotPasswordTranslations
from src.languages.translations.Dutch.groups import GroupsDutchTranlsations
from src.languages.translations.English.groups import GroupsEnglishTranlsations
from src.languages.translations.Dutch.messages import MessagesDutchTranlsations
from src.languages.translations.English.messages import MessagesEnglishTranlsations
from src.languages.translations.Dutch.navigation import NavigationDutchTranlsations
from src.languages.translations.English.navigation import NavigationEnglishTranlsations


def generate_json(translations: Base):
    full = {
        "translations": translations.get_translations()
    }
    return full

test_data = [
    ("/languages/translations/EN/login", {"status": 200, "json": generate_json(LoginTranlsations())}),
    ("/languages/translations/NL/login", {"status": 200, "json": generate_json(DutchLoginTranlsations())}),
    ("/languages/translations/EN/emails", {"status": 200, "json": generate_json(EnglishEmailsTranslations())}),
    ("/languages/translations/NL/emails", {"status": 200, "json": generate_json(DutchEmailsTranslations())}),
    ("/languages/translations/EN/registration", {"status": 200, "json": generate_json(RegistrationTranslations())}),
    ("/languages/translations/NL/registration", {"status": 200, "json": generate_json(DutchRegistrationTranslations())}),
    ("/languages/translations/EN/reset_password", {"status": 200, "json":generate_json(ResetPasswordTranslations())}),
    ("/languages/translations/NL/reset_password", {"status": 200, "json":generate_json(DutchResetPasswordTranslations())}),
    ("/languages/translations/EN/groups", {"status": 200, "json": generate_json(GroupsEnglishTranlsations())}),
    ("/languages/translations/NL/groups", {"status": 200, "json": generate_json(GroupsDutchTranlsations())}),
    ("/languages/translations/EN/forgot_password", {"status": 200, "json": generate_json(ForgotPasswordTranslations())}),
    ("/languages/translations/NL/forgot_password", {"status": 200, "json": generate_json(DutchForgotPasswordTranslations())}),
    ("/languages/translations/EN/messages", {"status": 200, "json": generate_json(MessagesEnglishTranlsations())}),
    ("/languages/translations/NL/messages", {"status": 200, "json": generate_json(MessagesDutchTranlsations())}),
    ("/languages/translations/EN/navigation", {"status": 200, "json":generate_json(NavigationEnglishTranlsations())}),
    ("/languages/translations/NL/navigation", {"status": 200, "json":generate_json(NavigationDutchTranlsations())}),
]


@pytest.mark.parametrize("url, outcome", test_data)
def test_get_en_login_translations(client, url, outcome):
    response = client.get(url)
    translations = response.json()
    data = json.loads(translations)
    assert response.status_code == outcome["status"] 
    assert data == outcome["json"]
