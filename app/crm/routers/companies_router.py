import time

from fastapi import APIRouter, HTTPException, Header, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.crm import crud, schemas
from app.crm.constants import K_DIR_CRM_IMGS
from app.database import DatabaseSessionMaker
# from app.crm.database import SessionLocal

router = APIRouter(prefix="/companies", tags=["Companies Resources"])

get_db = DatabaseSessionMaker("shydans_db")


@router.get("/trade-types/")
async def get_trade_types(db: Session = Depends(get_db)):
    return crud.get_trade_types(db)


@router.post("/trade-types/")
async def create_new_trade_type(
    trade_type: schemas.TradeTypeBase, db: Session = Depends(get_db)
):
    return crud.create_trade_type(db, trade_type)


@router.put("/trade-types/{trade_type_id}/")
async def update_trade_type(
    trade_type: schemas.TradeType, trade_type_id: int, db: Session = Depends(get_db)
):
    return crud.update_trade_type(db, trade_type_id, trade_type)


@router.delete("/trade-types/{trade_type_id}/")
async def delete_trade_type(trade_type_id: int, db: Session = Depends(get_db)):
    return crud.delete_trade_type(db, trade_type_id)


@router.get("/{contact_id}/trade-types/")
async def get_company_trade_types(contact_id: int, db: Session = Depends(get_db)):
    return crud.get_company_trade_types(db, contact_id)


@router.get("/{contact_id}/sub-contacts/")
async def get_company_sub_contacts(contact_id: int, db: Session = Depends(get_db)):
    return crud.get_company_sub_contacts(db=db, contact_id=contact_id)


@router.put("/{contact_id}/trade-types/")
async def update_company_trade_types(
    contact_id: int, trade_types: list[schemas.TradeType], db: Session = Depends(get_db)
):
    return crud.update_company_trade_types(db, contact_id, trade_types)


@router.get("/{contact_id}/", response_model=schemas.Company)
async def get_company(contact_id: int, db: Session = Depends(get_db)):
    company = crud.get_contact(db, contact_id)

    if company is None:
        raise HTTPException(status_code=404)

    if company.contact_type != "company":
        raise HTTPException(status_code=400, detail="Contact is not a company")

    return company


@router.get("/")
async def get_companies(
    x_country_id: int = Header(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return crud.get_companies(db, x_country_id, skip, limit)


@router.post("/")
async def create_company(company: schemas.Company, db: Session = Depends(get_db)):
    return crud.create_company(db, company)


@router.put("/{contact_id}/")
async def update_company(
    company: schemas.Company, contact_id: int, db: Session = Depends(get_db)
):
    return crud.update_company(db, contact_id, company)


@router.put("/{contact_id}/picture/")
async def upload_company_picture(
    contact_id: int, img: UploadFile = File(...), db: Session = Depends(get_db)
):
    image_content_type = img.content_type
    if not (image_content_type == "image/jpeg" or image_content_type == "image/png"):
        raise HTTPException(status_code=415)

    image_name = str(time.time()) + img.filename

    image_file_bytes = img.file.read()
    new_file = open(K_DIR_CRM_IMGS + image_name, "+wb")
    new_file.write(image_file_bytes)
    new_file.close()
    return crud.update_company_photo(db, contact_id, image_name)


@router.delete("/{contact_id}/")
async def delete_company(contact_id: int, db: Session = Depends(get_db)):
    company = await crud.delete_contact(db, contact_id)

    if company is None:
        raise HTTPException(status_code=404)

    return company
