#[1]
#
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:.2f}'.format
nls97 = pd.read_csv("data/nls97f.csv")

#[2]
# exploring the columns that need to be tidied
nls97.set_index(['originalid'], inplace=True)
weeksworkedcols = ['weeksworked00','weeksworked01','weeksworked02',
  'weeksworked03','weeksworked04']

nls97[weeksworkedcols].head(2).T
nls97.shape

#[3]
# running the stack operatiion then resetting the index to get the originalid as a column
weeksworked = nls97[weeksworkedcols].stack(dropna=False).reset_index().rename(\
    columns={'level_1':'year',0:'weeks_worked'}) # changing the columns names which are modified
#double check functionality for dropna
weeksworked.head(10)
#[4]
# creating a year variable
weeksworked['year'] = weeksworked.year.str[-2:].astype(int)+2000
weeksworked.head(10)
weeksworked.shape

#[5]
# running the melt operatiion which provides more flexibility

weeksworked = nls97.reset_index().loc[:,['originalid'] + weeksworkedcols].melt(id_vars=['originalid'], value_vars= weeksworkedcols ,var_name='year', value_name='weeksworked')

weeksworked['year'] = weeksworked.year.str[-2:].astype(int)+2000
weeksworked.set_index(['originalid'], inplace=True)
weeksworked.loc[[8245,3962]]

#[6]
# doing the same melt operation with a different group of columns
colenrcols = ['colenroct00','colenroct01','colenroct02',
  'colenroct03','colenroct04']

colenr = nls97.reset_index().loc[:,['originalid'] + colenrcols].melt(id_vars='originalid', value_vars=colenrcols, var_name='year', value_name='colenr')

colenr['year'] = colenr.year.str[-2:].astype(int)+2000
colenr.set_index(['originalid'], inplace=True)
colenr.loc[[8245,3962]]

#[7]
# merging the result of our two melt operations
workschool = pd.merge(weeksworked, colenr, on=['originalid','year'], how="inner")
workschool.shape
workschool.loc[[8245,3962]]
