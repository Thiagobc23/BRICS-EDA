import pandas as pd
import sqlite3
from sqlite3 import Error
import sys

#carregar os dados
df_ed_env = pd.read_csv('EducationAndEnviron_Data.csv', sep=';')
df_ed_env['Category'] = ['Education and Enviorment']*len(df_ed_env)

df_health_pov = pd.read_csv('HealthAndPoverty_Data.csv', sep=';')
df_health_pov['Category'] = ['Health and Poverty']*len(df_health_pov)

df_priv = pd.read_csv('PrivateSector_Data.csv', sep=';')
df_priv['Category'] = ['Private Sector']*len(df_priv)

df_pub = pd.read_csv('PublicSector_Indicators.csv', sep=';')
df_pub['Category'] = ['Public Sector']*len(df_pub)

df_econ = pd.read_csv('Economy_Data.csv', sep=';')
df_econ['Category'] = ['Economy']*len(df_econ)

# Concatenate Datasets
df = pd.concat([df_ed_env, df_health_pov, df_priv, df_pub, df_econ])

## SeriesName
mask = pd.isnull(df.SeriesName)
### drop 750 rows with missing series name
df = df[~mask]

## SeriesCode
mask = pd.isnull(df.SeriesCode)
### drop 500 rows with missing series code
df = df[~mask]

## Value
mask = pd.isnull(df.Value)
### drop 185,515 rows with missing value
df = df[~mask]

# Create Fact table and Dimensions

## Name Dimension
cols = ['SeriesName', 'SeriesCode', 'Category']
d_name = pd.DataFrame(df.groupby(cols).count().index.tolist()).rename(columns={0:cols[0], 1:cols[1], 2:cols[2]})
### Create a new index for the SeriesName/ SeriesCode
d_name.reset_index(inplace=True)
df = pd.merge(df, d_name, on=['SeriesName', 'SeriesCode', 'Category'])

## Country Dimension
cols = ['CountryName', 'CountryCode']
d_country = pd.DataFrame(df.groupby(cols).count().index.tolist()).rename(columns={0:cols[0], 1:cols[1]})

## Years Dimension
years = sorted(df.Year.unique())
filter_years = []
relationship_years = []
for idx, value in enumerate(years):
    for i in range(idx+1):
        filter_years.append(value)
        relationship_years.append(years[idx-i])
        
d_years = pd.DataFrame({'Years': relationship_years, 'Filter_Years': filter_years})

## Fact table
cols = ['index', 'CountryCode', 'Year', 'Value']
d_brics = df[cols].rename(columns={'index':'SeriesIndex'})

#save data to db
conn = sqlite3.connect("brics.db")
cur = conn.cursor()

#years
sql = ''' insert into years(id,Years,Filter_Years)
            values(?,?,?) '''

for index, row in d_years.iterrows():
    parametros = (index,row['Years'],row['Filter_Years'])
    cur.execute(sql, parametros)

#countries
sql = ''' insert into countries(id,CountryName,CountryCode)
            values(?,?,?) '''

for index, row in d_country.iterrows():
    parametros = (index,row['CountryName'],row['CountryCode'])
    cur.execute(sql, parametros)

#names
sql = ''' insert into names(id,SeriesName,SeriesCode,Category)
            values(?,?,?,?) '''

for index, row in d_name.iterrows():
    parametros = (index,row['SeriesName'],row['SeriesCode'],row['Category'])
    cur.execute(sql, parametros)

#brics
sql = ''' insert into brics(id,seriesIndex,countryCode,year,value)
            values(?,?,?,?,?) '''

for index, row in d_brics.iterrows():
    parametros = (index,row['SeriesIndex'],row['CountryCode'],row['Year'],row['Value'])
    cur.execute(sql, parametros)

conn.commit()
conn.close()