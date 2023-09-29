from datetime import datetime, timedelta
from typing import Optional

from dotenv import dotenv_values
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from fastapi import Depends, FastAPI, HTTPException

config = dotenv_values("env/.env")
mysql_password = config["MYSQL_ROOT_PASSWORD"]
mysql_host = config["MYSQL_HOST"]
mysql_port = config["MYSQL_PORT"]
db_name = config['DB_NAME']

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:{mysql_password}@{mysql_host}:{mysql_port}/{db_name}"

# Definitions for the various values needed to generate a JWT token
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_HOURS = 720  # 30 days

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# SQLAlchemy model


class User(Base):
    __tablename__ = "dashboard_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)


# Pydantic models
class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=2)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user(db: Session, username: str, password: Optional[str] = None):
    user_with_name = db.query(User).filter(User.username == username)
    if password is not None:
        user = user_with_name.filter(User.password == password).one_or_none()
    else:
        user = user_with_name.one_or_none()

    if user is None:
        return None
    else:
        return UserLogin.from_orm(user)


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        token_data = TokenData(username=username)
    except JWTError:
        return None
    user = get_user(username=token_data.username, db=db)
    if user is None:
        return None
    return user


async def get_current_active_user(current_user: UserLogin = Depends(get_current_user)):
    return current_user


# Used to generate login tokens.
@app.post("/token/", response_model=Token)
async def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = get_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(hours=ACCESS_TOKEN_HOURS)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/verify/")
async def validate_jwt(current_user: UserLogin = Depends(get_current_active_user)):
    credentials_exception = JSONResponse(
        status_code=401,
        content={"detail": "Could not validate credentials"},
        headers={"WWW-Authenticate": "Bearer"},
    )

    if current_user is None:
        return credentials_exception
    else:
        return {"active": True}
