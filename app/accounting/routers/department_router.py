from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.accounting import crud, schemas
from app.database import DatabaseSessionMaker

router = APIRouter(prefix="/departments", tags=["Departments Resources"])

get_db = DatabaseSessionMaker("shydans_db")


@router.get("/")
async def read_departments(db: Session = Depends(get_db), sort_direction: str = "desc", skip: int = 0, limit: int = 100):
    """ List Department. """
    return crud.get_departments(db=db, sort_direction=sort_direction, skip=skip, limit=limit)


@router.get("/by-company/")
async def read_departments_by_company(company_id: int, db: Session = Depends(get_db)):
    """ List Chart of Accounts by Frame. """
    return crud.get_departments_by_company(db=db, company_id=company_id)


@router.post("/")
async def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    """ Add Department. """
    return crud.create_department(db=db, department=department)


@router.put("/{id}/", response_model=schemas.Department)
async def update_department(department: schemas.DepartmentCreate, id: int, db: Session = Depends(get_db)):
    """ Update Department """
    return crud.update_department(db=db, id=id, department=department)


@router.delete("/{id}/", response_model=schemas.Department)
async def delete_department(id: int, db: Session = Depends(get_db)):
    """ Remove Department """
    return crud.delete_department(db=db, id=id)
