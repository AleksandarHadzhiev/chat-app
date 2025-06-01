import json

import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.users import login_user as access_token


test_data = [
    (0, 0, {"status": 400, "json": {"fail": ["invalid-group_id", "invalid-user_id"]}}),
    (0, 1, {"status": 400, "json": {"fail": ["invalid-group_id"]}}),
    (1, 0, {"status": 400, "json": {"fail": ["invalid-user_id"]}}),
    (2, 1, {"status": 200, "json": {"message": "deleted"}}),
]


@pytest.mark.order(7)
@pytest.mark.parametrize("id, admin, outcome", test_data)
def test_delete_group(api, access_token, id, admin, outcome):
    access_token = access_token
    headers={"Authorization": access_token}
    response = api.delete(f"/groups/{id}/{admin}", headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
