#[1]
#

import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:.2f}'.format
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index('personid', inplace=True)

#[2]
# exploring the 2 groups of columns that need to be tidied
week_cols = ['weeksworked00','weeksworked01','weeksworked02',
  'weeksworked03','weeksworked04']
col_cols = ['colenroct00','colenroct01','colenroct02',
  'colenroct03','colenroct04']

nls97.loc[nls97.originalid.isin([1,2]),['originalid'] + week_cols + col_cols].T

#[3]
# using the wide_to_long function to complete the data modification in one fell swoop

school_work = pd.wide_to_long(nls97.loc[:,['originalid'] + week_cols + col_cols] , stubnames= ['weeksworked','colenroct'], i=['originalid'], j='year').reset_index()
school_work['year'] = school_work.year+2000
school_work = school_work.sort_values(['originalid','year'])
school_work.set_index(['originalid'], inplace=True)
school_work.head(10)

#[4]
# what happens when the columns aren't aligned properly


weeksworkedcols = ['weeksworked00','weeksworked01','weeksworked02',
  'weeksworked04','weeksworked05']
workschool = pd.wide_to_long(nls97[['originalid'] + weeksworkedcols
  + colenrcols], stubnames=['weeksworked','colenroct'],
  i=['originalid'], j='year').reset_index()
workschool['year'] = workschool.year+2000
workschool = workschool.sort_values(['originalid','year'])
workschool.set_index(['originalid'], inplace=True)
workschool.head(12)
