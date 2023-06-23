from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.accounting import crud, schemas
from app.accounting.database import SessionLocal
from typing import List

router = APIRouter(prefix="/journals", tags=["Journal Entry Resources"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get All Journal Entry
@router.get("/")
async def read_journals(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Journal Entry. """
    return crud.get_journals(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

# Get All Journal Entry {account_names}
@router.get("/account_names/", response_model=List)
async def get_account_names(db: Session = Depends(get_db)) -> List:
    """ List Journal Enrty {account_names} """
    journal = crud.get_journals(db=db)

    # Debit List
    debit_list = [journal.debit_account_name for journal in journal]

    # Credit List
    credit_list = [journal.credit_account_name for journal in journal]

    # All
    account_names_list = debit_list + credit_list

    # Remove Duplicates in the List
    filtered_list = list(set(account_names_list))

    return filtered_list

# Get All Journal Entry {account_names}
@router.get("/supplier_names/", response_model=List)
async def get_supplier_names(db: Session = Depends(get_db)) -> List:
    """ List Journal Enrty {supplier_names} """
    journal = crud.get_journals(db=db)


    name_list = [journal.supplier_name for journal in journal]
    cleaned_names = list(set(name for name in name_list if name))
    
    return cleaned_names

# Create Journal Entry
@router.post("/")
async def create_journal(journal: schemas.JournalCreate, db: Session = Depends(get_db)):
    """ Add Journal Entry. """
    return crud.create_journal(db=db, journal=journal)

# Update Journal Entry
@router.put("/{id}", response_model=schemas.Journal)
async def update_journal(journal: schemas.JournalCreate, id: int, db: Session = Depends(get_db)):
    """ Update Journal """
    return crud.update_journal(db=db, id=id, journal=journal)

# Remove Journal Entry
@router.delete("/{id}", response_model=schemas.Journal)
async def delete_journal(id: int, db: Session = Depends(get_db)):
    """ Remove Journal """
    return crud.delete_journal(db=db, id=id)