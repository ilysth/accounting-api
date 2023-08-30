import os
from fastapi import FastAPI
from . import tessa_methods, schemas
import mysql.connector

app = FastAPI()

MYSQL_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
DB_NAME = "tessa_db"

# Get a sample message
@app.post("/message", tags=["Bency_Test"])
async def say_hello(my_obj: schemas.tessa_obj):
    """Returns a sample"""
    return tessa_methods.say_hello(str=my_obj.name, tessa_obj=my_obj)


@app.post('/create_table', tags=["TESSA_Database_Modeling"])
async def create_table(table_name: str, columns: list, data_types: list, table_comment: str = ""):
    """Creates a new table with the given name and columns."""
    
    mysql_connection = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        password=MYSQL_PASSWORD,
        database=DB_NAME # "tessa_db"
    )
    schema = "(" + ",".join([f"{column} {data_type}" for column, data_type in zip(columns, data_types)]) + ")"

    cursor = mysql_connection.cursor()
    cursor.execute(f"CREATE TABLE {table_name} {schema}")
    cursor.close()

    mysql_connection.close()

    return {'message': 'Table created successfully'}