from pydantic import BaseModel, EmailStr
from typing import Literal

class UserBase(BaseModel):
    username: str
    email: EmailStr
    user_type: Literal["business", "society"]

class UserCreate(UserBase):
    password: str  # Plain password from user input

class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
