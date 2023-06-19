from datetime   import datetime
from pydantic import BaseModel
from typing import Optional


class ChartBase(BaseModel):
    account_name: str
    account_type: str
    report_type: str
    is_deleted: int


class ChartCreate(ChartBase):
    pass


class Chart(ChartBase):
    id: int

    class Config:
        orm_mode = True


class JournalBase(BaseModel):
    debit_account_type: str
    credit_account_type: str
    debit: str
    credit: str
    date: Optional[datetime] = None
    notes: str
    is_deleted: int


class JournalCreate(JournalBase):
    pass


class Journal(JournalBase):
    id: int

    class Config:
        orm_mode = True