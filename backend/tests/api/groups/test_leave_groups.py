import json

import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.users import login_user as access_token

test_data = [
    (0, 0, {"status": 400, "json": {"fail": ["invalid-group_id", "invalid-user_id"]}}),
    (1, 0, {"status": 400, "json": {"fail": ["invalid-group_id"]}}),
    (0, 1, {"status": 400, "json": {"fail": ["invalid-user_id"]}}),
    (1, 2, {"status": 400, "json": {"fail": "not-member"}}),
    (2, 2, {"status": 200, "json": {"message": "left"}}),
]


@pytest.mark.order(4)
@pytest.mark.parametrize("account_id, group_id, outcome", test_data)
def test_leave_groups(api, access_token, account_id, group_id, outcome):
    access_token = access_token
    headers = {"Authorization": access_token}
    response = api.post(f"groups/{account_id}/leave/{group_id}", headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
