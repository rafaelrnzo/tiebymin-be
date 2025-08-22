# Authentication API Specification

## Base URL
```
/api/v1/auth
```

## Endpoints

### 1. Register User
**POST** `/register`

Register a new user account.

**Request Body:**
```json
{
  "username": "string",
  "password": "string",
  "email": "string",
  "full_name": "string (optional)",
  "team": "string (optional)"
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_at": "string"
}
```

### 2. Login User
**POST** `/login`

Authenticate user and get access token.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_at": "string"
}
```

### 3. Get Current User
**GET** `/me`

Get current user information from JWT token.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "id": "uuid",
  "username": "string",
  "full_name": "string",
  "email": "string",
  "team": "string",
  "created_at": "datetime",
  "created_by": "string",
  "updated_at": "datetime",
  "updated_by": "string"
}
```

### 4. Update Profile
**PUT** `/profile`

Update current user profile information.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "full_name": "string (optional)",
  "email": "string (optional)",
  "team": "string (optional)"
}
```

**Response:**
```json
{
  "id": "uuid",
  "username": "string",
  "full_name": "string",
  "email": "string",
  "team": "string",
  "created_at": "datetime",
  "created_by": "string",
  "updated_at": "datetime",
  "updated_by": "string"
}
```

**Notes:**
- All fields are optional
- Email must be unique if provided
- Only provided fields will be updated

### 5. Change Password
**PUT** `/password`

Change current user password.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "current_password": "string",
  "new_password": "string"
}
```

**Response:**
```json
{
  "message": "Password updated successfully"
}
```

**Notes:**
- Current password must be correct
- New password will be hashed before storage

### 6. Reset Password
**POST** `/password/reset`

Reset password by email (admin functionality).

**Request Body:**
```json
{
  "email": "string"
}
```

**Response:**
```json
{
  "message": "Password reset successfully",
  "temporary_password": "string",
  "note": "Please change your password after login"
}
```

**Notes:**
- Generates a temporary password
- In production, consider sending reset link via email instead
- User should change password after login

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Error message"
}
```

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 404 Not Found
```json
{
  "detail": "User not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Authentication

Most endpoints require authentication via JWT Bearer token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Security Notes

1. Passwords are hashed using bcrypt
2. JWT tokens have expiration time
3. Email addresses must be unique
4. Profile updates validate email uniqueness
5. Password changes require current password verification
