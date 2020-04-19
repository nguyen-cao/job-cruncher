import os
from app import settings

from sqlalchemy import create_engine

# DATABASE_URL = 'sqlite:///data.sqlite3'
DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI

engine = create_engine(DATABASE_URL, echo=True)
