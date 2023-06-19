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
    debit_account_type = Column(String, default="NONE")
    credit_account_type = Column(String, default="NONE")
    debit = Column(String, default="NONE")
    credit = Column(String, default="NONE")
    date = Column(DateTime, nullable=True)
    notes = Column(String, default="NONE")
    created_at = Column(DateTime, default=datetime.datetime.now)
    is_deleted = Column(Integer, default=0)