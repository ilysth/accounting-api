from datetime   import datetime
from pydantic import BaseModel
from typing import Optional


# class UserBase(BaseModel):
#     username: str
#     password: str
#     first_name: str
#     last_name: str
#     role: int
#     creation_update: Optional[datetime] = None

# class UserCreate(UserBase):
#     pass


# class User(UserBase):
#     id: int

#     class Config:
#         orm_mode = True

# class UserLogin(BaseModel):
#     username: str
#     password: str
#     first_name: str
#     last_name: str
#     role: int

#     class Config:
#         orm_mode = True


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: Optional[str] = None

class ApplicationFile(BaseModel):
    file_name: str
    file_size: int
    mime_type: str


class ApplicationBase(BaseModel):
    app_id: int
    platform_id: int
    app_architecture: int
    app_version: int
    app_name: str
    app_zip: str
    download_url: str
    compressed_size: Optional[str] = ""
    version_notes: Optional[str] = ""


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(ApplicationBase):
    app_id: Optional[int] = None
    platform_id: Optional[int] = None
    app_architecture: Optional[int] = None
    app_version: Optional[int] = None
    app_name: Optional[str] = None
    app_zip: Optional[str] = None
    download_url: Optional[str] = None
    compressed_size: Optional[str] = None
    version_notes: Optional[str] = None


class Application(ApplicationBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    role: int
    fname: str
    lname: str
    email: str = None
    contact: str
    image: str
    apps: str
    country: str = None
    creation_update: Optional[datetime] = None
    is_superuser: bool = 0


class UserCreate(UserBase):
    password: str
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True