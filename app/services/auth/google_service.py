import uuid, secrets, requests
from urllib.parse import urlencode
from fastapi import HTTPException, Request, Response
from fastapi.responses import RedirectResponse

from app.core.config import settings
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.utils.password_utils import get_password_hash
from app.services.auth.token_service import create_access_token

GOOGLE_AUTH_URI = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URI = "https://oauth2.googleapis.com/token"
GOOGLE_USERINFO_URI = "https://www.googleapis.com/oauth2/v3/userinfo"
SCOPES = ["openid", "email", "profile"]
STATE_COOKIE_NAME = "g_state"

def build_google_url(state: str) -> str:
    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
    }
    return f"{GOOGLE_AUTH_URI}?{urlencode(params)}"

def login_google(response: Response):
    state = secrets.token_urlsafe(24)
    url = build_google_url(state)
    resp = RedirectResponse(url)
    resp.set_cookie(STATE_COOKIE_NAME, state, httponly=True, max_age=600, samesite="lax")
    return resp

def callback_google(request: Request, code: str, state: str, user_repo: UserRepository):
    cookie_state = request.cookies.get(STATE_COOKIE_NAME)
    if not cookie_state or cookie_state != state:
        raise HTTPException(status_code=400, detail="Invalid state")

    token_data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_resp = requests.post(GOOGLE_TOKEN_URI, data=token_data, timeout=15)
    token_json = token_resp.json()

    access_token = token_json.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Google access token missing")

    headers = {"Authorization": f"Bearer {access_token}"}
    userinfo_resp = requests.get(GOOGLE_USERINFO_URI, headers=headers, timeout=15)
    userinfo = userinfo_resp.json()

    email = userinfo.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Email not available")

    user = user_repo.get_by_email(email=email)
    if not user:
        user_to_create = UserCreate(
            email=email,
            first_name=userinfo.get("given_name", ""),
            last_name=userinfo.get("family_name", ""),
            google_id=userinfo.get("sub"),
            password_hash=get_password_hash(str(uuid.uuid4())),
        )
        user = user_repo.create(user_to_create)
    elif not user.google_id:
        user_repo.update_google_id(user.id, userinfo.get("sub"))

    jwt_token = create_access_token(data={"sub": str(user.id)})
    if settings.GOOGLE_POST_LOGIN_REDIRECT:
        redirect_url = f"{settings.GOOGLE_POST_LOGIN_REDIRECT}#access_token={jwt_token}&token_type=bearer"
        return RedirectResponse(redirect_url)
    return {"access_token": jwt_token, "token_type": "bearer"}
