import hashlib
import hmac
import time


def authenticate_user(email: str, password: str):
    # Stub: real impl queries DB
    return None


def create_access_token(user_id: int, expires_in: int = 3600) -> str:
    payload = f"{user_id}:{int(time.time()) + expires_in}"
    return hmac.new(b"secret", payload.encode(), hashlib.sha256).hexdigest()
