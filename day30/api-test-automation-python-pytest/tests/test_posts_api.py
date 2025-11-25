from utils.api_client import APIClient

client = APIClient()


def test_get_posts_list_status_200_and_not_empty():
    """
    Basic check: GET /posts returns 200 and a non-empty list.
    """
    response = client.get("/posts")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_create_post_returns_201_and_echoes_body():
    """
    POST /posts should create a resource (201) and echo back sent data.
    Note: JSONPlaceholder is a fake API, so it fakes creation but is
    perfect for testing.
    """
    payload = {
        "title": "Hello world",
        "body": "This is a test post.",
        "userId": 1,
    }

    response = client.post("/posts", json=payload)

    assert response.status_code == 201

    data = response.json()
    # Contract: response has at least these keys
    for key in ["id", "title", "body", "userId"]:
        assert key in data

    # Data echo check
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
