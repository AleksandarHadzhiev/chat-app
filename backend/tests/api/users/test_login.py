import json

import pytest

from tests.global_fixtures.boot_up import client as api

test_data = [
    (
        {"language": "EN", "email": "", "password": "", "user": ""},
        {"status": 400, "json": {"fail": "unsupported-format"}},
    ),
    (
        {"email": "", "password": ""},
        {
            "status": 400,
            "json": {
                "fail": [
                    "empty-email",
                    "empty-password",
                ]
            },
        },
    ),
    (
        {"email": "user-not-found@gmail.com", "password": ""},
        {"status": 400, "json": {"fail": ["user-not-found", "empty-password"]}},
    ),
    (
        {"email": "unverified@gmail.com", "password": ""},
        {"status": 400, "json": {"fail": ["unverified", "empty-password"]}},
    ),
    (
        {"email": "aleks_01_@gmail.com", "password": ""},
        {"status": 400, "json": {"fail": ["empty-password"]}},
    ),
    (
        {"email": "", "password": "some-password"},
        {"status": 400, "json": {"fail": ["empty-email"]}},
    ),
    (
        {"email": "invalid-email.example.com", "password": "some-password"},
        {"status": 400, "json": {"fail": ["invalid-email"]}},
    ),
    (
        {"email": "user-not-found@example.com", "password": "some-password"},
        {"status": 400, "json": {"fail": ["user-not-found"]}},
    ),
    (
        {"email": "unverified@gmail.com", "password": "some-password"},
        {"status": 400, "json": {"fail": ["unverified"]}},
    ),
    (
        {"email": "aleks_01_@gmail.com", "password": "admin"},
        {
            "status": 200,
            "json": {
                "email": "aleks_01_@gmail.com",
                "id": 1,
                "password": "admin",
                "username": "administrator",
                "verified": True,
            },
        },
    ),
    (
        {"email": "aleks_01_@gmail.com", "password": "pesho"},
        {"status": 400, "json": {"fail": "wrong-credentials"}},
    ),
]


@pytest.mark.parametrize("data, outcome", test_data)
def test_login(api, data, outcome):
    response = api.post("/login", content=json.dumps(data))
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
