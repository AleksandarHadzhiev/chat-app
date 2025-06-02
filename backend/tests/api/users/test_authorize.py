import json

import pytest

from tests.global_fixtures.boot_up import client as api

test_data = [
    ({"email": "", "code": ""}, {"status": 400, "json": {"fail": "missing-code"}}),
    (
        {"email": "reset-password@gmail.com", "code": ""},
        {"status": 400, "json": {"fail": "missing-code"}},
    ),
    (
        {"email": "not-existing@gmail.com", "code": "2321"},
        {"status": 400, "json": {"fail": "unauthorized"}},
    ),
    ({"email": "", "code": "2321"}, {"status": 400, "json": {"fail": "missing-email"}}),
]


@pytest.mark.parametrize("data, outcome", test_data)
def test_authorize(api, data, outcome):
    response = api.post("/authorize", content=json.dumps(data))
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
