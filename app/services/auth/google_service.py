# app/services/auth/google_service.py
import uuid
import secrets
import requests
import base64
import hmac
import hashlib
import time
from typing import Optional

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

# If you hop across subdomains and want the cookie to be shared,
# set this to something like ".yourdomain.com". Otherwise keep None.
COOKIE_DOMAIN: Optional[str] = None

# Signed-state config
STATE_TTL_SECONDS = 600  # 10 minutes


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _unb64url(s: str) -> bytes:
    pad = "=" * (-len(s) % 4)
    return base64.urlsafe_b64decode(s + pad)


def _sign_state(nonce: str, issued_at: int) -> str:
    msg = f"{nonce}.{issued_at}".encode("utf-8")
    key = settings.SECRET_KEY.encode("utf-8")
    sig = hmac.new(key, msg, hashlib.sha256).digest()
    return _b64url(sig)


def create_state() -> str:
    """
    Creates a self-contained, signed state value that does not require server-side storage.
    Format: "<nonce>.<issued_at>.<sig>"
    """
    nonce = secrets.token_urlsafe(16)
    issued_at = int(time.time())
    sig = _sign_state(nonce, issued_at)
    return f"{nonce}.{issued_at}.{sig}"


def verify_state(state: str) -> bool:
    """
    Verifies the signed state value and checks TTL.
    """
    try:
        nonce, ts_str, sig = state.split(".", 2)
        issued_at = int(ts_str)
    except Exception:
        return False

    # TTL check
    if int(time.time()) - issued_at > STATE_TTL_SECONDS:
        return False

    expected_sig = _sign_state(nonce, issued_at)
    return hmac.compare_digest(sig, expected_sig)


def build_google_url(state: str) -> str:
    if not settings.GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="Google Client ID not configured")
    if not settings.GOOGLE_REDIRECT_URI:
        raise HTTPException(status_code=500, detail="Google Redirect URI not configured")

    params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
    }
    url = f"{GOOGLE_AUTH_URI}?{urlencode(params)}"
    print(f"🔥 Google OAuth URL: {url}")
    return url


def _set_state_cookie(resp: Response, state: str) -> None:
    """
    Cross-site safe cookie so it survives the redirect from Google back to your domain.
    """
    resp.set_cookie(
        STATE_COOKIE_NAME,
        state,
        httponly=True,
        max_age=STATE_TTL_SECONDS,
        samesite="none",       # cross-site friendly
        secure=True,           # required when SameSite=None
        path="/",
        domain=COOKIE_DOMAIN,  # keep None unless you need a parent domain
    )


def login_google(response: Response):
    try:
        state = create_state()
        url = build_google_url(state)
        print(f"🔥 Redirecting to: {url}")
        resp = RedirectResponse(url=url, status_code=302)
        _set_state_cookie(resp, state)
        return resp
    except Exception as e:
        print(f"🔥 Error in login_google: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to initiate Google login: {str(e)}")


def login_google_with_request(request: Request, response: Response, return_url: bool = False):
    try:
        state = create_state()
        url = build_google_url(state)

        if return_url:
            # Useful for Swagger/manual flows; returns URL + state for copy-paste
            return {
                "google_oauth_url": url,
                "state": state,
                "message": "Open this URL in your browser to complete OAuth",
            }

        print(f"🔥 Redirecting to: {url}")
        resp = RedirectResponse(url=url, status_code=302)
        _set_state_cookie(resp, state)
        return resp
    except Exception as e:
        print(f"🔥 Error in login_google_with_request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to initiate Google login: {str(e)}")


def callback_google(request: Request, code: str, state: str, user_repo: UserRepository):
    try:
        cookie_state = request.cookies.get(STATE_COOKIE_NAME)

        # Accept cookie match, or—if no cookie—accept a valid signed state.
        if cookie_state:
            if cookie_state != state:
                raise HTTPException(status_code=400, detail="Invalid state parameter (cookie mismatch)")
        else:
            if not verify_state(state):
                raise HTTPException(status_code=400, detail="Invalid state parameter")

        # Exchange code for tokens
        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        token_resp = requests.post(
            GOOGLE_TOKEN_URI,
            data=token_data,
            timeout=15,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if token_resp.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to get access token from Google: {token_resp.text}",
            )

        token_json = token_resp.json()
        if "error" in token_json:
            raise HTTPException(
                status_code=400,
                detail=f"Google OAuth error: {token_json.get('error_description', token_json['error'])}",
            )

        access_token = token_json.get("access_token")
        if not access_token:
            raise HTTPException(status_code=400, detail="Access token not received from Google")

        # Fetch userinfo
        headers = {"Authorization": f"Bearer {access_token}"}
        userinfo_resp = requests.get(GOOGLE_USERINFO_URI, headers=headers, timeout=15)

        if userinfo_resp.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to get user info from Google: {userinfo_resp.text}",
            )

        userinfo = userinfo_resp.json()
        email = userinfo.get("email")
        google_id = userinfo.get("sub")

        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")
        if not google_id:
            raise HTTPException(status_code=400, detail="Google ID not provided by Google")

        # Upsert user
        user = user_repo.get_by_email(email=email)
        if not user:
            user_to_create = UserCreate(
                email=email,
                first_name=userinfo.get("given_name", ""),
                last_name=userinfo.get("family_name", ""),
                google_id=google_id,
                password_hash=get_password_hash(str(uuid.uuid4())),
            )
            user = user_repo.create(user_to_create)
        elif not getattr(user, "google_id", None):
            user_repo.update_google_id(user.id, google_id)
            user.google_id = google_id

        # App token
        jwt_token = create_access_token(data={"sub": str(user.id)})

        # Clean up & redirect / return JSON
        if getattr(settings, "GOOGLE_POST_LOGIN_REDIRECT", None):
            redirect_url = f"{settings.GOOGLE_POST_LOGIN_REDIRECT}#access_token={jwt_token}&token_type=bearer"
            resp = RedirectResponse(url=redirect_url, status_code=302)
            # delete cookie (best-effort)
            resp.delete_cookie(STATE_COOKIE_NAME, path="/", samesite="none", domain=COOKIE_DOMAIN)
            return resp

        # API-style success
        return {"access_token": jwt_token, "token_type": "bearer"}

    except HTTPException:
        raise
    except Exception as e:
        print(f"Google OAuth callback error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error during Google authentication: {str(e)}")
