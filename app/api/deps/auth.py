from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.schemas.token import TokenData
from app.services.auth_service import AuthService
from app.api.deps import get_db
from app.models.user import User
from typing import Optional

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Get current user from JWT token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    auth_service = AuthService(db)
    user = await auth_service.user.get_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Get current active user (not deleted)."""
    if current_user.deleted_at is not None:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Optional security scheme that does not automatically return 403 when the
# Authorization header is missing. This allows endpoints to accept anonymous
# requests while still supporting authenticated users when a valid bearer token
# is provided.
security_optional = HTTPBearer(auto_error=False)

async def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_optional),
    db: AsyncSession = Depends(get_db)
) -> Optional[User]:
    """Return the current user if a valid bearer token is supplied; otherwise
    return None without raising an exception. This is useful for endpoints that
    can be accessed both anonymously and by authenticated users.
    """
    # If no credentials were supplied, treat as anonymous request.
    if credentials is None:
        return None

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        # Invalid token supplied – treat as anonymous rather than raising to
        # keep behaviour optional. Clients with bad tokens will be considered
        # unauthenticated but still receive successful responses.
        return None

    auth_service = AuthService(db)
    user = await auth_service.user.get_by_username(username=token_data.username)
    # If user is not found or is soft-deleted, also treat as anonymous.
    if user is None or user.deleted_at is not None:
        return None

    return user
