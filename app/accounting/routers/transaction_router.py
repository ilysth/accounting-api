from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/transactions", tags=["Transaction Resources"])

get_db = DatabaseSessionMaker("shydans_db")


@router.get("/")
async def read_transactions(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List of Transacations """
    return crud.get_transactions(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

@router.post("/")
async def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    """ Add Transacation """
    return crud.create_transaction(db=db, transaction=transaction)

@router.put("/{id}", response_model=schemas.Transaction)
async def update_transaction(transaction: schemas.TransactionCreate, id: int, db: Session = Depends(get_db)):
    """ Update Transacation """
    return crud.update_transaction(db=db, id=id, transaction=transaction)

@router.delete("/{id}", response_model=schemas.Transaction)
async def delete_transaction(id: int, db: Session = Depends(get_db)):
    """ Remove Transacation """
    return crud.delete_transaction(db=db, id=id)