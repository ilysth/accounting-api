# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.accounting import crud, schemas
# from app.database import DatabaseSessionMaker

# router = APIRouter(prefix="/balance", tags=["Balance Resources"])

# get_db = DatabaseSessionMaker("shydans_db")


# @router.get("/debit/")
# async def read_latest_debit_balance(db: Session = Depends(get_db)):
#     return crud.get_latest_debit_balance(db=db)


# @router.post("/debit/")
# async def create_debit(debit: schemas.DebitCreate, db: Session = Depends(get_db)):
#     return crud.create_debit(db=db, debit=debit)


# @router.get("/credit/")
# async def read_latest_credit_balance(db: Session = Depends(get_db)):
#     return crud.get_latest_credit_balance(db=db)


# @router.post("/credit/")
# async def create_credit(credit: schemas.CreditCreate, db: Session = Depends(get_db)):
#     return crud.create_credit(db=db, credit=credit)
