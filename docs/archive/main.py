from cleaning import clean
import sqlite

path = 'c:/py/BRICS-EDA/'

if __name__ == '__main__':
    df = clean.get_data(path)
    clean.process(df, path)
    conn = sqlite.create_connection(r"c:/py/BRICS-EDA/data/brics.db")

    # create tables
    if conn is not None:
        # import data
        sqlite.import_data(conn, path)
        print('data imported to mysql')
    else:
        print("Error! cannot create the database connection.")
    conn.close()