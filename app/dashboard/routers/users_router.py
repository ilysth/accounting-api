from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import DatabaseSessionMaker
from app.dashboard import crud, schemas

router = APIRouter(prefix="/users", tags=["Users Resources"])

get_db = DatabaseSessionMaker("shydans_db")

@router.get("/login/")
async def login_user(username: str, password: str, db: Session = Depends(get_db)):
    return crud.login(username=username, password=password, db=db)

@router.post("/")
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """ Add User. """
    return crud.create_user(db=db, user=user)