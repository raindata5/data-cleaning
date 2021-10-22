#[1]
#
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:.2f}'.format
cma = pd.read_csv("data/cmacollections.csv")

#[2]
# getting the count of ids after dropping any duplicates (like nunique)

cma.shape
cma.head(3).T
cma.id.nunique()
cma.drop_duplicates(['id','citation']).id.count()
cma.drop_duplicates(['id','creator']).id.count()

#[3]
# exploring the nature of duplicate id values
cma.set_index(['id'], inplace=True)
cma.loc[124733, ['title','citation','creator','birth_year']].head(14)

#[4]
# creating a table so we can eventually get to a bridge table to permit one-to-many merges
conjunta_var = ['title','collection','type']
cmacollections = cma[conjunta_var].\
    reset_index().\
    drop_duplicates(['id']).\
    set_index(['id'])
cmacollections.shape
cmacollections.head()
cmacollections.loc[124733]

#[5]
# ids to citations(many)
cmacitations = cma[['citation']].\
  reset_index().\
  drop_duplicates(['id','citation']).\
  set_index(['id'])

cmacitations.loc[124733]

#[6]
# ids to creators(many)
creatorsvars = ['creator','birth_year','death_year']
cmacreators = cma[creatorsvars].\
  reset_index().\
  drop_duplicates(['id','creator']).\
  set_index(['id'])
cmacreators.loc[124733]


#[7]
# collection items with at least 1 creator of an item that was born after 1950

cmacreators['birth_year'] = cmacreators.birth_year.str
youngartists = cmacreators.loc[cmacreators.birth_year>1950, ['creator']].assign(creatorbornafter1950='Y')
youngartists.shape[0]==youngartists.index.nunique()

#[8]
# merging the data and identifying the rows that fulfill our previous creator criteria
cmacollections = pd.merge(cmacollections, youngartists, left_on=['id'], right_on=['id'], how='left')
cmacollections.creatorbornafter1950.fillna("N", inplace=True)
cmacollections.shape
cmacollections.creatorbornafter1950.value_counts()
