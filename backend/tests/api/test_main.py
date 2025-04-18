import json
from fastapi.testclient import TestClient

from src.main import create_app

app = create_app(server="test")

client = TestClient(app=app)


def test_read_main():
    response = client.get("/languages/translations/EN/login")
    assert response.status_code == 200
    outcome = response.json()
    assert outcome == '{"translations": {"header": "Welcome back", "login": "Login", "email": "Email", "exampple": "example@gmail.com", "password": "Password", "forgot-password": "Forgot password?", "here": "Here", "button": "Sign in", "account": "You don\'t have an account?", "signup": "Sing up", "fail": "Failed due to: ", "empty-email": "Empty email", "empty-password": "Empty password", "wrong-credentials": "Either email or password is incorrect"}}'