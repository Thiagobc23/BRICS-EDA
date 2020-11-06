from cleaning import clean
import sqlite

path = 'c:/py/BRICS-EDA/'

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
                                id integer PRIMARY KEY,
                                Years text NOT NULL,
                                Filter_Years text NOT NULL
                                ); """


if __name__ == '__main__':
    df = clean.get_data(path)
    clean.process(df, path)
    conn = sqlite.create_connection(r"c:/py/BRICS-EDA/db_files/pythonsqlite.db")

    # create tables
    if conn is not None:
        sqlite.create_table(conn, sql_create_brics)
        sqlite.create_table(conn, sql_create_countries)
        sqlite.create_table(conn, sql_create_names)
        sqlite.create_table(conn, sql_create_years)
        print('tables created')
    else:
        print("Error! cannot create the database connection.")

    conn.close()