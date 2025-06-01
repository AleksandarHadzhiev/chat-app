import json

import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.messages import send_message as message
from tests.global_fixtures.users import login_user as access_token

test_data = [
    ("/messages/s", {"status": 400, "json": {"fail": "missing-id"}}),
    ("/messages/0", {"status": 400, "json": {"fail": "missing-id"}}),
    (
        "/messages/2",
        {
            "status": 200,
            "json": {
                "messages": [
                    {
                        "id": 1,
                        "author": "Administrator",
                        "user_id": 2,
                        "content": "Chat has been created",
                        "group_id": 2,
                        "code": "2-2-2023-01-01-12-00-00",
                        "created_at": "2023-01-01 12:00:00",
                    }
                ]
            },
        },
    ),
    ("/messages/4", {"status": 204, "json": {"messages": []}}),
]


@pytest.mark.order(11)
@pytest.mark.parametrize("url, outcome", test_data)
def test_get_messages(api, access_token, message, url, outcome):
    headers = {"Authorization": access_token}
    response = api.get(url, headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
