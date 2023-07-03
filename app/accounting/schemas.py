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
    supplier_name: str
    document_no: str
    debit_account_name: str
    credit_account_name: str
    debit: str
    credit: str
    date: Optional[datetime] = None
    notes: str
    is_supplier: int


class JournalCreate(JournalBase):
    pass


class Journal(JournalBase):
    id: int

    class Config:
        orm_mode = True


class SupplierBase(BaseModel):
    business_type: str
    first_name: str
    last_name: str
    email: str
    contact_number: str
    tel_number: str
    address: str
    tin: str
    sec_registration: str
    dti_registration: str


class SupplierCreate(SupplierBase):
    pass


class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True