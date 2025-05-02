from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from app import models
from app.schemas import user as schemas

from app.core import security
from app.db.session import get_db

from app.core.deps import get_current_user


router = APIRouter()

# Register endpoint
@router.post("/register", response_model=schemas.UserOut)
async def register(user_create: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user with email already exists
    result = await db.execute(select(models.User).where(models.User.email == user_create.email))
    user = result.scalars().first()
    
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password
    hashed_password = security.hash_password(user_create.password)
    db_user = models.User(
        username=user_create.username,
        email=user_create.email,
        hashed_password=hashed_password,
        user_type=user_create.user_type
    )
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Login endpoint
@router.post("/login")
async def login( form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    result = await db.execute(select(models.User).where(models.User.email == form_data.username))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = security.create_access_token(data={"sub": str(user.id),
                                                      "user_type": str(user.user_type)
                                                      })
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserOut)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user