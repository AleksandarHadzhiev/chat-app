import json

import pytest

from tests.global_fixtures.boot_up import client as api

test_data = [
    (
        {"language": "EN", "email": "", "password": "", "user": ""},
        {"status": 400, "json": {"fail": "unsupported-format"}},
    ),
    (
        {"language": "EN", "email": ""},
        {"status": 400, "json": {"fail": ["empty-email"]}},
    ),
    (
        {"language": "EN", "email": "sadas.example.com"},
        {"status": 400, "json": {"fail": ["invalid-email"]}},
    ),
    (
        {"language": "EN", "email": "aleks@example.com"},
        {"status": 400, "json": {"fail": ["user-not-found"]}},
    ),
    (
        {"language": "EN", "email": "unverified@gmail.com"},
        {"status": 400, "json": {"fail": ["unverified"]}},
    ),
    (
        {"language": "EN", "email": "aleks_01_@gmail.com"},
        {"status": 200, "json": {"message": "success"}},
    ),
]


@pytest.mark.parametrize("data, outomce", test_data)
def test_forgot_password(api, data, outomce):
    response = api.post("/forgot-password", content=json.dumps(data))
    assert response.status_code == outomce["status"]
    assert response.json() == outomce["json"]
