# BRICS - World Bank Indicators EDA 

The objective of this project is to explore and analyze data about BRICS.  
  
BRICS refers to the combined economies of Brazil, Russia, India, China and South Africa. In this project, we'll use the World Bank Indicators data to explore and understand more about the five countries considered emerging economies.  

## Cleaning
The Jupyter Notebook `ipynb/cleaning.ipynb` goes into more detail about the cleaning process and its development. 

### Source Schema
__EducationAndEnviron_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__HealthAndPoverty_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__PrivateSector_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__PublicSector_Indicators.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__Economy_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  

### Transformed Schema
__brics__ -> [SeriesIndex, CountryCode, Year, Value]  
__countries__ -> [CountryName, CountryCode]  
__names__ -> [SeriesIndex, SeriesName, SeriesCode, Category]  
__years__ -> [Years, Filter_Years]

\* The table __years__ has a 'many to many' relationships with the fact table (brics). That allows us to create a filter for the year and retrieve the last year available, regardless of the selected year having missing records. 

## ETA

The data is downloaded from Kaggle, cleaned, and saved to an SQLite database. A Flask app then reads the database and transmits the data as .json files through API calls.

## Analysis and Visualizations
We will perform the Data analysis and visualizations with MS Power BI. The idea is to explore and learn about the BRICS countries using data from the World Bank Indicators to illustrate and tell a story about the group.

## Requirements

Kaggle API  
`pip install Kaggle`

Pandas  
`pip install pandas`

MissingNo  
`pip install missingno`

SQLite  
`pip install sqlite3`

Flask
`pip install flask`

Microsoft Power BI  
https://powerbi.microsoft.com/en-us/desktop/

Data  
https://www.kaggle.com/docstein/brics-world-bank-indicators