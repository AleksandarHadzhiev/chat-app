import pytest

from tests.global_fixtures.boot_up import client as api
from tests.global_fixtures.users import login_user as access_token
test_data = [
    (
        "/groups/",
        {
            "status": 200,
            "json": {
                "groups": [
                    {
                        "id": 1,
                        "title": "General Group Chat",
                        "admin_id": 1,
                        "members": [
                            {"id": 1, "name": "administrator"},
                            {"id": 2, "name": "test-01"},
                        ],
                    }
                ]
            },
        },
    ),
    (
        "/groups/1",
        {
            "status": 200,
            "json": {
                "groups": [
                    {
                        "id": 1,
                        "title": "General Group Chat",
                        "admin_id": 1,
                        "members": [{"id": 1, "name": "administrator"}],
                    }
                ]
            },
        },
    ),
    ("/groups/25", {"status": 200, "json": {"groups": []}}),
    ("/groups/0", {"status": 200, "json": {"groups": []}}),
    ("/groups/s", {"status": 400, "json": {"fail": "invalid"}}),
]


@pytest.mark.order(1)
@pytest.mark.parametrize("url, outcome", test_data)
def test_groups(api, access_token, url, outcome):
    access_token = access_token
    headers={"Authorization": access_token}
    response = api.get(url=url, headers=headers)
    assert response.status_code == outcome["status"]
    assert response.json() == outcome["json"]
