from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from typing import List
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/suppliers", tags=["Supplier Resources"])

get_db = DatabaseSessionMaker("shydans_db")

@router.get("/")
async def read_supplier(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Supplier. """
    return crud.get_suppliers(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

@router.post("/")
async def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    """ Add Supplier. """
    return crud.create_supplier(db=db, supplier=supplier)

@router.put("/{id}", response_model=schemas.Supplier)
async def update_supplier(supplier: schemas.SupplierCreate, id: int, db: Session = Depends(get_db)):
    """ Update Supplier """
    return crud.update_supplier(db=db, id=id, supplier=supplier)

@router.delete("/{id}", response_model=schemas.Supplier)
async def delete_supplier(id: int, db: Session = Depends(get_db)):
    """ Remove Supplier """
    return crud.delete_supplier(db=db, id=id)