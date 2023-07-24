import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.users.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, default="NONE")
    password = Column(String, default="NONE")
    first_name = Column(String, default="NONE")
    last_name = Column(String, default="NONE")
    role = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
    creation_update = Column(DateTime, nullable=True)
