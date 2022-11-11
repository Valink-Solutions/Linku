from pydantic import BaseModel, EmailStr


# Utility Models
class Token(BaseModel):
    access_token: str
    token_type: str | None = 'Bearer'
    
    
class TokenData(BaseModel):
    uuid: str
    # scopes: dict | None = None
    
    
class VerifyToken(BaseModel):
    token: str
    
    
class RequestReset(BaseModel):
    email: EmailStr
    
    
class ResetPassword(BaseModel):
    token: str
    password: str
    
    
class RequestVerification(BaseModel):
    email: EmailStr
    