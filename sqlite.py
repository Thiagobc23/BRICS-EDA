import sqlite3
from sqlite3 import Error

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
            conn.close()