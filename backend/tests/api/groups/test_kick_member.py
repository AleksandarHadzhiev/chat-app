import json

import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.users import login_user as access_token

test_data = [
    (
        0,
        0,
        0,
        {
            "status": 400,
            "json": {
                "fail": ["invalid-group_id", "invalid-user_id", "invalid-member_id"]
            },
        },
    ),
    (0, 1, 1, {"status": 400, "json": {"fail": ["invalid-group_id"]}}),
    (
        0,
        0,
        1,
        {"status": 400, "json": {"fail": ["invalid-group_id", "invalid-member_id"]}},
    ),
    (
        0,
        1,
        0,
        {
            "status": 400,
            "json": {
                "fail": [
                    "invalid-group_id",
                    "invalid-user_id",
                ]
            },
        },
    ),
    (
        1,
        1,
        0,
        {
            "status": 400,
            "json": {
                "fail": [
                    "invalid-user_id",
                ]
            },
        },
    ),
    (
        1,
        0,
        0,
        {"status": 400, "json": {"fail": ["invalid-user_id", "invalid-member_id"]}},
    ),
    (1, 12, 1, {"status": 400, "json": {"fail": "not-member"}}),
    (
        2,
        1,
        2,
        {"status": 400, "json": {"fail": "Unauthorized to remove member from group"}},
    ),
    (1, 2, 1, {"status": 200, "json": {"message": "kicked"}}),
]


@pytest.mark.order(6)
@pytest.mark.parametrize("id, member, admin, outcome", test_data)
def test_kick_member_out(api, access_token, id, member, admin, outcome):
    access_token = access_token
    headers = {"Authorization": access_token}
    response = api.delete(f"/groups/{id}/kick/{member}/{admin}", headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
