# User Management Features

## Overview

This document describes the user management features including profile updates and password management.

## Features

### 1. Profile Management

Users can update their profile information through the `/api/v1/auth/profile` endpoint.

**Available fields for update:**
- `full_name`: User's full name
- `email`: User's email address (must be unique)
- `team`: User's team/department

**Security features:**
- Email uniqueness validation
- Only authenticated users can update their own profile
- Audit trail with updated_at and updated_by fields

### 2. Password Management

#### Change Password
Users can change their password through the `/api/v1/auth/password` endpoint.

**Requirements:**
- User must be authenticated
- Current password must be provided and verified
- New password will be hashed using bcrypt

#### Reset Password
Administrators can reset user passwords through the `/api/v1/auth/password/reset` endpoint.

**Features:**
- Generates temporary password
- Email validation
- Returns temporary password for immediate use

## API Endpoints

### Update Profile
```http
PUT /api/v1/auth/profile
Authorization: Bearer <token>

{
  "full_name": "New Name",
  "email": "newemail@example.com",
  "team": "new-team"
}
```

### Change Password
```http
PUT /api/v1/auth/password
Authorization: Bearer <token>

{
  "current_password": "oldpassword",
  "new_password": "newpassword"
}
```

### Reset Password
```http
POST /api/v1/auth/password/reset

{
  "email": "user@example.com"
}
```

## Database Changes

The user management features utilize the existing user table structure:

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    full_name VARCHAR(100),
    team VARCHAR(100),
    password TEXT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT now(),
    created_by VARCHAR(100) DEFAULT 'SYSTEM',
    updated_at TIMESTAMP DEFAULT now(),
    updated_by VARCHAR(100) DEFAULT 'SYSTEM',
    deleted_at TIMESTAMP
);
```

## Security Considerations

1. **Password Hashing**: All passwords are hashed using bcrypt
2. **Email Validation**: Email addresses are validated for format and uniqueness
3. **Authentication**: All profile and password operations require valid JWT tokens
4. **Audit Trail**: All updates are tracked with timestamps and user information
5. **Input Validation**: All inputs are validated using Pydantic schemas

## Error Handling

The API provides comprehensive error handling:

- **400 Bad Request**: Invalid input data or business rule violations
- **401 Unauthorized**: Invalid or missing authentication
- **404 Not Found**: User not found
- **500 Internal Server Error**: Server-side errors

## Usage Examples

### Update Profile
```python
import requests

# Login to get token
login_response = requests.post("http://localhost:8000/api/v1/auth/login", json={
    "username": "user",
    "password": "password"
})
token = login_response.json()["access_token"]

# Update profile
headers = {"Authorization": f"Bearer {token}"}
response = requests.put("http://localhost:8000/api/v1/auth/profile", 
    headers=headers,
    json={
        "full_name": "John Doe",
        "email": "john@example.com"
    }
)
```

### Change Password
```python
response = requests.put("http://localhost:8000/api/v1/auth/password",
    headers=headers,
    json={
        "current_password": "oldpassword",
        "new_password": "newpassword"
    }
)
```

## Testing

The features include comprehensive test coverage in `tests/api/test_auth.py`:

- User registration and login
- Profile updates
- Password changes
- Password resets
- Error handling

Run tests with:
```bash
pytest tests/api/test_auth.py -v
```

## Future Enhancements

1. **Email Verification**: Add email verification for new registrations
2. **Password Strength**: Implement password strength requirements
3. **Two-Factor Authentication**: Add 2FA support
4. **Session Management**: Add session tracking and management
5. **Rate Limiting**: Implement rate limiting for security endpoints 