from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from config import CONNECTION_STRING

engine = create_engine(f'sqlite:///{CONNECTION_STRING}', echo=True)
base = declarative_base()

class User(base):
    __tablename__ = "users"
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)