from fastapi import FastAPI
from app.inventory.routers import items_router
from app.database import DatabaseSessionMaker

app = FastAPI(title="Shydans API", description="App Integration Resources")

get_db = DatabaseSessionMaker("shydans_db")
        
app.include_router(items_router.router)