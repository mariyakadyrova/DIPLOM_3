import random
import string

def random_email():
    s = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
    return f"ui_{s}@example.com"

def random_user_payload():
    return {"email": random_email(), "password": "password123", "name": "UI User"}
