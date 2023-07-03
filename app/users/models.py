import datetime
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey

from app.users.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, default="NONE")
    password = Column(String, default="NONE")
    first_name = Column(String, default="NONE")
    last_name = Column(String, default="NONE")
    role = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
    creation_update = Column(DateTime, nullable=True)
