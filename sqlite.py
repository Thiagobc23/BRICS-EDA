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
            return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
