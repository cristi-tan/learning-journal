import requests


class APIClient:
    """
    Simple API client wrapper around the JSONPlaceholder base URL.
    """

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url.rstrip("/")

    def _build_url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, **kwargs) -> requests.Response:
        """
        Send a GET request to the given path.
        Example: client.get("/users/1")
        """
        url = self._build_url(path)
        return requests.get(url, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        """
        Send a POST request to the given path.
        Example: client.post("/posts", json=payload)
        """
        url = self._build_url(path)
        return requests.post(url, **kwargs)
