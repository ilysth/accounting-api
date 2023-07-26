from datetime   import datetime
from pydantic import BaseModel
from typing import Optional


class ChartBase(BaseModel):
    account_name: str
    account_type: str
    report_type: str


class ChartCreate(ChartBase):
    pass


class Chart(ChartBase):
    id: int

    class Config:
        orm_mode = True


class JournalBase(BaseModel):
    supplier_id: Optional[int] = None
    document_no: str
    debit_acct_id: Optional[int] = None
    credit_acct_id: Optional[int] = None
    debit: float
    credit: float
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
    sec: str
    dti: str


class SupplierCreate(SupplierBase):
    pass


class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True


class DebitBase(BaseModel):
    name: str
    debit: float

class DebitCreate(DebitBase):
    pass


class Debit(DebitBase):
    id: int

    class Config:
        orm_mode = True


class CreditBase(BaseModel):
    name: str
    credit: float

class CreditCreate(CreditBase):
    pass


class Credit(CreditBase):
    id: int

    class Config:
        orm_mode = True