import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "dashboard_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    role = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
    creation_update = Column(DateTime, nullable=True)
