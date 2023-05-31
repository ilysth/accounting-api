from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = dotenv_values('env/.env')
mysql_password = config['MYSQL_ROOT_PASSWORD']
mysql_host = config['MYSQL_HOST']
mysql_port = config['MYSQL_PORT']

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:{mysql_password}@{mysql_host}:{mysql_port}/shydans_accounting"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()
