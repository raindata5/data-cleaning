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
#
percapitagdp.describe()
