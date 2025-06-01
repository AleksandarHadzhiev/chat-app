import json

import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.messages import send_message as message
from tests.global_fixtures.users import login_user as access_token


test_data = [
    ("/messages", {"status": 400, "json": {"fail": "Incorrect data"}}),
    (
        "/messages?code=&group_id=&user_id=",
        {"status": 400, "json": {"fail": "Incorrect data"}},
    ),
    (
        "/messages?some=&other=&queries=",
        {"status": 400, "json": {"fail": "Incorrect data"}},
    ),
    (
        "/messages?code=s&group_id=0&user_id=s",
        {"status": 400, "json": {"fail": "Incorrect data"}},
    ),
    (
        "/messages?code=wqwe&group_id=1&user_id=1",
        {"status": 200, "json": {"message": "success"}},
    ),
]


@pytest.mark.order(12)
@pytest.mark.parametrize("url, outcome", test_data)
def test_delete_message(api, access_token, message, url, outcome):
    headers = {
        "Authorization": access_token
    }
    response = api.delete(url, headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
