import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class User(Base):
#     __tablename__ = "dashboard_users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(255))
#     password = Column(String(255))
#     first_name = Column(String(255))
#     last_name = Column(String(255))
#     role = Column(Integer, default=0)
#     created_at = Column(DateTime, default=datetime.datetime.now)
#     creation_update = Column(DateTime, nullable=True)

class Application(Base):
    __tablename__ = "dashboard_apps"
    id = Column(Integer, primary_key=True, index=True)
    app_id = Column(Integer)
    platform_id = Column(Integer)
    app_architecture = Column(Integer)
    app_version = Column(Integer)
    app_name = Column(String(255))
    app_zip = Column(String(255))
    download_url = Column(String(255))
    compressed_size = Column(String(255))
    version_notes = Column(String(255))


class User(Base):
    __tablename__ = "dashboard_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    role = Column(Integer)
    fname = Column(String(255))
    lname = Column(String(255))
    email = Column(String(255))
    contact = Column(String(255))
    image = Column(String(255))
    apps = Column(String(255))
    country = Column(Integer)
    creation_date = Column(DateTime, default=datetime.datetime.now)
    creation_update = Column(DateTime, nullable=True)
    is_superuser = Column(Boolean)