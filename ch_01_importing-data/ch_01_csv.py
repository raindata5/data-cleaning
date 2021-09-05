import pandas as pd

# []
# making the output easier to see

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 8)

# []

landtemps = pd.read_csv('data/landtempssample.csv', names=['stationid','year',
    'month','avgtemp','latitude','longitude','elevation','station','countryid','country'],
    skiprows=1,parse_dates=[['month','year']],low_memory=False)

#[]
# quick glimpse of the data
landtemps.head(10)

landtemps.dtypes
landtemps.shape

#[]
# modifying column names and chechking summary stats for avgtemp

landtemps.rename(columns={'month_year':'measuredate'},inplace=True)
landtemps.avgtemp.describe()

#[]
# going to check for nulls
landtemps.isnull().sum()

#[]
# dropping rows with na for measuredate since key to analysis
landtemps.dropna(subset=['avgtemp'],inplace=True)
# default is 0
landtemps.shape
