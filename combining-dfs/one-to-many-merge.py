#[1]
#

import pandas as pd
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")

#[2]
# setting the index to facilitate subsequent join operation
countries.set_index(['countryid'], inplace=True)
locations.set_index(['countryid'], inplace=True)
countries.head()
countries.index.nunique()==countries.shape[0] # the number of rows is equal to the the number of unique countries (this confirms the nature of our join)
locations[['locationid','latitude','stnelev']].head(10)

#[2]
# performing the join and then inspecting the dataset
stations = countries.join(locations)
stations[['locationid','latitude','stnelev','country']].head(10)

#[3]
# reloading in the dataset to use our function to check for any discrepancy in the merge by column
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")

def checkmerge(dfleft, dfright, idvar):
    dfleft['inleft'] = "Y"
    dfright['inright'] = "Y"
    dfboth = pd.merge(dfleft[[idvar,'inleft']],\
    dfright[[idvar,'inright']], on=[idvar], how="outer")
    dfboth.fillna('N', inplace=True)
    print(pd.crosstab(dfboth.inleft, dfboth.inright))
    print(dfboth.loc[(dfboth.inleft=='N') | (dfboth.inright=='N')])

checkmerge(countries.copy(), locations.copy(), "countryid")


#[4]
# inspecting the particular values that wouldn't be retained
countries.loc[countries.countryid.isin(["LQ","ST"])]
locations.loc[locations.countryid=="FO"]

#[5]
# left join on data
stations = pd.merge(countries, locations, on=["countryid"], how="left")
stations[['locationid','latitude','stnelev','country']].head(10)
stations.shape
stations.loc[stations.countryid.isin(["LQ","ST"])].isnull().sum()
