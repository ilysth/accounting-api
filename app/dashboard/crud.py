from sqlalchemy.orm import Session
from app.dashboard import schemas, models
from fastapi import HTTPException
from passlib.hash import bcrypt

def get_user_from_db(db: Session, username: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()

    return db_user

def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)

def login(username: str, password: str, db: Session):
    # Retrieve the user's record from the database based on their username or email
    user = get_user_from_db(username=username, db=db)

    # Return user
    if user is None:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    
    # Verify the password
    if verify_password(password, user.password):
        return user
    else:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    

def create_user(db: Session, user: schemas.UserCreate):
    db_user_check = get_user_from_db(username=user.username , db=db)
    
    if db_user_check:
        raise HTTPException(status_code=404, detail="Username already taken")
    
    hashed_password = bcrypt.hash(user.password)  # Hash the password
    db_user = models.User(
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