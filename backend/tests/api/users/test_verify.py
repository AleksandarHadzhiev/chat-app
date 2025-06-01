import json
import logging

import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.users import create_user_to_verify as get_code

test_data = [
    (
        {"language": "EN", "email": "", "password": "", "user": ""},
        {"status": 400, "json": {"fail": "unsupported-format"}},
    ),
    (
        {"email": "", "code": ""},
        {"status": 400, "json": {"fail": ["empty-email", "empty-code"]}},
    ),
    (
        {"email": "invalid.email.com", "code": ""},
        {"status": 400, "json": {"fail": ["invalid-email", "empty-code"]}},
    ),
    (
        {"email": "", "code": "swwww"},
        {"status": 400, "json": {"fail": ["empty-email", "invalid-code"]}},
    ),
    ({"email": "", "code": "swww"}, {"status": 400, "json": {"fail": ["empty-email"]}}),
    (
        {"email": "user-not-found@gmail.com", "code": ""},
        {"status": 400, "json": {"fail": ["user-not-found", "empty-code"]}},
    ),
    (
        {"email": "user-not-found@gmail.com", "code": "swwqq"},
        {"status": 400, "json": {"fail": ["user-not-found", "invalid-code"]}},
    ),
    (
        {"email": "unverified@gmail.com", "code": "swqq"},
        {"status": 400, "json": {"fail": "unverified"}},
    ),
]


@pytest.mark.parametrize("data, outomce", test_data)
def test_verify(api, data, outomce):
    response = api.post("/verification", content=json.dumps(data))
    assert response.status_code == outomce["status"]
    assert response.json() == outomce["json"]


def test_verify_success(api, get_code):
    code = get_code
    if code:
        data = {"email": "verify@gmail.com", "code": str(code)}
        response = api.post("/verification", content=json.dumps(data))
        assert response.status_code == 200
        assert response.json() == {"message": "success"}
    else:
        logging.error(msg="Failed at fetching code from message")
