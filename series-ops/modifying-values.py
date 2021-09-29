import pandas as pd

#[1]
# reading in data and setting appropriate index

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

#[2]
#

nls97.gpaoverall.head()
gpaoverall100=nls97['gpaoverall'] * 100
gpaoverall100.head()

#[]
#

nls97.loc[[100061], 'gpaoverall'] = 3
nls97.loc[[100139,100284,100292],'gpaoverall'] = 0
nls97.gpaoverall.head()

#[]
#
nls97['childnum'] = nls97.childathome + nls97.childnotathome
nls97.childnum.value_counts().sort_index()

#[]
#
nls97.loc[100061:100292,'gpaoverall'] = nls97.gpaoverall.mean()
nls97.gpaoverall.head()

#[]
#
nls97.iloc[0, 13] = 2
nls97.iloc[1:4, 13] = 1
nls97.gpaoverall.head()

#[]
#

nls97.gpaoverall.nlargest()
nls97.loc[nls97.gpaoverall>4, 'gpaoverall'] = 4
nls97.gpaoverall.nlargest()

#[]
#
type(nls97.loc[[100061], 'gpaoverall'])
nls97.loc[[100061],'gpaoverall']


type(nls97.loc[[100061], ['gpaoverall']])
nls97.loc[[100061],['gpaoverall']]
