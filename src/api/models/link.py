from typing import Optional
from pydantic import BaseModel, Field, HttpUrl

class LinkInDB(BaseModel):
    url: str = Field(...)
    description: str = Field(...)
    
    favicon: str = Field(...)
    is_protected: bool = Field(...)
    
    created_at: float = Field(...)
    updated_at: float = Field(...)
    
    
class LinkCreate(BaseModel):
    short_code: Optional[str] = Field(default=None, min_length=3, max_length=15)
    url: HttpUrl = Field(...)
    description: Optional[str] = Field(default=None)
    is_protected: Optional[bool] = Field(default=False)
    
    
class LinkUpdate(BaseModel):
    url: Optional[HttpUrl] = Field(default=None)
    description: Optional[str] = Field(default=None)
    is_protected: Optional[bool] = Field(default=None)
    

class LinkRead(BaseModel):
    short_code: str = Field(alias="key", title="short_code")
    url: str = Field(...)
    description: str = Field(...)
    
    favicon: str = Field(...)
    is_protected: bool = Field(...)
    
    created_at: float = Field(...)
    updated_at: float = Field(...)