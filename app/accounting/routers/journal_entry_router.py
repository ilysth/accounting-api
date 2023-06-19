from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.accounting import crud, schemas
from app.accounting.database import SessionLocal

router = APIRouter(prefix="/journals", tags=["Journal Entries Resources"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get All Journal Entries
@router.get("/")
async def read_journals(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Journal Entries. """
    return crud.get_journals(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

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