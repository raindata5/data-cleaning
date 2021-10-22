#[1]
#
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index(['originalid'], inplace=True)

#[2]
# stacked data which we will rearrange again shortly
weeksworkedcols = ['weeksworked00','weeksworked01',
  'weeksworked02','weeksworked03','weeksworked04']

weeksworkedstacked = nls97[weeksworkedcols].\
  stack(dropna=False)
weeksworkedstacked.loc[[1,2]]
weeksworkedstacked.index #Multiindex

#[3]
# melted data which we will rearrange again shortly

weeksworkedmelted = nls97.reset_index().\
  loc[:,['originalid'] + weeksworkedcols].\
  melt(id_vars=['originalid'], value_vars=weeksworkedcols,
    var_name='year', value_name='weeksworked')

weeksworkedmelted.loc[weeksworkedmelted.originalid.isin([1,2])].\
  sort_values(['originalid','year'])


#[4]
# untidying data
weeksworked = weeksworkedstacked.unstack()
weeksworked.loc[[1,2]]
weeksworked.head(10)

#[5]
# similar to pivot table
weeksworked = weeksworkedmelted.pivot(index='originalid', columns='year', values='weeksworked').reset_index()

#[6]
# modifying the data so the column name year isn't shown on top of index
weeksworked.columns = ['originalid'] + [col for col in weeksworked.columns[1:]]

weeksworked.loc[weeksworked.originalid.isin([1,2])].T

#[7]
#

