from pydantic import BaseModel

class tessa_obj(BaseModel):
    name: str = "TESSA Object"
    message: str = "Hello World"