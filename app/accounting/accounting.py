from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from app.accounting.database import SessionLocal
from app.accounting.routers import chart_of_accounts_router, journal_entry_router
from app.accounting import crud, schemas

app = FastAPI(title="APP Features", description="App Integration Resources")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app.include_router(chart_of_accounts_router.router)
app.include_router(journal_entry_router.router)