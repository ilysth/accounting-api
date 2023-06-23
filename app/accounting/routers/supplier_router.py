from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.accounting import crud, schemas
from app.accounting.database import SessionLocal
from typing import List

router = APIRouter(prefix="/suppliers", tags=["Supplier Resources"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get All Suppliers
@router.get("/")
async def read_suppliers(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Suppliers. """
    return crud.get_suppliers(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

# Get All Suppliers {Names}
@router.get("/names/", response_model=List)
async def get_names(db: Session = Depends(get_db)) -> List:
    """ List Supplier Names """
    supplier = crud.get_suppliers(db=db)

    # Last Name List
    last_name = [supplier.last_name for supplier in supplier]

    # First Name List
    first_name = [supplier.first_name for supplier in supplier]

    # Names (Lname, Fname)
    names_list = [f"{last}, {first}" for first, last in zip(first_name, last_name)]

    return names_list

# Create Supplier
@router.post("/")
async def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    """ Add Supplier. """
    return crud.create_supplier(db=db, supplier=supplier)

@router.put("/{id}", response_model=schemas.Supplier)
async def update_supplier(supplier: schemas.SupplierCreate, id: int, db: Session = Depends(get_db)):
    """ Update Supplier """
    return crud.update_supplier(db=db, id=id, supplier=supplier)

# Remove Journal Entry
@router.delete("/{id}", response_model=schemas.Supplier)
async def delete_supplier(id: int, db: Session = Depends(get_db)):
    """ Remove Supplier """
    return crud.delete_supplier(db=db, id=id)