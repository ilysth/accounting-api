import time

from fastapi import APIRouter, HTTPException, Header, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.crm import crud, schemas
from app.crm.constants import K_DIR_CRM_IMGS
from app.database import DatabaseSessionMaker
# from app.crm.database import SessionLocal

router = APIRouter(prefix="/persons", tags=["Persons Resources"])

get_db = DatabaseSessionMaker("shydans_db")


@router.get("/{contact_id}/", response_model=schemas.Person)
async def get_person(contact_id: int, db: Session = Depends(get_db)):
    person = crud.get_contact(db, contact_id)

    if person is None:
        raise HTTPException(status_code=404)

    if person.contact_type != "person":
        raise HTTPException(status_code=400, detail="Contact is not a person")

    return person


@router.get("/")
async def get_persons(
    x_country_id: int = Header(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return crud.get_persons(db, x_country_id, skip, limit)


@router.post("/")
async def create_person(person: schemas.Person, db: Session = Depends(get_db)):
    person.name = person.first_name + " " + person.last_name
    return crud.create_person(db, person)


@router.put("/{contact_id}/")
async def update_person(
    person: schemas.Person, contact_id: int, db: Session = Depends(get_db)
):
    person = crud.update_person(db, contact_id, person)
    if person is None:
        raise HTTPException(status_code=404)
    return person


@router.put("/{contact_id}/picture/")
async def upload_person_picture(
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
    return crud.update_person_photo(db, contact_id, image_name)


@router.delete("/{contact_id}/")
async def delete_person(contact_id: int, db: Session = Depends(get_db)):
    person = await crud.delete_contact(db, contact_id)

    if person is None:
        raise HTTPException(status_code=404)

    return person
