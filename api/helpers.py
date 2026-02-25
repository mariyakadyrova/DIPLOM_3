import random
import string

from api.client import ApiClient

API_BASE = "https://stellarburgers.education-services.ru"

REGISTER = "/api/auth/register"
LOGIN = "/api/auth/login"
USER = "/api/auth/user"


def _rand_str(n=10):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def create_user() -> dict:
    """
    Создаёт пользователя через API.
    Возвращает dict: email, password, name, accessToken
    """
    client = ApiClient(API_BASE)
    payload = {
        "email": f"test_{_rand_str(10)}@example.com",
        "password": "password123",
        "name": "UserName",
    }
    r = client.request("POST", REGISTER, json=payload)
    assert r.status_code == 200, r.text
    body = r.json()
    return {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "accessToken": body["accessToken"],
    }


def delete_user(access_token: str):
    client = ApiClient(API_BASE)
    headers = {"Authorization": access_token}
    client.request("DELETE", USER, headers=headers)
