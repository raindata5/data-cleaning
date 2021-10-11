
#[]
#

import pandas as pd
countries = pd.read_csv("data/ltcountries.csv")
locations = pd.read_csv("data/ltlocations.csv")

#[]
#
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
#

stations = pd.merge(countries, locations, left_on=["countryid"], right_on=["countryid"], how="left")
stations[['locationid','latitude','stnelev','country']].head(10)
stations.shape

stations.loc[stations.countryid=="FO"]

stations.loc[stations.countryid.isin(["LQ","ST"])]
