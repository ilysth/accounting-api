import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Chart(Base):
    __tablename__ = "accounting_chart"

    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String(255))
    account_type = Column(String(255))
    report_type = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)


class Journal(Base):
    __tablename__ = "accounting_journal"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, nullable=True)
    document_no = Column(String(255), nullable=True)
    debit_acct_id = Column(Integer, nullable=True)
    credit_acct_id = Column(Integer, nullable=True)
    debit = Column(Float)
    credit = Column(Float)
    date = Column(DateTime, nullable=True)
    notes = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    is_supplier = Column(Integer, default=0)


class Supplier(Base):
    __tablename__ = "accounting_supplier"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    business_type = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    contact_number = Column(String(255), nullable=True)
    tel_number = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    tin = Column(String(255), nullable=True)
    sec = Column(String(255), nullable=True)
    dti = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)


class Debit(Base):
    __tablename__ = "accounting_debit_balance"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    debit = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)


class Credit(Base):
    __tablename__ = "accounting_credit_balance"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    credit = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
