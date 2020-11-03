# BRICS - World Bank Indicators EDA 

The objective of this project is to explore and analyse data about BRICS.  
  
BRICS refers to the combined economies of Brazil, Russia, India, China and South Africa. In this project we'll make use of the World Bank Indicators data to explore and understand more about the five countries considered as emerging economies.  

## Cleaning
Data cleaning is performed with Python; the Jupyter Notebook `cleaning.ipynb` contains the steps to merge the datasets from Kaggle into a single data frame, remove empty records, check the integrity of the dataset, and separate the dataframe into dimensions that will later be used to perform the EDA.

### Source Schema
__EducationAndEnviron_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__HealthAndPoverty_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__PrivateSector_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__PublicSector_Indicators.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  
__Economy_Data.csv__ -> [SeriesName, SeriesCode, CountryName, CountryCode, Year, Value]  

### Transformed Schema
__brics.csv__ -> [SeriesIndex, CountryCode, Year, Value]  
__countries__ -> [CountryName, CountryCode]  
__names__ -> [SeriesIndex, SeriesName, SeriesCode, Category]  
__years__ -> [Years, Filter_Years]

\* The table 'years' was designed to have a many to many relationship with the the fact table (brics). That allow us to create a filter for the year and retrieve the last year available, regardless if the selected year has a missing records.

## Analysis and Visualizations
Data exploration will be performed with MS Power BI. The idea is to explore and learn about the countries of BRICS using data from the World Bank Indicators to illustrate and tell a story about the group.

## Complementary information
Other data sources may be useful to illustrate the story and will be explored. In special data sources that can not only add value to the story but also display the use of different technologies. By the end of the project I'll try to add at least one web scrapper and make use of at least one API.

## Requirements

Kaggle API  
`pip install Kaggle`

Pandas  
`pip install pandas`

MissingNo  
`pip install missingno`

Microsoft Power BI  
https://powerbi.microsoft.com/en-us/desktop/

Data  
https://www.kaggle.com/docstein/brics-world-bank-indicators