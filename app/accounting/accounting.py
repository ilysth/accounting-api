from fastapi import FastAPI
from app.accounting.routers import account_frame_router, chart_of_accounts_router, transaction_router, companies_router, department_router, journal_entry_router, supplier_router, balance_router
from app.database import DatabaseSessionMaker

app = FastAPI(title="APP Features", description="App Integration Resources")

get_db = DatabaseSessionMaker("shydans_accounting")
        
app.include_router(account_frame_router.router)
app.include_router(chart_of_accounts_router.router)
app.include_router(companies_router.router)
app.include_router(department_router.router)
app.include_router(journal_entry_router.router)
app.include_router(transaction_router.router)
app.include_router(supplier_router.router)
# app.include_router(balance_router.router)