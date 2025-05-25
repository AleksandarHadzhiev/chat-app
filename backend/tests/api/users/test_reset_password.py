import json
from urllib.parse import urlparse, parse_qs

import pytest
from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.users import send_message_forgot_password as get_url

test_data = [
    ({"language": "EN", "email": "", "password": "", "user": ""}, {"status": 400, "json":{'fail': 'unsupported-format'}}),
    ({"email": "", "code": "", "password": ""}, {"status": 400, "json":{'fail': ['empty-email', 'empty-code', 'empty-password']}}),
    ({"email": "reset-password@gmail.com", "code": "", "password": ""}, {"status": 400, "json":{'fail': ['empty-code', 'empty-password']}}),
    ({"email": "reset-password@gmail.com", "code": "1232", "password": "123123"}, {"status": 400, "json":{'fail': 'unverified'}}),
    ({"email": "unverified@gmail.com", "code": "", "password": ""}, {"status": 400, "json":{'fail': ['unverified', 'empty-code', 'empty-password']}}),
    ({"email": "unverified@gmail.com", "code": "adsa", "password": "asdsad"}, {"status": 400, "json":{'fail': ['unverified']}}),
    ({"email": "user-not-found@gmail.com", "code": "adsa", "password": "asdsad"}, {"status": 400, "json":{'fail': ['user-not-found']}}),
]

@pytest.mark.parametrize("data, outcome", test_data)
def test_reset_password(api, data, outcome):
    response = api.post("/reset-password", content=json.dumps(data))
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]


def test_reset_password_success(api, get_url):
    url = get_url
    parsed_url = urlparse(url=url)
    queries = parse_qs(parsed_url.query)
    code = queries["code"][0]
    email: str = queries["email"][0]
    email = email.replace(" ", "")
    data = {"email": email, "code": code, "password": "123123"}
    _authorize_usccess(api=api, data={"email": email, "code": code})
    response = api.post("/reset-password", content=json.dumps(data))
    assert response.status_code == 200
    assert response.json() == {"message": "success"}


def _authorize_usccess(api, data: dict):
    response = api.post("/authorize", content=json.dumps(data))
    assert response.status_code == 201
    assert response.json() == {"message": "authorized"}
    