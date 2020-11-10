# BRICS - World Bank Indicators EDA 

The objective of this project is to explore and analyze data about BRICS.  
  
BRICS refers to the combined economies of Brazil, Russia, India, China and South Africa. In this project, we'll use the World Bank Indicators data to explore and understand more about the five countries considered emerging economies.  

[Dashboard](https://thiagobc23.github.io/BRICS-EDA/)

## ETA
The data is downloaded from Kaggle, cleaned, and saved to an SQLite database. A Flask app then reads the database and transmits the data as .json files through API calls.

The Jupyter Notebook `ipynb/cleaning.ipynb` goes into more detail about the cleaning process and its development. 

This project is also available with a 

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

## Analysis and Visualizations
We will perform the Data analysis and visualizations with MS Power BI. The idea is to explore and learn about the BRICS countries using data from the World Bank Indicators to illustrate and tell a story about the group.

The Power Bi dashboard has two pages. The first is more static in a report format and contains an overview for each country, we tried to convey a story where we first try to draw a general perception of the country, it's name, flag, location, area, population (urban and rural), and currency.
The following visualizations tell more about the population displaying it's distribution by sex and age. Then we tell more about the economy with GDP, GDP per capita, number of days to open a business, numbers of imports and exports of goods and services. After those we go for health with indicators of numbers of physicians, nurses, hospital beds, and life expectancy. We end with education and unemployment

## Technologies
This project was built mostly to learn and explore methods, technologies, and different ways of achieving the same results. We extracted the data to `.csv`, `.json`, moved it to SQLite, built a Flask API to pull it again, and we still plan to explore MongoDB.  

Visualization wise, we explored the many different ways to load our cleaned data into Power BI and other sources such as the API to get the current currency values. We also had to work the data inside PBI, creating measures, calculated columns.

Besides ETA and Visualizations, we also explored Docker (`\Dockerfile`), PIP (`\requirements.txt`), and github.io pages (https://thiagobc23.github.io/BRICS-EDA/)

## Requirements

Kaggle API  
`pip install Kaggle`  
\* You also need a Kaggle account and the authentication file - `kaggle.json`

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
https://api.exchangeratesapi.io  

### Authors:  
[adrianonsilva](https://github.com/adrianonsilva)  
[thiagobc23](https://github.com/thiagobc23)  
