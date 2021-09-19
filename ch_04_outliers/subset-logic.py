import pandas as pd
import numpy as np
pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

#[]
#

nls97[['wageincome','highestgradecompleted','highestdegree']].head(3).T

nls97.loc[:, "weeksworked12":"weeksworked17"].head(3).T
nls97.loc[:, "colenroct09":"colenrfeb14"].head(3).T

#[]
#review
nls97.loc[(nls97.weeksworked16==0) & nls97.wageincome>0, ['weeksworked16','wageincome']]
nls97.filter(like="colenr").apply(lambda x: x.str[0:1]=='3').head(2).T
nls97.filter(like="colenr").apply(lambda x: x.str[0:1]=='3').any(axis=1).head(2)

#[]
#review
bachskip = nls97.loc[(nls97.filter(like="colenr").apply(lambda x : x.str[:1]=='4').any(axis=1)) & ~(nls97.filter(like="colenr").apply(lambda x : x.str[:1]=='3').any(axis=1)),"colenrfeb97":"colenroct17"]

bachskip.shape

#[]
#
degrees = nls97.highestdegree.value_counts(sort=False).sort_index().index[-4:]
degrees = list(degrees)
for y,row in enumerate(degrees):
    degrees[y] = row[0:1]

#[]
#
fouryeardegreeskip = nls97.loc[nls97.highestdegree.str[0:1].isin(degrees) & ~nls97.filter(like="colenr").apply(lambda x: x.str[0:1]=='3').any(axis=1), "colenrfeb97":"colenroct17"]
len(fouryeardegreeskip)
fouryeardegreeskip.head(3).T

#[]
#
highwages = nls97.loc[nls97.wageincome > nls97.wageincome.mean()+(nls97.wageincome.std()*3),['wageincome']]
highwages

#[]
#


workchanges = nls97.loc[~nls97.loc[:,"weeksworked12":"weeksworked16"].mean(axis=1).between(nls97.weeksworked17*0.5,nls97.weeksworked17*2)& ~nls97.weeksworked17.isnull(),
"weeksworked12":"weeksworked17"]
len(workchanges)
workchanges.head(7).T


#[]
#
ltgrade12 = nls97.loc[nls97.highestgradecompleted<12, ['highestgradecompleted','highestdegree']]

pd.crosstab(ltgrade12.highestgradecompleted, ltgrade12.highestdegree)
