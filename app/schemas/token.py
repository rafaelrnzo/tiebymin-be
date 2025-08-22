from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_at: str

class TokenData(BaseModel):
    username: str = None
