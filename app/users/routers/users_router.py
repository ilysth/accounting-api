from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.users import crud, schemas
from app.users.database import SessionLocal
from typing import List, Optional

router = APIRouter(prefix="/users", tags=["Users Resources"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Get All Suppliers
# @router.get("/login/")
# async def login_user(username: str, password: str, db: Session = Depends(get_db)):
#     return crud.login(username=username, password=password, db=db)

@router.post("/login/", response_model=schemas.Users)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.login(db=db, user=user)

# Create Chart of Account
@router.post("/")
async def create_user(user: schemas.UsersCreate, db: Session = Depends(get_db)):
    """ Add User. """
    return crud.create_user(db=db, user=user)