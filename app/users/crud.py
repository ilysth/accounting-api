from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.functions import func
from app.users import crud, schemas, models
from fastapi import HTTPException
from typing import List
from passlib.hash import bcrypt

# def get_user_from_db(db: Session, username: str):
#     db_user = db.query(models.Users).filter(models.Users.username == username).first()

#     return db_user

# def verify_password(plain_password, hashed_password):
#     return bcrypt.verify(plain_password, hashed_password)

# def login(username: str, password: str, db: Session):
#     # Retrieve the user's record from the database based on their username or email
#     user = get_user_from_db(username=username, db=db)

#     return user
#     # if user is None:
#     #     raise HTTPException(status_code=404, detail="User not found.")

#     # # Verify the password
#     # if verify_password(password, user.password):
#     #     return db.query(models.Users).filter(models.Users.username == username, models.Users.password == password).first()

#     # raise HTTPException(status_code=404, detail="Incorrect credentials.")

def login(db: Session, user: schemas.UserLogin):
    username = user.username
    password = user.password
    return db.query(models.Users).filter(models.Users.username == username, models.Users.password == password).first()


# Create User
def create_user(db: Session, user: schemas.UsersCreate):
    hashed_password = bcrypt.hash(user.password)  # Hash the password
    db_user = models.Users(
        username=user.username,
        password=hashed_password,
        role=user.role,
        first_name=user.first_name,
        last_name=user.last_name,
        creation_update=user.creation_update
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user