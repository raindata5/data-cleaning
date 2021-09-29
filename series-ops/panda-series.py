import pandas as pd


pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

#[1]
# isolating gpaoverall as a series

gpaoverall = nls97.gpaoverall
type(gpaoverall)


gpaoverall.index()

#[2]
#using slice notation to get different slices of the series
gpaoverall.head()
gpaoverall[:5]
gpaoverall.tail()
gpaoverall[-5:]

#[3]
# selecting more data using the bracket operator and also using loc to select by index labels
gpaoverall[999963]
gpaoverall[[999963]]
gpaoverall.loc[[100061,100139,100284]]
gpaoverall.loc[100061:100833]


#[4]
# using row positions to select data

gpaoverall.iloc[[0]]
gpaoverall.iloc[[0,1,2,3,4]]
gpaoverall.iloc[:5]
gpaoverall.iloc[-5:]
