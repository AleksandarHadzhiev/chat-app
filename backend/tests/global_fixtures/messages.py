import json
from freezegun import freeze_time
import pytest
from fastapi.testclient import TestClient

from src.main import create_app


@freeze_time("2023-01-01 12:00:00")
@pytest.fixture(scope="session")
def send_message():
    data = {
        "type": "message",
        "data": {
            "content": "s",
            "group_id": int(1),
            "created_at": "as",
        },
    }
    outcome = {
        "type": "message",
        "data": {
            "user_id": 1,
            "author": "administrator",
            "content": "s",
            "group_id": 1,
            "code": "1-1-2023-01-01-12-00-00",
            "created_at": "as",
        },
    }
    app = create_app(server="test")["app"]
    client = TestClient(app=app)
    response = client.post("/login", content=json.dumps({"email": "aleks_01_@gmail.com", "password": "admin"}))
    assert response.status_code == 200
    assert  "access_token" in response.json()
    token = response.json()["access_token"]
    ws_url = f"/ws/{token}/1"
    with client.websocket_connect(ws_url) as websocket:
        websocket.send_json(data=data)
