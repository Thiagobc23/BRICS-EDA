import pandas as pd
import sqlite3

# Read sqlite query, get data frame, and close the connection
conn = sqlite3.connect(r"c:/py/BRICS-EDA/db_files/brics.db")
df = pd.read_sql_query("SELECT * from {}".format('names'), conn)

print(df.count())