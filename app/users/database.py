from dotenv import dotenv_values
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = dotenv_values('env/.env')
mysql_password = config['MYSQL_ROOT_PASSWORD']
mysql_host = config['MYSQL_HOST']
mysql_port = config['MYSQL_PORT']
db_name = config['DB_NAME_USER']

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:{mysql_password}@{mysql_host}:{mysql_port}/"
SQLALCHEMY_DATABASE_URL_W_NAME = f"mysql+mysqlconnector://root:{mysql_password}@{mysql_host}:{mysql_port}/{db_name}"

mysql_engine = create_engine(SQLALCHEMY_DATABASE_URL)
with mysql_engine.connect() as connection:
    create_db_query = text("CREATE DATABASE IF NOT EXISTS {0}".format(db_name))
    connection.execute(create_db_query)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL_W_NAME,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()
