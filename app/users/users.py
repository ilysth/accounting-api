from fastapi import FastAPI
from app.database import DatabaseSessionMaker
from app.users.routers import users_router

app = FastAPI(title="APP Features", description="App Integration Resources")

get_db = DatabaseSessionMaker("shydans_db")

app.include_router(users_router.router)