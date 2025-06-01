import json

import pytest

from src.messages.repositories.postgres_repository import break_down_long_messages
from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.messages import send_message as message

test_data = [
    ("/messages/s/last-message", {"status": 400, "json": {"fail": "missing-id"}}),
    ("/messages/0/last-message", {"status": 400, "json": {"fail": "missing-id"}}),
    (
        "/messages/1/last-message",
        {
            "status": 200,
            "json": {
                "message": [
                    {
                        "id": 6,
                        "author": "s",
                        "user_id": 1,
                        "content": "wa",
                        "group_id": 1,
                        "code": "wqwe",
                        "created_at": "as",
                    }
                ]
            },
        },
    ),
    ("/messages/4/last-message", {"status": 204, "json": {"messages": []}}),
]


@pytest.mark.order(10)
@pytest.mark.parametrize("url, outcome", test_data)
def test_edit_message(api, message, url, outcome):
    response = api.get(url)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]


def test_break_down_long_messages():
    message = "Some, very long message, which exceeds 50 charachters."
    output = break_down_long_messages(message=message, is_last_message=True)
    expected = message[:49] + "..."
    assert output == expected
