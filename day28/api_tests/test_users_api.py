import pytest
import requests

@pytest.mark.parametrize("user_id", [1, 2, 3, 4])
def test_users_status_code(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    assert response.status_code == 200


def test_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/99999")
    assert response.status_code == 404

def test_create_post():
    payload = {
        "title": "Automation test",
        "body": "API testing is cool",
        "userId": 1
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

def test_user_structure():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    expected_keys = ["id", "name", "username", "email", "address"]

    for key in expected_keys:
        assert key in data

test_data = [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
]

@pytest.mark.parametrize("user_id,expected_name", test_data)
def test_user_names(user_id, expected_name):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    data = requests.get(url).json()

    assert data["name"] == expected_name