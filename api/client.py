import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def request(self, method: str, path: str, headers=None, json=None):
        return self.session.request(
            method=method,
            url=f"{self.base_url}{path}",
            headers=headers,
            json=json,
            timeout=20,
        )
