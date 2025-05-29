import pytest
from src.main import create_app
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def send_message():
    data = {"type": "message", "data": {"user_id": int(1), 
                "author": "s", 
                "content": "s", 
                "group_id": int(1), 
                "code": "wqwe",
                "created_at": "as"}}
    outcome = {'type': 'message', 'data': {'user_id': 1, 'author': 's', 'content': 's', 'group_id': 1, 'code': 'wqwe', 'created_at': 'as'}}
    app = create_app(server="test")
    client = TestClient(app=app)
    ws_url = f'/ws/1/s/1'
    with client.websocket_connect(ws_url) as websocket:
        websocket.send_json(data=data)
        message = websocket.receive_json()
        assert message == outcome