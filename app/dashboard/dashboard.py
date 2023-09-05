from fastapi import FastAPI, Depends, File, HTTPException, UploadFile
from app.database import DatabaseSessionMaker
from app.dashboard.routers import users_router

from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app.dashboard import schemas, crud, models
from typing import List
import os
import time
app = FastAPI(title="APP Features", description="App Integration Resources")

get_db = DatabaseSessionMaker("shydans_db")

# app.include_router(users_router.router)

app.mount("/imgs/", StaticFiles(directory="app/dashboard/imgs"), name="imgs")

app.mount("/apps/dl/", StaticFiles(directory="app/dashboard/apps"), name="apps")


@app.post("/login/", response_model=schemas.User)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.login(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@app.get("/users/{search}", response_model=List[schemas.User])
def search_user(search: str, db: Session = Depends(get_db)):
    return crud.search_users(db=db, search=search)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.put("/users/{id}/image", response_model=schemas.User)
def upload_user_photo(
    id: int, image: UploadFile = File(...), db: Session = Depends(get_db)
):
    image_content_type = image.content_type
    if not (image_content_type == "image/jpeg" or image_content_type == "image/png"):
        raise HTTPException(status_code=415)

    image_name = str(time.time()) + image.filename

    image_file_bytes = image.file.read()
    new_file = open("app/dashboard/imgs/" + image_name, "+wb")
    new_file.write(image_file_bytes)
    new_file.close()

    return crud.update_user_photo(db=db, id=id, image=image_name)


@app.put("/users/{id}", response_model=schemas.User)
def update_user(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, id=id, user=user)


@app.delete("/users/{id}", response_model=schemas.User)
def delete_user(id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, id=id)


@app.get("/apps/{app_name}", response_model=List[schemas.Application])
def get_applications(app_name: str, db: Session = Depends(get_db)):
    return crud.get_application_like_name(db=db, app=app_name)


@app.get("/apps/{app_name}/{platform_id}/latest/", response_model=schemas.Application)
def get_applications(app_name: str, platform_id: int, db: Session = Depends(get_db)):
    return crud.get_application(db=db, app=app_name, platform_id=platform_id)


@app.get("/apps/", response_model=List[schemas.Application])
def get_applications(db: Session = Depends(get_db)):
    return crud.get_applications(db=db)


@app.post("/apps/", response_model=schemas.Application)
def create_application(app: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_application(db=db, app=app)


@app.post("/apps/batch-create/", response_model=List[schemas.Application])
def batch_create_applications(
    apps: List[schemas.ApplicationCreate], db: Session = Depends(get_db)
):
    for app in apps:
        yield crud.create_application(db, app)


@app.post("/apps/upload/{app_dir}/", response_model=schemas.ApplicationFile)
def upload_file(app_dir: str, app_file: UploadFile = File(...)):
    app_file_bytes = app_file.file.read()
    new_file = open("app/dashboard/apps/" + app_dir + "/" + app_file.filename, "+wb")
    new_file.write(app_file_bytes)
    new_file.close()
    return {
        "file_name": app_file.filename,
        "file_size": len(app_file_bytes),
        "mime_type": app_file.content_type,
    }


@app.put("/apps/{id}")
def update(id: int, app: schemas.ApplicationUpdate, db: Session = Depends(get_db)):
    return crud.update_application(db=db, id=id, app=app)


@app.delete("/apps/{id}", status_code=204)
def delete_file(id: int, db: Session = Depends(get_db)):
    db_app = db.query(models.Application).get(id)
    if not db_app:
        return

    app_path = db_app.download_url.replace("/dl/", "/")
    file_path = f"app/dashboard{app_path}"

    if os.path.isfile(file_path):
        os.remove(file_path)

    crud.delete_application(db, id)