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

@router.post("/")
async def create_department(department: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    """ Add Department. """
    return crud.create_department(db=db, department=department)

@router.put("/{id}", response_model=schemas.Department)
async def update_company(department: schemas.DepartmentCreate, id: int, db: Session = Depends(get_db)):
    """ Update Department """
    return crud.update_departments(db=db, id=id, department=department)

@router.delete("/{id}", response_model=schemas.Department)
async def delete_company(id: int, db: Session = Depends(get_db)):
    """ Remove Department """
    return crud.delete_company(db=db, id=id)
