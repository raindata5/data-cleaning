
#[1]
#

import pandas as pd
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")

#[2]
# using a checkmerge variation which is robust to joining on a different column (name is different) for each dataframe
def checkmerge(dfleft, dfright, mergebyleft, mergebyright):
  dfleft['inleft'] = "Y"
  dfright['inright'] = "Y"
  dfboth = pd.merge(dfleft[[mergebyleft,'inleft']],\
    dfright[[mergebyright,'inright']], left_on=[mergebyleft],\
    right_on=[mergebyright], how="outer")
  dfboth.fillna('N', inplace=True)
  print(pd.crosstab(dfboth.inleft, dfboth.inright))
  print(dfboth.loc[(dfboth.inleft=='N') | (dfboth.inright=='N')].head(20))

checkmerge(countries.copy(), locations.copy(), "countryid", "countryid")

#[]
# sample values from each side to see which would be retained
countries.loc[countries.countryid.isin(["LQ","ST"])]
locations.loc[locations.countryid=="FO"]

#[3]
# carrying out the merge and checking the results

stations = pd.merge(countries, locations, left_on=["countryid"], right_on=["countryid"], how="left")
stations[['locationid','latitude','stnelev','country']].head(10)
stations.shape

stations.loc[stations.countryid=="FO"]

stations.loc[stations.countryid.isin(["LQ","ST"])]
