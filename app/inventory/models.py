import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Numeric, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(150)) 
    uom1 = Column(String(150)) 
    uom2 = Column(String(150)) 
    uom3 = Column(String(150)) 
    conversion = Column(String(150)) 
    default_coa = Column(String(150)) 
    nominated_supplier = Column(String(150)) 
    last_vendor = Column(String(150)) 
    ave_cost = Column(Numeric(19, 4), default=0.00)
    highest_price = Column(Numeric(19, 4), default=0.00)
    lowest_price = Column(Numeric(19, 4), default=0.00)
    is_vatable = Column(Boolean, nullable=True, default=0)
    is_deleted = Column(Boolean, nullable=True, default=0)
    added_by = Column(String(150)) 
    added_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=datetime.datetime.now)
