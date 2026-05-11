from sqlalchemy import create_engine, text
import pandas as pd

DB_FILE = 'Chinook_Sqlite.sqlite'

def get_engine():
    return create_engine(f'sqlite:///{DB_FILE}')


