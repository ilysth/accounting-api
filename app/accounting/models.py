import datetime
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey

from app.accounting.database import Base


class Chart(Base):
    __tablename__ = "chart_of_accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String, default="NONE")
    account_type = Column(String, default="NONE")
    report_type = Column(String, default="NONE")
    created_at = Column(DateTime, default=datetime.datetime.now)
    is_deleted = Column(Integer, default=0)


class Journal(Base):
    __tablename__ = "journal_entry"

    id = Column(Integer, primary_key=True, index=True)
    supplier_name = Column(String, default="NONE")
    document_no = Column(String, default="NONE")
    debit_account_name = Column(String, default="NONE")
    credit_account_name = Column(String, default="NONE")
    debit = Column(String, default="NONE")
    credit = Column(String, default="NONE")
    date = Column(DateTime, nullable=True)
    notes = Column(String, default="NONE")
    created_at = Column(DateTime, default=datetime.datetime.now)
    is_supplier = Column(Integer, default=0)


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(Integer, primary_key=True, index=True)
    business_type = Column(String, default="NONE")
    first_name = Column(String, default="NONE")
    last_name = Column(String, default="NONE")
    email = Column(String, default="NONE")
    contact_number = Column(String, default="NONE")
    tel_number = Column(String, default="NONE")
    address = Column(String, default="NONE")
    tin = Column(String, default="NONE")
    sec_registration = Column(String, default="NONE")
    dti_registration = Column(String, default="NONE")