import sqlite3
import sys
from sqlite3 import Error

sql_create_brics = """ CREATE TABLE IF NOT EXISTS brics (
                    id integer PRIMARY KEY,
                    seriesIndex integer NOT NULL,
                    countryCode text NOT NULL,
                    year integer NOT NULL,
                    value integer NOT NULL
                    ); """

sql_create_countries = """ CREATE TABLE IF NOT EXISTS countries (
                        id integer PRIMARY KEY,
                        CountryName text NOT NULL,
                        CountryCode text NOT NULL
                        ); """

sql_create_names = """ CREATE TABLE IF NOT EXISTS names (
                    id integer PRIMARY KEY,
                    SeriesName text NOT NULL,
                    SeriesCode text NOT NULL,
                    Category text NOT NULL
                    ); """

sql_create_years = """ CREATE TABLE IF NOT EXISTS years (
                    id int PRIMARY KEY,
                    Years int NOT NULL,
                    Filter_Years int NOT NULL
                    ); """

conn = sqlite3.connect("brics.db")

# create tables
if conn is not None:
    print('conn created')
    c = conn.cursor()
    c.execute(sql_create_brics)
    c.execute(sql_create_countries)
    c.execute(sql_create_names)
    c.execute(sql_create_years)            
    print('tables created')
else:
    print("Error! cannot create the database connection.")

conn.close()
