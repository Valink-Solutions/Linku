from datetime import datetime
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr, validator

from nanoid import generate

from app.models.links import Link, Tree
from app.models.stripe import StripeCustomer

# Main Auth Models
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uuid: str = Field(default_factory=lambda: generate(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456_', size=20), unique=True, index=True)
    
    name: str | None = Field(default="J Doe")
    
    picture: str | None = Field(default="https://picsum.photos/200")
    
    email: str = Field(unique=True, index=True)
    hashed_password: str = Field(default=None)
    
    is_active: bool = Field(default=False)
    is_superuser: bool = Field(default=False, index=True)
    is_verified: bool = Field(default=False, index=True)
    
    account_type: str = Field(default="BASIC", index=True)
    
    stripe_customer: Optional["StripeCustomer"] = Relationship(sa_relationship_kwargs={'uselist': False}, back_populates="user")
    
    links: List["Link"] = Relationship(back_populates="user")
    trees: List["Tree"] = Relationship(back_populates="user")
    
    # scopes: dict | None = Field(default=None)

    accessed_at: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ReturnUser(SQLModel):
    uuid: str
    
    name: str | None = None
    
    picture: str
    
    email: str

    is_active: bool
    is_superuser: bool
    is_verified: bool
    
    account_type: str
    
    # scopes: dict | None = None
    
    accessed_at: datetime
    updated_at: datetime
    

class ReadUser(SQLModel):
    id: str
    uuid: str
    
    name: str | None = None
    
    picture: str
    
    email: str

    is_active: bool
    is_superuser: bool
    is_verified: bool
    
    account_type: str
    
    # scopes: Optional[dict] = None
    
    accessed_at: datetime
    created_at: datetime
    updated_at: datetime
    
    
class CreateUser(SQLModel):
    name: str | None = None
    email: EmailStr
    password: str
    
    
    @validator("email")
    def lower_email(cls, v):
        return v.lower()
    
    
    @validator("password")
    def check_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters.")
        
        return v
    
    
class PatchUser(SQLModel):
    name: str | None = None
    
    email: str | None = None
    
    is_superuser: bool | None = None
    is_verified: bool | None = None
    
    account_type: str | None = None
    
