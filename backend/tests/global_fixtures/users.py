import json

import pytest
import requests

from tests.global_fixtures.boot_up import create_app as api

MAILHOG_API_URL = "http://localhost:8025/api/v2/messages"


@pytest.fixture(scope="session")
def create_user_to_verify(api):
    requst_data = {
        "language": "EN",
        "email": "verify@gmail.com",
        "password": "some-password",
        "username": "username",
    }
    email = {"box": "verify", "domain": "gmail.com"}
    response = api.post("/register", content=json.dumps(requst_data))
    assert response.status_code == 201
    assert response.json() == {"message": "success"}
    return mailhog(response=response, email=email, type="code")


@pytest.fixture(scope="session")
def send_message_forgot_password(api):
    data = {"language": "EN", "email": "reset-password@gmail.com"}
    email = {"box": "reset-password", "domain": "gmail.com"}
    response = api.post("/forgot-password", content=json.dumps(data))

    assert response.status_code == 200
    assert response.json() == {"message": "success"}
    return mailhog(response=response, email=email, type="reset")


def mailhog(response, email: dict, type: str):
    if response.status_code == 201 or response.status_code == 200:
        messages = _get_mailhog_messages()
        for message in messages:
            receivers = message["To"]
            return _find_message(
                message=message, receivers=receivers, email=email, type=type
            )
    return None


def _get_mailhog_messages():
    response = requests.get(MAILHOG_API_URL)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        return []


def _find_message(message, receivers, email, type: str = "code"):
    for receiver in receivers:
        if (
            receiver["Mailbox"] == email["box"]
            and receiver["Domain"] == email["domain"]
        ):
            if type == "code":
                return _get_code(message=message)
            else:
                return _get_url(message=message)
    return None


def _get_url(message):
    content = message["Content"]
    body: str = content["Body"]
    part = body.split("password: : ")[1]
    url = part.split("If that was not you")[0]
    return url


def _get_code(message):
    content = message["Content"]
    body: str = content["Body"]
    part = body.split("code: ")[1]
    return part[0:4]
