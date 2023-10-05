from sqlalchemy.orm import Session
from app.dashboard import schemas, models
from fastapi import HTTPException
from passlib.hash import bcrypt
from sqlalchemy import and_, desc, func, or_

# def get_user_from_db(db: Session, username: str):
#     db_user = db.query(models.User).filter(models.User.username == username).first()

#     return db_user

# def verify_password(plain_password, hashed_password):
#     return bcrypt.verify(plain_password, hashed_password)

# def login(username: str, password: str, db: Session):
#     # Retrieve the user's record from the database based on their username or email
#     user = get_user_from_db(username=username, db=db)

#     # Return user
#     if user is None:
#         raise HTTPException(status_code=404, detail="Incorrect username or password")

#     # Verify the password
#     if verify_password(password, user.password):
#         return user
#     else:
#         raise HTTPException(status_code=404, detail="Incorrect username or password")


# def create_user(db: Session, user: schemas.UserCreate):
#     db_user_check = get_user_from_db(username=user.username , db=db)

#     if db_user_check:
#         raise HTTPException(status_code=404, detail="Username already taken")

#     hashed_password = bcrypt.hash(user.password)  # Hash the password
#     db_user = models.User(
#         username=user.username,
#         password=hashed_password,
#         role=user.role,
#         first_name=user.first_name,
#         last_name=user.last_name,
#         creation_update=user.creation_update
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


def login(db: Session, user: schemas.UserLogin):
    username = user.username
    password = user.password
    return (
        db.query(models.User)
        .filter(models.User.username == username, models.User.password == password)
        .first()
    )


def get_users(db: Session):
    return db.query(models.User).all()


def search_users(db: Session, search: str):
    return (
        db.query(models.User)
        .filter(
            or_(
                models.User.username.like("%" + search + "%"),
                models.User.fname.like("%" + search + "%"),
                models.User.lname.like("%" + search + "%"),
                models.User.email.like("%" + search + "%"),
            )
        )
        .all()
    )


def get_user(db: Session, id: int):
    return db.query(models.User).get(id)


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).get(id)
    db_user.username = user.username
    db_user.password = user.password
    db_user.role = user.role
    db_user.fname = user.fname
    db_user.lname = user.lname
    db_user.email = user.email
    db_user.creation_date = user.creation_date
    db_user.creation_update = user.creation_update
    db_user.image = user.image
    db_user.apps = user.apps
    db_user.user_contact = user.user_contact
    db_user.country = user.country

    db_user.terminal_user = user.terminal_user
    db_user.terminal_production = user.terminal_production
    db_user.terminal_storage = user.terminal_storage
    db_user.terminal_workspace_id = user.terminal_workspace_id
    db_user.is_superuser = user.is_superuser

    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_photo(db: Session, id: int, image: str):
    db_user = db.query(models.User).get(id)
    db_user.image = image
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, id: int):
    db_user = db.query(models.User).get(id)
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_applications(db: Session):
    return db.query(models.Application).all()


def get_application_like_name(db: Session, app: str):
    return (
        db.query(models.Application)
        .filter(models.Application.app_name.like("%" + app + "%"))
        .all()
    )


def get_application(db: Session, app: str, platform_id: int):
    return (
        db.query(models.Application)
        .filter(
            models.Application.app_name.like("%" + app + "%"),
            models.Application.platform_id == platform_id,
        )
        .order_by(models.Application.app_version.desc())
        .first()
    )


def create_application(db: Session, app: schemas.ApplicationCreate):
    db_app = models.Application(**app.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app


def update_application(db: Session, id: int, app: schemas.ApplicationCreate):
    try:
        rows_matched = (
            db.query(models.Application)
            .filter(models.Application.id == id)
            .update(app.dict(skip_defaults=True))
        )
        db.commit()
        return {"rows_matched": rows_matched}
    except:
        return {"rows_matched": -1}


def delete_application(db: Session, app_id: int):
    db_app = db.query(models.Application).get(app_id)

    if not db_app:
        return

    db.delete(db_app)
    db.commit()
    return db_app
