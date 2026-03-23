from fastapi import APIRouter, Depends, HTTPException
from app.auth.models import LoginRequest, TokenResponse
from app.auth.service import authenticate_user, create_access_token

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest):
    user = await authenticate_user(req.email, req.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(user_id=user.id)
    return TokenResponse(access_token=token, token_type="bearer")


@router.post("/refresh")
async def refresh_token():
    # TODO: implement refresh token rotation
    raise HTTPException(status_code=501, detail="Not implemented yet")
