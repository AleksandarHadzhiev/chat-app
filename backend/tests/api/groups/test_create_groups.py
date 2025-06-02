import json

import pytest
from freezegun import freeze_time

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.users import login_user as access_token

test_data = [
    (
        {"title": "", "admin": ""},
        {"status": 400, "json": {"fail": ["empty-admin", "empty-title"]}},
    ),
    ({"title": "ss", "admin": ""}, {"status": 400, "json": {"fail": ["empty-admin"]}}),
    ({"title": "", "admin": "1"}, {"status": 400, "json": {"fail": ["empty-title"]}}),
    (
        {"title": "INVALID-ADMIN", "admin": "0"},
        {
            "status": 400,
            "json": {
                "fail": [
                    "invalid-admin",
                ]
            },
        },
    ),
    (
        {"title": "VALUD-ADMIN", "admin": "2"},
        {"status": 201, "json": {"message": "created group"}},
    ),
]


@pytest.mark.order(2)
@freeze_time("2023-01-01 12:00:00")
@pytest.mark.parametrize("data, outcome", test_data)
def test_create_groups(api, access_token, data, outcome):
    access_token = access_token
    headers = {"Authorization": access_token}
    response = api.post("/groups", content=json.dumps(data), headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
