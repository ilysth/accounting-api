from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/charts", tags=["Chart of Account Resources"])

get_db = DatabaseSessionMaker("shydans_db")

@router.get("/")
async def read_charts(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Chart of Accounts. """
    return crud.get_charts(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

@router.get("/by-frame/")
async def read_charts_by_frame(frame_id: int, db: Session = Depends(get_db)):
    """ List Chart of Accounts by Frame. """
    return crud.get_charts_by_frame(db=db, frame_id=frame_id)

@router.post("/")
async def create_chart(chart: schemas.ChartCreate, db: Session = Depends(get_db)):
    """ Add Chart of Account. """
    return crud.create_chart(db=db, chart=chart)

@router.put("/{id}/", response_model=schemas.Chart)
async def update_chart(chart: schemas.ChartCreate, id: int, db: Session = Depends(get_db)):
    """ Update Account """
    return crud.update_chart(db=db, id=id, chart=chart)

@router.delete("/{id}/", response_model=schemas.Chart)
async def delete_chart(id: int, db: Session = Depends(get_db)):
    """ Remove Account """
    return crud.delete_chart(db=db, id=id)
