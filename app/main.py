from fastapi import FastAPI
from app.accounting import accounting

app = FastAPI(title="APP Features", description="App Integration Resources")

app.mount("/accounting", accounting.app)
