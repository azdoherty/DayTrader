from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from . import engine
base = declarative_base()

class User(base):
    __tablename__ = "users"
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, primary_key=True)
    password = Column(String)


if __name__ == "__main__":
    base.metadata.create_all(engine)
