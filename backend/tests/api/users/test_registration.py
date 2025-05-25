import json

import pytest
from tests.global_fixtures.boot_up import client as api

test_data = [
    ({"language": "EN", "email": "", "password": "", "user": ""}, {"status": 400, "json":{'fail': 'unsupported-format'}}),
    ({"language": "EN", "email": "", "password": "", "username": ""}, {"status": 400, "json":{'fail': ['empty-email', 'empty-password', 'empty-username']}}),
    ({"language": "EN", "email": "register@gmail.com", "password": "", "username": ""}, {"status": 400, "json":{'fail': ['empty-password', 'empty-username']}}),
    ({"language": "EN", "email": "unverified@gmail.com", "password": "", "username": ""}, {"status": 400, "json":{'fail': [ 'empty-password', 'empty-username']}}),
    ({"language": "EN", "email": "aleks_01_@gmail.com", "password": "", "username": ""}, {"status": 400, "json":{'fail': ['user-exists', 'empty-password', 'empty-username']}}),
    ({"language": "EN", "email": "", "password": "some-password", "username": ""}, {"status": 400, "json":{'fail': ['empty-email', 'empty-username']}}),
    ({"language": "EN", "email": "unverified@gmail.com", "password": "some-password", "username": ""}, {"status": 400, "json":{'fail': ['empty-username']}}),
    ({"language": "EN", "email": "", "password": "some-password", "username": "username"}, {"status": 400, "json":{'fail': ['empty-email']}}),
    ({"language": "EN", "email": "", "password": "", "username": "username"}, {"status": 400, "json":{'fail': ['empty-email', 'empty-password']}}),
    ({"language": "EN", "email": "invalid-email.example.com", "password": "some-password", "username": "username"}, {"status": 400, "json":{'fail': ['invalid-email']}}),
    ({"language": "EN", "email": "unverified@gmail.com", "password": "some-password", "username": "username"}, {"status": 201, "json":{'message': "success"}}),
    ({"language": "NL", "email": "unverified@gmail.com", "password": "some-password", "username": "username"}, {"status": 201, "json":{'message': "success"}}),
    ({"language": "EN", "email": "aleks_01_@gmail.com", "password": "admin", "username": "username"}, {"status": 400, "json":{'fail': ['user-exists']}}),
    ({"language": "EN", "email": "offensive@gmail.com", "password": "admin", "username": "offensive_name"}, {"status": 400, "json":{'fail': ['offensive-speech']}}),
]

@pytest.mark.parametrize("data, outcome", test_data)
def test_registration(api, data, outcome):
    response = api.post("/register", content=json.dumps(data))
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]


