from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from typing import List, Optional
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/journals", tags=["Journal Entry Resources"])

get_db = DatabaseSessionMaker("shydans_db")


@router.get("/filter-all-by-frame/")
async def read_journals(db: Session = Depends(get_db), from_date: Optional[str] = None, to_date: Optional[str] = None, frame_id: int = 0, chart_id: int = 0, company_ids: List[int] = Query(None, title="List of Company IDs"), department_ids: List[int] = Query(None, title="List of Department IDs"), supplier_id: int = 0):
    """ List Journal Entry all by frame. """
    return crud.get_journals_by_frame(db=db, from_date=from_date, to_date=to_date, frame_id=frame_id, chart_id=chart_id, company_ids=company_ids, department_ids=department_ids, supplier_id=supplier_id)


@router.get("/transactions/")
def read_journal_and_transactions(db: Session = Depends(get_db)):
    return crud.get_all_journals_and_transactions(db)


@router.post("/transactions/", status_code=status.HTTP_201_CREATED)
async def create_journal_and_transactions(journal: schemas.JournalCreate, db: Session = Depends(get_db)):
    """ Add Journal Entry """
    return crud.create_journal_and_transactions(db=db, journal=journal)


@router.put("/transactions/{id}/")
def update_journal_and_transactions(
    id: int,
    journal: schemas.JournalCreate,
    db: Session = Depends(get_db)
):
    return crud.update_journal_and_transactions(db=db, journal=journal, id=id)


@router.get("/{id}/")
async def read_journals(id: int, db: Session = Depends(get_db)):
    """ Journal Entry by ID. """
    return crud.get_journals_by_id(db=db, id=id)


@router.put("/{id}/", response_model=schemas.Journal)
async def update_journal(journal: schemas.JournalCreate, id: int, db: Session = Depends(get_db)):
    """ Update Journal Entry """
    return crud.update_journal(db=db, id=id, journal=journal)


@router.delete("/{id}/", response_model=schemas.Journal)
async def delete_journal(id: int, db: Session = Depends(get_db)):
    """ Remove Journal Entry """
    return crud.delete_journal(db=db, id=id)

# @router.get("/transactions/debit/")
# async def read_transactions_debit(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
#     """ List of Debit Transacations """
#     return crud.get_transactions_debit(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

# @router.post("/transactions/debit/")
# async def create_transaction_debit(debit: schemas.DebitEntryCreate, db: Session = Depends(get_db)):
#     """ Add Debit Transacation """
#     return crud.create_transaction_debit(db=db, debit=debit)

# @router.put("/transactions/debit/{id}", response_model=schemas.DebitEntry)
# async def update_transaction_debit(debit: schemas.DebitEntryCreate, id: int, db: Session = Depends(get_db)):
#     """ Update Debit Transacation """
#     return crud.update_transaction_debit(db=db, id=id, debit=debit)

# @router.delete("/transactions/debit/{id}", response_model=schemas.DebitEntry)
# async def delete_transaction_debit(id: int, db: Session = Depends(get_db)):
#     """ Remove Debit Transacation """
#     return crud.delete_transaction_debit(db=db, id=id)

# @router.get("/transactions/credit/")
# async def read_transactions_credit(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
#     """ List of Credit Transacations """
#     return crud.get_transactions_credit(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

# @router.post("/transactions/credit/")
# async def create_transaction_credit(credit: schemas.CreditEntryCreate, db: Session = Depends(get_db)):
#     """ Add Credit Transacation """
#     return crud.create_transaction_credit(db=db, credit=credit)

# @router.put("/transactions/credit/{id}", response_model=schemas.CreditEntry)
# async def update_transaction_credit(credit: schemas.CreditEntryCreate, id: int, db: Session = Depends(get_db)):
#     """ Update Credit Transacation """
#     return crud.update_transaction_credit(db=db, id=id, credit=credit)

# @router.delete("/transactions/credit/{id}", response_model=schemas.CreditEntry)
# async def delete_transaction_credit(id: int, db: Session = Depends(get_db)):
#     """ Remove Credit Transacation """
#     return crud.delete_transaction_credit(db=db, id=id)


@router.post("/import-journals/", status_code=status.HTTP_201_CREATED)
async def import_journals(
    csv_journals: list[schemas.JournalCreate], db: Session = Depends(get_db)
):
    return crud.import_journals(db=db, csv_journals=csv_journals)


@router.post("/generate-reference-number/", status_code=status.HTTP_201_CREATED)
async def create_reference_number(
    journal: schemas.JournalCreate, db: Session = Depends(get_db)
):
    """Create Reference Number only."""
    return crud.create_reference_number(db=db, journal=journal)
