from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/companies", tags=["Companies Resources"])

get_db = DatabaseSessionMaker("shydans_db")


@router.get("/")
async def read_companies(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Company. """
    return crud.get_companies(db=db, sort_direction=sort_direction, skip=skip, limit=limit)


@router.post("/")
async def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    """ Add Company. """
    return crud.create_company(db=db, company=company)


@router.put("/{id}/", response_model=schemas.Company)
async def update_company(company: schemas.CompanyCreate, id: int, db: Session = Depends(get_db)):
    """ Update Company """
    return crud.update_company(db=db, id=id, company=company)


@router.delete("/{id}/", response_model=schemas.Company)
async def delete_company(id: int, db: Session = Depends(get_db)):
    """ Remove Company """
    return crud.delete_company(db=db, id=id)
