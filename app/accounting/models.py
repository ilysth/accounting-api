import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

from app.accounting.database import Base


class Chart(Base):
    __tablename__ = "chart_of_accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String, default="NONE")
    account_type = Column(String, default="NONE")
    report_type = Column(String, default="NONE")
    created_at = Column(DateTime, default=datetime.datetime.now)


class Journal(Base):
    __tablename__ = "journal_entry"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, nullable=True)
    document_no = Column(String, default="NONE")
    debit_acct_id = Column(Integer, nullable=True)
    credit_acct_id = Column(Integer, nullable=True)
    debit = Column(Float, default="NONE")
    credit = Column(Float, default="NONE")
    date = Column(DateTime, nullable=True)
    notes = Column(String, default="NONE")
    created_at = Column(DateTime, default=datetime.datetime.now)
    is_supplier = Column(Integer, default=0)


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, default="NONE")
    last_name = Column(String, default="NONE")
    business_type = Column(String, default="NONE")
    email = Column(String, default="NONE")
    contact_number = Column(String, default="NONE")
    tel_number = Column(String, default="NONE")
    address = Column(String, default="NONE")
    tin = Column(String, default="NONE")
    sec = Column(String, default="NONE")
    dti = Column(String, default="NONE")
    created_at = Column(DateTime, default=datetime.datetime.now)


class Debit(Base):
    __tablename__ = "debit_balance"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="NONE")
    debit = Column(Float, default=0, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)


class Credit(Base):
    __tablename__ = "credit_balance"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="NONE")
    credit = Column(Float, default=0, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
