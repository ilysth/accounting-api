from datetime   import datetime
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    role: int
    creation_update: Optional[datetime] = None

class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    role: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None