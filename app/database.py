import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import mysql.connector

dotenv_path = Path("env/.env")
load_dotenv(dotenv_path=dotenv_path)

MYSQL_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")

database_names = [
    "shydans_db", "tessa_db"
]

# Create a connection to the MySQL server then create databases that don't exist.
mysql_connection = mysql.connector.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    password=MYSQL_PASSWORD
)

for db_name in database_names:
    cursor = mysql_connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.close()

mysql_connection.close()


databases = {}
for db_name in database_names:
    db_connect = f"mysql+mysqlconnector://root:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{db_name}"
    engine = create_engine(db_connect, pool_pre_ping=True, pool_size=20, max_overflow=0)
    databases[db_name] = sessionmaker(
        autocommit=False, autoflush=True, bind=engine)


def get_db(database_name: str):
    db = databases[database_name]()
    try:
        yield db
    finally:
        db.close()


class DatabaseSessionMaker:
    """
    Creates a new session to be used for database operations.
    Wraps the get_db(), so that it can still be used as a Dependency after adding a parameter.

    See Referring to a new database section in README.md
    """

    def __init__(self, database_name: str):
        self.database_name = database_name

    def __call__(self):
        if self.database_name not in database_names:
            raise KeyError("Database name invalid")

        return self._get_db(self.database_name)

    def _get_db(self, database_name):
        return next(get_db(database_name))