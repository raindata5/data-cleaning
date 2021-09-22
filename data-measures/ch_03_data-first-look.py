import pandas as pd
import numpy as np

#[]
#editing display of the output
pd.set_option('display.width', 70)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.0f}'.format
#[]
#reading in data and changing column to datetime
nls97 = pd.read_csv("data/nls97.csv")
covidtotals = pd.read_csv("data/covidtotals.csv",parse_dates=['lastdate'])

#[]
# setting index as personid and examining different aspects of the data
nls97.set_index('personid',inplace=True)
nls97.index
nls97.shape
nls97.index.nunique()
nls97.info()
nls97.head(2).T #transposing the output to make it look better

#[]
# setting the iso_code as the index for each country
covidtotals.set_index('iso_code',inplace=True)
covidtotals.index
covidtotals.shape
covidtotals.index.nunique()
covidtotals.info()

#[]
#sampling 2 countries from the data set and including random_state for reproducibility
covidtotals.sample(2,random_state=2).T
