#[1]
#

import pandas as pd
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index("originalid", inplace=True)
nls97add = pd.read_csv("data/nls97add.csv")

#[2]
# exploring the 2 datasets

nls97.head()
nls97.shape
nls97add.head()
nls97add.shape

#[3]
# prior to merging checking to see if the number of unique values is equal to the amount of rows in order to confirm this is a one-to-one merge
nls97.originalid.nunique()==nls97.shape[0]
nls97add.originalid.nunique()==nls97add.shape[0]

#[4]
# modifying select values to show nature of different joins when there are non-matching values among the keys

nls97 = nls97.sort_values('originalid')
nls97add = nls97add.sort_values('originalid')
nls97.iloc[0:2, -1] = nls97.iloc[0:2, -1]+10000
nls97.originalid.head(2)
nls97add.iloc[0:2, 0] = nls97add.iloc[0:2, 0]+20000
nls97add.originalid.head(2)

#[5]
#doing a left join on indexes
nlsnew = nls97.join(nls97add.set_index(['originalid']))
nlsnew.loc[nlsnew.originalid>9999, ['originalid','gender','birthyear','motherage','parentincome']]

#[6]
# another left join but with merge function
nlsnew = pd.merge(nls97, nls97add, on=['originalid'], how="left")
nlsnew.loc[nlsnew.originalid>9999, ['originalid','gender','birthyear','motherage','parentincome']]

#[7]
# right join
nlsnew = pd.merge(nls97, nls97add, on=['originalid'], how="right")
nlsnew.loc[nlsnew.originalid>9999, ['originalid','gender','birthyear','motherage','parentincome']]

#[8]
# inner join

nlsnew = pd.merge(nls97, nls97add, on=['originalid'], how="inner")
nlsnew.loc[nlsnew.originalid>9999, ['originalid','gender','birthyear','motherage','parentincome']]

#[9]
# outer join
nlsnew = pd.merge(nls97, nls97add, on=['originalid'], how="outer")
nlsnew.loc[nlsnew.originalid>9999, ['originalid','gender','birthyear','motherage','parentincome']]

#[10]
# function to check for mismatches
def check_merge(left_df, right_df ,idvar):
    left_df['inleft'] = 'Y'
    right_df['inright'] = 'Y'
    both_df = pd.merge(left_df[[idvar,'inleft']],right_df[[idvar,'inright']], on=[idvar], how='outer')
    both_df.fillna('N',inplace=True)
    print(pd.crosstab(both_df.inleft,both_df.inright))

check_merge(nls97,nls97add, "originalid")
