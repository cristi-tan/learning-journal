import requests


class APIClient:
    """
    Simple wrapper client for JSONPlaceholder API.
    """

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url.rstrip("/")

    def _build_url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, **kwargs) -> requests.Response:
        return requests.get(self._build_url(path), **kwargs)
