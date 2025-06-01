import json

from freezegun import freeze_time
import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.messages import send_message as message
from tests.global_fixtures.users import login_user as access_token


test_data = [
    (
        {"content": "", "code": "", "user_id": int(0), "group_id": int(0)},
        {
            "status": 400,
            "json": {
                "fail": [
                    "empty-content",
                    "undefined-group",
                    "undefined-user",
                    "undefined-user",
                    "empty-code",
                    "is-not-member",
                    "is-not-author",
                ]
            },
        },
    ),
    (
        {"content": "a", "code": "wqwe", "user_id": int(2), "group_id": int(2)},
        {"status": 400, "json": {"fail": ["is-not-member", "is-not-author"]}},
    ),
    (
        {"content": "a", "code": "s", "user_id": int(2), "group_id": int(1)},
        {"status": 400, "json": {"fail": ["is-not-member", "is-not-author"]}},
    ),
    (
        {"content": "s", "code": "s", "user_id": int(1), "group_id": int(1)},
        {
            "status": 400,
            "json": {
                "fail": [
                    "is-not-author",
                ]
            },
        },
    ),
    (
        {"content": "wa", "code": "1-1-2023-01-01-12-00-00", "user_id": int(1), "group_id": int(1)},
        {"status": 200, "json": {"message": "success"}},
    ),
]


@freeze_time("2023-01-01 12:10:00")
@pytest.mark.order(9)
@pytest.mark.parametrize("data, outcome", test_data)
def test_edit_message(api, access_token, message, data, outcome):
    headers = {
        "Authorization": access_token
    }
    response = api.put("/messages", content=json.dumps(data), headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
