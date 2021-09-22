import pandas as pd

#[]
# reading in file and viewing first few rows
percapitagdp = pd.read_excel('data/GDPpercapita.xlsx'
    ,skiprows=4,skipfooter=1,usecols='A,C:T',sheet_name='OECD.Stat export')

percapitagdp.head()

#[]
# getting info on data types and nulls and rows annd columns
percapitagdp.info()

#[]
# renaming column, and also confirming the presence of trailing spaces
    #then stripping those spaces
percapitagdp.rename({'Year':'metro'},inplace=True, axis=1)
percapitagdp.metro.str.startswith(' ').sum()
percapitagdp.metro.str.startswith(' ').any()

percapitagdp.metro.str.endswith(' ').sum()
percapitagdp.metro.str.endswith(' ').any()

percapitagdp['metro'] = percapitagdp['metro'].str.strip()
percapitagdp.metro.str.startswith(' ').any()

#[]
# we coerced the numbers into float type, had to coerce because of potential letters in data
# these coerced values become null we also rename columns

for col in percapitagdp.columns[1:] :
    percapitagdp[col] = pd.to_numeric(percapitagdp[col],errors='coerce')
    percapitagdp.rename({col:'pcGDP' + col},axis=1,inplace=True)

percapitagdp.head()
percapitagdp.dtypes

#[]
# genertating summary statistics
percapitagdp.describe()

#[]
# looking to remove rows where all the yearly gdp values are missing
percapitagdp.dropna(subset=percapitagdp.columns[1:],how='all',inplace=True)
percapitagdp.describe()
percapitagdp.shape

#[]
# will set the metropolitan area as the index
#before doing so must confirm if each metro area is unique
percapitagdp.metro.count()
percapitagdp['metro'].nunique()
percapitagdp.set_index('metro',inplace=True)
percapitagdp.head()

#[]
percapitagdp.iloc[15:20,]
