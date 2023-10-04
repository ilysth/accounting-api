import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Frame(Base):
    __tablename__ = "accounting_frame"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    report_type = Column(String(255))
    code = Column(String(255))
    is_deleted = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)

    charts = relationship("Chart", back_populates="frame",
                          cascade="all, delete-orphan")


class Chart(Base):
    __tablename__ = "accounting_charts"

    id = Column(Integer, primary_key=True, index=True)
    frame_id = Column(Integer, ForeignKey("accounting_frame.id"))
    name = Column(String(255))
    account_type = Column(String(255))
    code = Column(String(255))
    is_deleted = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)

    frame = relationship("Frame", back_populates="charts")
    transaction = relationship(
        "Transaction", back_populates="chart", cascade="all, delete-orphan")


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

    journal = relationship(
        "Journal", back_populates="supplier", cascade="all, delete-orphan")


class Company(Base):
    __tablename__ = "accounting_company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    code = Column(String(255))
    is_deleted = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)

    departments = relationship(
        "Department", back_populates="company", cascade="all, delete-orphan")
    journal = relationship(
        "Journal", back_populates="company", cascade="all, delete-orphan")


class Department(Base):
    __tablename__ = "accounting_department"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("accounting_company.id"))
    name = Column(String(255))
    code = Column(String(255))
    is_deleted = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)

    company = relationship("Company", back_populates="departments")
    journal = relationship("Journal", backref="department",
                           cascade="all, delete-orphan")


class Journal(Base):
    __tablename__ = "accounting_journal"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey(
        "accounting_company.id"), nullable=True)
    department_id = Column(Integer, ForeignKey(
        "accounting_department.id"), nullable=True)
    supplier_id = Column(Integer, ForeignKey(
        "accounting_supplier.id"), nullable=True)
    reference_no = Column(String(255), nullable=True)
    date = Column(DateTime, nullable=True)
    notes = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    is_supplier = Column(Integer, default=0)

    transaction = relationship(
        "Transaction", back_populates="journal", cascade="all, delete-orphan")
    company = relationship("Company", back_populates="journal")
    supplier = relationship("Supplier", back_populates="journal")


class Transaction(Base):
    __tablename__ = "accounting_transaction"

    id = Column(Integer, primary_key=True, index=True)
    journal_id = Column(Integer, ForeignKey(
        "accounting_journal.id"), nullable=True)
    chart_id = Column(Integer, ForeignKey(
        "accounting_charts.id"), nullable=True)
    amount = Column(Float, default=0.00)
    particulars = Column(String(255), nullable=True)
    is_type = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)

    journal = relationship("Journal", back_populates="transaction")
    chart = relationship("Chart", back_populates="transaction")


class DebitBalance(Base):
    __tablename__ = "accounting_debit_balance"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    debit = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)


class CreditBalance(Base):
    __tablename__ = "accounting_credit_balance"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    credit = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
