import os

from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///db.sqlite3'
engine = create_engine(DATABASE_URL, echo=True)  

# SQLALCHEMY_DATABASE_URI = 'postgresql://[username]:[password]@localhost/[dbName]'
SQLALCHEMY_DATABASE_URI = DATABASE_URL

SQLALCHEMY_TRACK_MODIFICATIONS = False