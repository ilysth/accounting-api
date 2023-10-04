from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/frames", tags=["Account Frame Resources"])

get_db = DatabaseSessionMaker("shydans_db")


@router.get("/")
async def read_frames(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Account Frame. """
    return crud.get_frames(db=db, sort_direction=sort_direction, skip=skip, limit=limit)


@router.post("/")
async def create_frame(frame: schemas.FrameCreate, db: Session = Depends(get_db)):
    """ Add Account Frame. """
    return crud.create_frame(db=db, frame=frame)


@router.put("/{id}/", response_model=schemas.Frame)
async def update_frame(frame: schemas.FrameCreate, id: int, db: Session = Depends(get_db)):
    """ Update Account """
    return crud.update_frame(db=db, id=id, frame=frame)


@router.delete("/{id}/", response_model=schemas.Frame)
async def delete_frame(id: int, db: Session = Depends(get_db)):
    """ Remove Account """
    return crud.delete_frame(db=db, id=id)
