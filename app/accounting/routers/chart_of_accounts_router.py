from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.accounting import crud, schemas
from app.accounting.database import SessionLocal
from typing import List

router = APIRouter(prefix="/charts", tags=["Chart of Accounts Resources"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get All Chart of Account
@router.get("/")
async def read_charts(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Chart of Accounts. """
    return crud.get_charts(db=db, sort_direction=sort_direction, skip=skip, limit=limit)

# Get All Chart of Account {account_names}
@router.get("/account_names", response_model=List)
async def get_account_names(db: Session = Depends(get_db)) -> List:
    """ List Chart of Accounts {account_names} """
    charts = crud.get_charts(db=db)

    # Exclude charts with is_deleted = 1
    filtered_chart = [chart for chart in charts if chart.is_deleted != 1]

    return [chart.account_name for chart in filtered_chart]

# Create Chart of Account
@router.post("/")
async def create_chart(chart: schemas.ChartCreate, db: Session = Depends(get_db)):
    """ Add Chart of Account. """
    return crud.create_chart(db=db, chart=chart)

# Update Chart of Account
@router.put("/{id}", response_model=schemas.Chart)
async def update_chart(chart: schemas.ChartCreate, id: int, db: Session = Depends(get_db)):
    """ Update ... """
    return crud.update_chart(db=db, id=id, chart=chart)

# Remove Chart of Account
@router.delete("/{id}", response_model=schemas.Chart)
async def delete_chart(id: int, db: Session = Depends(get_db)):
    """ Remove ... """
    return crud.delete_chart(db=db, id=id)
