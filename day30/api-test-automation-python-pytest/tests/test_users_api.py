import pytest
from utils.api_client import APIClient

client = APIClient()


def test_get_single_user_status_and_fields():
    """
    GET /users/1 returns 200 and contains expected fields.
    """
    response = client.get("/users/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    # Basic contract / field presence
    for key in ["name", "username", "email", "address"]:
        assert key in data, f"Missing key in user response: {key}"


@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_get_multiple_users_status_200(user_id):
    """
    Data-driven test: GET /users/{id} for multiple ids.
    """
    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == user_id


def test_get_nonexistent_user_returns_404():
    """
    Negative test: GET /users/99999 should return 404.
    """
    response = client.get("/users/99999")

    assert response.status_code == 404

