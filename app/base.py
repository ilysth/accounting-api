# take Base out of the module that imports; Break the cyclic import
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
