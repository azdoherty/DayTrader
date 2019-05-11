import psycopg2
from sqlalchemy import create_engine
from config import db_connection

def get_connection_string():
    user = db_connection['user']
    host = db_connection['host']
    port = db_connection['port']
    db = db_connection['dbname']
    conn_string = f'postgresql+psycopg2://{user}@{host}:{port}/{db}'
    return conn_string

engine = create_engine(get_connection_string())
