import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from . import tessa_methods, schemas
import mysql.connector

app = FastAPI()

MYSQL_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
DB_NAME = "tessa_db"

# Define the directory where uploaded files will be stored
K_DIR_TESSA_UPLOADS = "app/tessa/uploads/"
# Create the directory if it doesn't exist
if not os.path.exists(K_DIR_TESSA_UPLOADS):
    os.makedirs(K_DIR_TESSA_UPLOADS)
app.mount("/files/", StaticFiles(directory=K_DIR_TESSA_UPLOADS), name="files")

# Get a sample message
@app.post("/message", tags=["Bency_Test"])
async def say_hello(my_obj: schemas.tessa_obj):
    """Returns a sample"""
    return tessa_methods.say_hello(str=my_obj.name, tessa_obj=my_obj)

# Create a table defined in TESSA
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

    # Todo: error checking
    cursor = mysql_connection.cursor()
    cursor.execute(f"CREATE TABLE {table_name} {schema}")
    cursor.close()

    mysql_connection.close()

    return {'message': 'Table created successfully'}

# Upload a file from TESSA
@app.post("/uploadfile/", tags=["TESSA_File_Management"])
async def upload_file(file: UploadFile):

    file_bytes = file.file.read()
    # Check if the uploaded file exceeds the 5MB limit
    if len(file_bytes) > 5 * 1024 * 1024:  # 5MB in bytes
        return JSONResponse(content={"error": "File size exceeds the 5MB limit"}, status_code=400)

    # Save the uploaded file to the "Uploads" directory
    file_path = os.path.join(K_DIR_TESSA_UPLOADS, file.filename)
    with open(file_path, "wb") as f:
        f.write(file_bytes)
        f.close

    return {"filename": file.filename}