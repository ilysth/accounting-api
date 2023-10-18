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
    ave_cost: float
    highest_price: float
    lowest_price: float
    is_vatable: int
    is_deleted: int


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    
    class Config:
        orm_mode = True
