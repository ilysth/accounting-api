from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.inventory import crud, schemas
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/items", tags=["Inventory Items"])

get_db = DatabaseSessionMaker("shydans_db")

@router.get("/")
async def read_items(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Items. """
    return crud.get_items(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

@router.post("/")
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    """ Add Item. """
    return crud.create_item(db=db, item=item)

@router.put("/{id}/", response_model=schemas.Item)
async def update_item(item: schemas.ItemCreate, id: int, db: Session = Depends(get_db)):
    """ Update Item """
    return crud.update_item(db=db, id=id, item=item)

@router.delete("/{id}/", response_model=schemas.Item)
async def delete_item(id: int, db: Session = Depends(get_db)):
    """ Remove Item """
    return crud.delete_item(db=db, id=id)