from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from app.users.database import SessionLocal
from app.users.routers import users_router

app = FastAPI(title="APP Features", description="App Integration Resources")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(users_router.router)