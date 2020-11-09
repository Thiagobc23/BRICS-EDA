import os
import shutil
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import kaggle

class clean:

    def get_data(path):
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files('docstein/brics-world-bank-indicators', path=path, unzip=True)
        print('data downloaded')

        # move files
        source = '{}BRICS Development Indicators'.format(path)
        data_dir = '{}data/'.format(path)
        files = ['Economy_Data.csv','EducationAndEnviron_Data.csv','HealthAndPoverty_Data.csv',
                'PrivateSector_Data.csv','PublicSector_Indicators.csv']

        for f in files:
            shutil.move(os.path.join(source, f), os.path.join(data_dir, f))
        
        # delete folder
        shutil.rmtree(source)
        print('files moved')
        # Define datasets
        df_ed_env = pd.read_csv('{}EducationAndEnviron_Data.csv'.format(data_dir), sep=';')
        df_ed_env['Category'] = ['Education and Enviorment']*len(df_ed_env)

        df_health_pov = pd.read_csv('{}HealthAndPoverty_Data.csv'.format(data_dir), sep=';')
        df_health_pov['Category'] = ['Health and Poverty']*len(df_health_pov)

        df_priv = pd.read_csv('{}PrivateSector_Data.csv'.format(data_dir), sep=';')
        df_priv['Category'] = ['Private Sector']*len(df_priv)

        df_pub = pd.read_csv('{}PublicSector_Indicators.csv'.format(data_dir), sep=';')
        df_pub['Category'] = ['Public Sector']*len(df_pub)

        df_econ = pd.read_csv('{}Economy_Data.csv'.format(data_dir), sep=';')
        df_econ['Category'] = ['Economy']*len(df_econ)

        # Concatenate Datasets
        df = pd.concat([df_ed_env, df_health_pov, df_priv, df_pub, df_econ])
        
        print('dataframe created')
        return df
    
    # Clean 
    def process(df, path):
        ## SeriesName
        mask = pd.isnull(df.SeriesName)
        len(df[mask])
        ### drop 750 rows with missing series name
        df = df[~mask]

        ## SeriesCode
        mask = pd.isnull(df.SeriesCode)
        len(df[mask])
        ### drop 500 rows with missing series code
        df = df[~mask]

        ## Value
        mask = pd.isnull(df.Value)
        len(df[mask])
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
        fact = df[cols].rename(columns={'index':'SeriesIndex'})

        # save files
        d_name.to_csv('{}data/names.csv'.format(path))
        d_country.to_csv('{}data/countries.csv'.format(path))
        d_years.to_csv('{}data/years.csv'.format(path))
        fact.to_csv('{}data/brics.csv'.format(path))

        print('done')