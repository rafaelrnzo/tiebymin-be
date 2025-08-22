from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate, UserLogin, ProfileUpdate, PasswordReset, PasswordResetRequest, UserOut
from app.schemas.token import Token
from app.api.deps import get_db
from app.api.deps.auth import get_current_active_user
from app.models.user import User
from app.repositories.review import ReviewActionRepo

router = APIRouter()

@router.post("/register", response_model=Token)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    user = await service.register_user(
        username=user_in.username,
        password=user_in.password,
        full_name=user_in.full_name,
        email=user_in.email,
        team=user_in.team
    )
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    # Generate token for new user
    access_token, expires_at = await service.create_access_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer", "expires_at": expires_at}

@router.post("/login", response_model=Token)
async def login_user(user_in: UserLogin, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    result = await service.login_for_access_token(user_in.username, user_in.password)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return {"access_token": result["access_token"], "token_type": "bearer", "expires_at": result["expires_at"]}

@router.get("/me", response_model=UserOut)
async def read_users_me(current_user: User = Depends(get_current_active_user), db: AsyncSession = Depends(get_db)):
    """Get current user info from JWT token with review statistics."""
    # Get review statistics for the current user
    review_repo = ReviewActionRepo(db)
    review_stats = await review_repo.get_user_review_stats(current_user.id)
    
    # Create user response with review statistics
    user_data = UserOut.model_validate(current_user)
    user_data.total_reviewed = review_stats['total_reviewed']
    user_data.total_approved = review_stats['total_approved']
    user_data.total_rejected = review_stats['total_rejected']
    user_data.contribution_percent = review_stats['contribution_percent']
    
    return user_data

@router.put("/profile", response_model=UserOut)
async def update_profile(
    profile_data: ProfileUpdate,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Update current user profile."""
    service = AuthService(db)
    
    # Convert profile_data to dict, excluding None values
    update_data = {k: v for k, v in profile_data.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No valid fields to update"
        )
    
    # Check if email is being updated and if it's already taken
    if 'email' in update_data and update_data['email'] != current_user.email:
        existing_user = await service.user.get_by_email(update_data['email'])
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    updated_user = await service.update_profile(str(current_user.id), update_data)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return updated_user

@router.put("/password")
async def change_password(
    password_data: PasswordReset,
    current_user: User = Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db)
):
    """Change current user password."""
    service = AuthService(db)
    
    updated_user = await service.change_password(
        str(current_user.id),
        password_data.current_password,
        password_data.new_password
    )
    
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )
    
    return {"message": "Password updated successfully"}

@router.post("/password/reset")
async def reset_password(
    reset_data: PasswordResetRequest,
    db: AsyncSession = Depends(get_db)
):
    """Reset password by email (admin functionality)."""
    service = AuthService(db)
    
    # For now, we'll use a simple approach
    # In production, you might want to send a reset link via email
    user = await service.user.get_by_email(reset_data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found with this email"
        )
    
    # Generate a temporary password (in production, send reset link instead)
    import secrets
    import string
    temp_password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(12))
    
    updated_user = await service.reset_password_by_email(reset_data.email, temp_password)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to reset password"
        )
    
    return {
        "message": "Password reset successfully",
        "temporary_password": temp_password,
        "note": "Please change your password after login"
    }
