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
# multipying a whole panda series by 100 through vectorization

nls97.gpaoverall.head()
gpaoverall100=nls97['gpaoverall'] * 100
gpaoverall100.head()

#[3]
# changing individual values and a group of values based on the index value

nls97.loc[[100061], 'gpaoverall'] = 3
nls97.loc[[100139,100284,100292],'gpaoverall'] = 0
nls97.gpaoverall.head()

#[4]
#adding together 2 pandas series to get the total number of children an observation has had
nls97['childnum'] = nls97.childathome + nls97.childnotathome
nls97.childnum.value_counts().sort_index()

#[5]
#imputing the mean gpa to a range of observations
nls97.loc[100061:100292,'gpaoverall'] = nls97.gpaoverall.mean()
nls97.gpaoverall.head()

#[6]
#using iloc to change values
nls97.iloc[0, 13] = 2
nls97.iloc[1:4, 13] = 1
nls97.gpaoverall.head()

#[7]
# showing the nth largest values and then change those values above 4 to 4

nls97.gpaoverall.nlargest()
nls97.loc[nls97.gpaoverall>4, 'gpaoverall'] = 4
nls97.gpaoverall.nlargest()

#[8]
# seeing how a string the in the column area will return a Series versus a list which returns a DataFrame
type(nls97.loc[[100061], 'gpaoverall'])
nls97.loc[[100061],'gpaoverall']


type(nls97.loc[[100061], ['gpaoverall']])
nls97.loc[[100061],['gpaoverall']]
