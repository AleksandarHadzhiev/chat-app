import json

import pytest
from fastapi.testclient import TestClient
from freezegun import freeze_time

from src.main import create_app

test_data = [
    (
        {
            "type": "message",
            "data": {
                "content": "",
                "group_id": int(0),
                "created_at": "",
            },
        },
        {
            "type": "fail",
            "data": [
                "empty-content",
                "empty-created_at",
                "undefined-group",
                "is-not-member",
            ],
        },
    ),
    (
        {
            "type": "message",
            "data": {
                "content": "s",
                "group_id": int(0),
                "created_at": "s",
            },
        },
        {
            "type": "fail",
            "data": ["undefined-group", "is-not-member"],
        },
    ),
    (
        {
            "type": "message",
            "data": {
                "content": "s",
                "group_id": int(1),
                "created_at": "as",
            },
        },
        {
            "type": "message",
            "data": {
                "content": "s",
                "group_id": 1,
                "created_at": "as",
                "user_id": 1,
                "author": "administrator",
                "code": "1-1-2023-01-01-12-00-00",
            },
        },
    ),
    (
        {
            "type": "message",
            "data": {
                "content": "word",
                "group_id": int(1),
                "created_at": "as",
            },
        },
        {"type": "fail", "data": ["offensive-speech"]},
    ),
]


@freeze_time("2023-01-01 12:00:00")
@pytest.mark.order(8)
@pytest.mark.parametrize("data, outcome", test_data)
def test_ws_connection(data, outcome):
    app = create_app(server="test")["app"]
    client = TestClient(app=app)
    response = client.post(
        "/login",
        content=json.dumps({"email": "aleks_01_@gmail.com", "password": "admin"}),
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    token = response.json()["access_token"]
    ws_url = f"/ws/{token}/1"
    with client.websocket_connect(ws_url) as websocket:
        websocket.send_json(data=data)
        message = websocket.receive_json()
        assert message == outcome
