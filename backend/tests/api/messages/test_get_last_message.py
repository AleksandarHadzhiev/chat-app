import json

import pytest
from freezegun import freeze_time

from src.messages.repositories.postgres_repository import \
    break_down_long_messages
from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.messages import send_message as message
from tests.global_fixtures.users import login_user as access_token

test_data = [
    ("/messages/s/last-message", {"status": 400, "json": {"fail": "missing-id"}}),
    ("/messages/0/last-message", {"status": 400, "json": {"fail": "missing-id"}}),
    (
        "/messages/1/last-message",
        {
            "status": 200,
            "json": {},
        },
    ),
    ("/messages/4/last-message", {"status": 204, "json": {"messages": []}}),
]


@pytest.mark.order(10)
@freeze_time("2023-01-01-12-00-00")
@pytest.mark.parametrize("url, outcome", test_data)
def test_get_last_message(api, message, access_token, url, outcome):
    headers = {"Authorization": access_token}
    response = api.get(url, headers=headers)
    assert response.status_code == outcome["status"]
    if "message" in response.json():
        assert response.json()["message"][0]["content"] == "s"
    else:
        assert response.json() == outcome["json"]


def test_break_down_long_messages():
    message = "Some, very long message, which exceeds 50 charachters."
    output = break_down_long_messages(message=message, is_last_message=True)
    expected = message[:49] + "..."
    assert output == expected
