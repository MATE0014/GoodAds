from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy import select
from jose import JWTError

from app.core import security
from app.db.session import get_db
from app.models import user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> user.User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = security.decode_access_token(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    result = await db.execute(select(user.User).where(user.User.id == int(user_id)))
    found_user = result.scalars().first()
    if found_user is None:
        raise credentials_exception
    return found_user
