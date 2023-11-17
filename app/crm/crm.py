import hashlib
import os
from typing import Optional

import filetype
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.crm import crud, schemas
from app.crm.constants import K_DIR_CRM_IMGS, K_DIR_CRM_UPLOADS
# from app.crm.database import SessionLocal
from app.crm.routers import addresses_router, companies_router, persons_router
from fastapi import (
    Depends,
    FastAPI,
    File,
    Header,
    HTTPException,
    Query,
    UploadFile,
    status,
)

from app.database import DatabaseSessionMaker

app = FastAPI(
    title="Shydan's Address List", description="API for all things related to contacts."
)

get_db = DatabaseSessionMaker("shydans_db")


# Sub-applications which are mounted cannot be found on the docs.
app.mount("/imgs/", StaticFiles(directory=K_DIR_CRM_IMGS), name="imgs")

app.mount("/files/", StaticFiles(directory=K_DIR_CRM_UPLOADS), name="files")

app.include_router(persons_router.router)
app.include_router(companies_router.router)
app.include_router(addresses_router.router)


@app.get("/contacts/")
async def get_contacts(
    cid: Optional[list[int]] = Query(None),
    offset: int = 0,
    limit: int = 500,
    sort_column: str = "id",
    sort_direction: str = "desc",
    x_country_id: int = Header(None),
    db: Session = Depends(get_db),
):
    return crud.get_contacts(
        db=db,
        country_id=x_country_id,
        contact_ids=cid,
        offset=offset,
        limit=limit,
        sort_column=sort_column,
        sort_direction=sort_direction,
    )


@app.get("/contacts/{contact_type}/{filters}/")
async def search_contact(
    contact_type: str,
    filters: str,
    query: str = None,
    x_country_id: int = Header(None),
    offset: int = 0,
    limit: int = 500,
    sort_column: str = "id",
    sort_direction: str = "desc",
    db: Session = Depends(get_db),
):
    """
    An extensive search method for contacts, with support for pagination through offset and limit.
    - ***contact_type***: Valid contact_type values are **all**, **company**, **person**, and **supplier**.
    - ***filters***: Is a string with values separated by a '+', valid filter values are **name**, **email**,
           **contact**, and **address**.
    - ***query***: The text/string to search in the database.
    - ***x-country-id***: Refers to the country in which the contact should belong to.
    - ***offset***: Refers to the number of items that will be skipped.
    - ***limit***: Refers to the max number of items that will be returned.
    - ***sort_column***: Refers to the column to be sorted by, valid sort_column values are **id**, **name**,
           **email**, **address**, and **main_telephone**.
    - ***sort_direction***: Refers to the sort direction to be applied to the sort_column, valid sort_direction values
           are **asc**, and **desc**
    """
    return crud.search_contact(
        db,
        contact_type,
        filters,
        query,
        x_country_id,
        offset,
        limit,
        sort_column,
        sort_direction,
    )


@app.get("/contacts/relationship/{empr_id}/employees/")
async def get_employees(empr_id: int, db: Session = Depends(get_db)):
    return crud.get_relationship_employees(db, empr_id)


@app.get("/contacts/relationship/{empe_id}/employers/")
async def get_employers(empe_id: int, db: Session = Depends(get_db)):
    return crud.get_relationship_employers(db, empe_id)


@app.post("/contacts/relationship/{empr_id}/{empe_id}/")
async def add_employee(empr_id: int, empe_id: int, db: Session = Depends(get_db)):
    return crud.create_relationship(db, empr_id, empe_id)


@app.delete("/contacts/relationship/{empr_id}/{empe_id}/")
async def delete_relationship(
    empr_id: int, empe_id: int, db: Session = Depends(get_db)
):
    return crud.delete_relationship(db, empr_id, empe_id)


@app.get("/uploads/{id}/")
async def get_files(id: int, db: Session = Depends(get_db)):
    return crud.read_files(db=db, contact_id=id)


@app.post("/uploads/{id}/")
async def upload_file(
    id: int, attached_file: UploadFile = File(...), db: Session = Depends(get_db)
):
    file_bytes = attached_file.file.read()
    file_type = filetype.guess(file_bytes)

    if file_type is None:
        raise HTTPException(status_code=415)

    file_name = (
        hashlib.sha224((attached_file.filename + str(id)
                        ).encode("UTF-8")).hexdigest()
        + "."
        + file_type.extension
    )

    new_file = open(K_DIR_CRM_UPLOADS + file_name, "+wb")
    new_file.write(file_bytes)
    new_file.close()

    db_item = schemas.AttachedFileCreate(
        file_name=attached_file.filename, dl_file=file_name, contact_id=id
    )
    return crud.insert_file(db=db, attached_file=db_item)


@app.put("/uploads/{id}/")
async def update_subject(
    id: int, file: schemas.AttachedFile, db: Session = Depends(get_db)
):
    return crud.update_file(db, id, file)


@app.delete("/uploads/")
async def delete_file(i: list[int] = Query(None), db: Session = Depends(get_db)):
    db_items = []
    for file_id in i:
        db_item = crud.delete_file(db=db, id=file_id)
        db_items.append(db_item)
        file_to_delete = db_item.dl_file
        os.remove(K_DIR_CRM_UPLOADS + file_to_delete)


@app.get("/contacts/{contact_type}/{contact_id}/note/")
async def get_note(contact_type: str, contact_id: int, db: Session = Depends(get_db)):
    return crud.get_note(db, contact_id, contact_type)


@app.put("/contacts/{contact_type}/{contact_id}/note/")
async def update_note(
    contact_type: str,
    contact_id: int,
    note: schemas.ContactNotes,
    db: Session = Depends(get_db),
):
    return crud.update_note(db, note, contact_id, contact_type)


@app.post("/import-contacts", status_code=status.HTTP_201_CREATED)
async def import_contacts(
    csv_contacts: list[schemas.CSVContacts], db: Session = Depends(get_db)
):
    return crud.import_contacts(db=db, csv_contacts=csv_contacts)


@app.get("/shop-account", response_model=list[schemas.ShopAccount])
async def get_contact_shop_account(
    contact_id: int = 0, user_id: int = 0, db: Session = Depends(get_db)
):
    return crud.get_contact_shop_accounts(db, user_id, contact_id)


@app.post("/shop-account", response_model=schemas.ShopAccount)
async def create_shop_account(
    shop_account: schemas.ShopAccountCreate, db: Session = Depends(get_db)
):
    return crud.create_shop_account(db, shop_account)


@app.put("/shop-account/{shop_account_id}/", response_model=schemas.ShopAccount)
async def update_shop_account(
    shop_account_id: int,
    shop_account: schemas.ShopAccount,
    db: Session = Depends(get_db),
):
    return crud.update_shop_account(db, shop_account_id, shop_account)


@app.delete("/shop-account/{shop_account_id}/")
async def delete_shop_account(shop_account_id: int, db: Session = Depends(get_db)):
    return crud.delete_shop_account(db, shop_account_id)


@app.put("/contacts/{contact_id}/address")
async def update_contact_address(
    contact_id: int, new_address: schemas.ContactAddress, db: Session = Depends(get_db)
):
    return crud.update_contact_address(db, contact_id, new_address)
