
#[1]
#

import pandas as pd
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.2f}'.format
nls97weeksworked = pd.read_csv("data/nls97weeksworked.csv")
nls97colenr = pd.read_csv("data/nls97colenr.csv")

#[2]
# exploring the data and confirming the amount of unique values in first df (with 5 years for each individual this would bring us to our current row count)
nls97weeksworked.sample(10,random_state=42)

nls97weeksworked.shape
nls97weeksworked.originalid.nunique()

#[3]
# exploring the data and confirming the amount of unique values in second df
nls97colenr.sample(10,random_state=42)

nls97colenr.shape
nls97colenr.originalid.nunique()

#[4]
# checking to make sure there is but 1 value for groups of originalid and year (otherwise if there was more then we'd have duplicates)
nls97weeksworked.groupby(['originalid','year'])['originalid'].count().shape

nls97colenr.groupby(['originalid','year'])['originalid'].count().shape

len(nls97colenr.groupby(['originalid','year']).groups) #this method is a bit more intuitive for me

#[5]
# a function for checking for missing pairs with functionality for joining on 2+ columns

def checkmerge(dfleft, dfright, idvar):
    dfleft['inleft'] = "Y"
    dfright['inright'] = "Y"
    dfboth = pd.merge(dfleft[idvar + ['inleft']],dfright[idvar + ['inright']], on=idvar, how="outer")
    dfboth.fillna('N', inplace=True)
    print(pd.crosstab(dfboth.inleft, dfboth.inright))

# going to use copies to not affect the original df's
checkmerge(nls97weeksworked.copy(),nls97colenr.copy(), ['originalid','year'])

#[6]
# carrying out the inner join
nlsworkschool = pd.merge(nls97weeksworked, nls97colenr, on=['originalid','year'], how="inner")
nlsworkschool.shape
nlsworkschool.sample(10, random_state=1)
