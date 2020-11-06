from cleaning import clean
import sqlite

path = 'c:/py/BRICS-EDA/'

if __name__ == '__main__':
    df = clean.get_data(path)
    clean.process(df, path)
    sqlite.create_connection(r"c:/py/BRICS-EDA/db_files/pythonsqlite.db")