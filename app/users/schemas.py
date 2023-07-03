from datetime   import datetime
from pydantic import BaseModel
from typing import Optional


class UsersBase(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    role: int
    creation_update: Optional[datetime] = None

class UsersCreate(UsersBase):
    pass


class Users(UsersBase):
    id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True