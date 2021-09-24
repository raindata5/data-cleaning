#importing needed libraries for persisting data into a feather file
import pandas as pd
import pyarrow


pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 8)


#[]
# loading in data, dropping rows with missing data and setting the index
landtemps = pd.read_csv('data/landtempssample.csv', names=['stationid','year',
    'month','avgtemp','latitude','longitude','elevation','station','countryid','country'],
    skiprows=1,parse_dates=[['month','year']],low_memory=False)

#renaming auto-generated month_year column from after using parse_dates, also dropping rows where there is a missing date
landtemps.dtypes
landtemps.rename(columns={'month_year':'measuredate'},inplace=True)

landtemps.dropna(subset=['avgtemp'],inplace=True) #default is for rows

landtemps.describe(include='all') # summary stats on other columns than just numeric data
landtemps.set_index(['measuredate','stationid'],inplace=True) # data can be considered as panel data due to their being duplicates of measuredate, then the same for stationid

#[]
#extreme values will be sent to csv and excel files
# these values will be based on quantiles through boolean indexing

extremevals = landtemps[(landtemps.avgtemp < 
    landtemps.avgtemp.quantile(.001)) |            # one or the other
(landtemps.avgtemp > landtemps.avgtemp.quantile(.999))]

extremevals.shape
extremevals.sample(7)

extremevals.to_excel('views/tempext.xlsx')
extremevals.to_csv('views/tempext.csv')

#[]
#now these will be saved/serialized to pickle and feather files
landtemps.to_pickle('views/landtemps.pkl')
landtemps.reset_index(inplace=True)       #feather files require that we reset the index back to normal
landtemps.to_feather('views/landtemps.ftr')

#[]
#now the pickle and feather files will be loaded in just to confirm everythig went fine

landtemps = pd.read_pickle('views/landtemps.pkl')
landtemps.head(2).T
landtemps = pd.read_feather("data/landtemps.ftr")
landtemps.head(2).T
