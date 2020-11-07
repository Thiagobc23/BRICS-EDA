import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(db_file):
    # create db connection
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('SQLite version: ', sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def import_data(conn, path):
    brics = pd.read_csv ('{}data/brics.csv'.format(path))
    brics.to_sql('brics', conn, if_exists='replace', index = False)

    names = pd.read_csv ('{}data/names.csv'.format(path))   
    names.to_sql('names', conn, if_exists='replace', index = False)

    country = pd.read_csv ('{}data/countries.csv'.format(path))
    country.to_sql('countries', conn, if_exists='replace', index = False)

    years = pd.read_csv ('{}data/years.csv'.format(path))
    years.to_sql('years', conn, if_exists='replace', index = False)



