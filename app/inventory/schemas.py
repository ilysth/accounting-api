from datetime   import datetime
from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    description: str
    uom1: str
    uom2: str
    uom3: str
    conversion: str
    default_coa: str
    nominated_supplier: str
    last_vendor: str
    ave_cost = float
    highest_price = float
    lowest_price = float
    is_vatable = boolean
    is_deleted = boolean
    added_by: str


class ItemCreate(FrameBase):
    pass

class Item(FrameBase):
    id: int
    
    class Config:
        orm_mode = True
