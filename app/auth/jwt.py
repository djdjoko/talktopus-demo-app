import jwt
import time
from typing import Optional


SECRET_KEY = "change-me-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 900      # 15 minutes
REFRESH_TOKEN_EXPIRE = 604800  # 7 days


def create_token_pair(user_id: int) -> dict:
    now = int(time.time())
    access = jwt.encode(
        {"sub": user_id, "exp": now + ACCESS_TOKEN_EXPIRE, "type": "access"},
        SECRET_KEY, algorithm=ALGORITHM,
    )
    refresh = jwt.encode(
        {"sub": user_id, "exp": now + REFRESH_TOKEN_EXPIRE, "type": "refresh", "jti": f"{user_id}-{now}"},
        SECRET_KEY, algorithm=ALGORITHM,
    )
    return {"access_token": access, "refresh_token": refresh}


def verify_token(token: str, expected_type: str = "access") -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != expected_type:
            return None
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def rotate_refresh_token(refresh_token: str) -> Optional[dict]:
    payload = verify_token(refresh_token, expected_type="refresh")
    if payload is None:
        return None
    return create_token_pair(payload["sub"])
