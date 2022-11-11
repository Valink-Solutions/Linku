from datetime import datetime, timedelta
from time import time

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from core import settings
from core.connections import auth_db

from models import Token, TokenData
from models.auth import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def create_access_token(user_uuid: str, expires_delta: timedelta | None = None):
    
    to_encode = TokenData(uuid=user_uuid).dict()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET, algorithm=settings.ALGORITHM)
    
    return Token(access_token=encoded_jwt)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET, algorithms=[settings.ALGORITHM])
        
        uuid: str = payload.get("uuid")
        exp: time = payload.get("exp")
    
        if uuid is None:
            raise credentials_exception
        
        if float(exp) <= time():
            raise credentials_exception
        
    except JWTError:
        raise credentials_exception
    
    # try:
    #     statement = select(User).where(User.uuid == uuid).options(selectinload(User.stripe_customer))
    #     results = await session.execute(statement)
    
    #     user = results.scalars().first()
        
    # except SQLAlchemyError:
    #     raise credentials_exception
    
    user = None
    
    if not user:
        raise credentials_exception
    
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User was logged out.")
    
    return user


async def get_current_superuser(current_user: User = Depends(get_current_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized to access this resource.")
    
    return current_user
        