import imp
from pydantic import BaseModel
from typing import Optional


class ChartBase(BaseModel):
    description: str
    account_type: str
    report_type: str
    is_deleted: int


class ChartCreate(ChartBase):
    pass


class Chart(ChartBase):
    id: int

    class Config:
        orm_mode = True