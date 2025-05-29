
from fastapi.testclient import TestClient
import pytest

from src.main import create_app


test_data = [
    (2,"s",{"type": "message", "data": {"user_id": int(0), 
                "author": "", 
                "content": "", 
                "group_id": int(0), 
                "code": "",
                "created_at": ""}}, {'type': 'fail', 'data': ['empty-author', 'empty-code', 'empty-content', 'empty-created_at', 'undefined-group', 'undefined-user', 'is-not-member']}),
    (2,"s",{"type": "message", "data": {"user_id": int(0), 
                "author": "s", 
                "content": "s", 
                "group_id": int(0), 
                "code": "s",
                "created_at": "s"}}, {'type': 'fail', 'data': ['undefined-group', 'undefined-user', 'is-not-member']}),
    (2,"s",{"type": "message", "data": {"user_id": int(2), 
                "author": "s", 
                "content": "s", 
                "group_id": int(1), 
                "code": "s",
                "created_at": "s"}}, {'type': 'fail', 'data': ['is-not-member']}),
    (1,"s",{"type": "message", "data": {"user_id": int(1), 
                "author": "s", 
                "content": "s", 
                "group_id": int(1), 
                "code": "wqwe",
                "created_at": "as"}}, {'type': 'message', 'data': {'user_id': 1, 'author': 's', 'content': 's', 'group_id': 1, 'code': 'wqwe', 'created_at': 'as'}}),
    (1,"s",{"type": "message", "data": {"user_id": int(1), 
                "author": "s", 
                "content": "word", 
                "group_id": int(1), 
                "code": "wqwe",
                "created_at": "as"}}, {'type': 'fail', 'data': ['offensive-speech']}),

]



@pytest.mark.order(8)
@pytest.mark.parametrize("id, username, data, outcome", test_data)
def test_ws_connection(id, username, data, outcome):
    app = create_app(server="test")
    client = TestClient(app=app)
    ws_url = f'/ws/{id}/{username}/1'
    with client.websocket_connect(ws_url) as websocket:
        websocket.send_json(data=data)
        message = websocket.receive_json()
        assert message == outcome
