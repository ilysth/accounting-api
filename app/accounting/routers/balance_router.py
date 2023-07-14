from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from app.accounting.database import SessionLocal

router = APIRouter(prefix="/balance", tags=["Balance Resources"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get Latest Debit Balance
@router.get("/debit/")
async def read_latest_debit_balance(db: Session = Depends(get_db)):
    return crud.get_latest_debit_balance(db=db)

# Create Debit Balance
@router.post("/debit/")
async def create_debit(debit: schemas.DebitCreate, db: Session = Depends(get_db)):
    return crud.create_debit(db=db, debit=debit)

# Get Latest Credit Balance
@router.get("/credit/")
async def read_latest_credit_balance(db: Session = Depends(get_db)):
    return crud.get_latest_credit_balance(db=db)

# Create Credit
@router.post("/credit/")
async def create_credit(credit: schemas.CreditCreate, db: Session = Depends(get_db)):
    return crud.create_credit(db=db, credit=credit)


