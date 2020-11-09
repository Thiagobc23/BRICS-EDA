import pandas as pd
import sqlite3


def to_json(table):
    # Read sqlite query, get data frame, and close the connection
    conn = sqlite3.connect(r"c:/py/BRICS-EDA/data/brics.db")
    df = pd.read_sql_query("SELECT * from {}".format(table), conn)
    conn.close()

    #print(df.head())
    return df.to_json()
    