from fastapi.testclient import TestClient

from src.main import create_app

app = create_app(server="test")

client = TestClient(app=app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


