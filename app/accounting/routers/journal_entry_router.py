from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from app.accounting.database import SessionLocal
from typing import List, Optional

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

# Get All Journal Entry filtered by dates and account name
@router.get("/filter/")
async def read_journals_by_filter(db: Session = Depends(get_db), from_date: Optional[str] = None, to_date: Optional[str] = None, account_id: int = 0, supplier_id: int = 0, sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """List Journal Entry."""

    try:
        journals = crud.get_journals_by_filter(
                db=db,
                from_date=from_date,
                to_date=to_date,
                supplier_id=supplier_id,
                account_id=account_id,
                sort_direction=sort_direction,
                skip=skip,
                limit=limit
        )

        return journals
    except:
        if from_date and to_date is None:
            raise HTTPException(status_code=404, detail="from_date or to_date should not be empty.")

# Import Journal Entry
@router.post("/import-journal", status_code=status.HTTP_201_CREATED)
async def import_journals(
    csv_journal: list[schemas.JournalCreate], db: Session = Depends(get_db)
):
    return crud.import_journals(db=db, csv_journal=csv_journal)

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