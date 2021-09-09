import pandas as pd
import numpy as np
import pyreadr
import pprint


#[]
# loading in rds file with the index None since rds just gives one file as opposed to R data
nls97r = pyreadr.read_r('data/nls97.rds')[None]
nls97r.head(10)

#will open dictionary contained in codes file
with open('data/nlscodes.txt','r') as reader:
    setvalues = eval(reader.read())

pprint.pprint(setvalues)

# new columns to be used
newcols = ['personid','gender','birthmonth','birthyear',
  'sampletype',  'category','satverbal','satmath',
  'gpaoverall','gpaeng','gpamath','gpascience','govjobs',
  'govprices','govhealth','goveld','govind','govunemp',
  'govinc','govcollege','govhousing','govenvironment',
  'bacredits','coltype1','coltype2','coltype3','coltype4',
  'coltype5','coltype6','highestgrade','maritalstatus',
  'childnumhome','childnumaway','degreecol1',
  'degreecol2','degreecol3','degreecol4','wageincome',
  'weeklyhrscomputer','weeklyhrstv',
  'nightlyhrssleep','weeksworkedlastyear']

  #[]
  #

  nls97r.replace(setvalues,inplace=True)
  nls97r.head()
  nls97r.replace(list(range(-9,0)), np.nan, inplace=True)


#interesting piece of code which lists the columns we just edited and then listing those columns with . columns for them to be iterated through

for col in nls97r[[k for k in setvalues]].columns:
    nls97r[col] = nls97r[col].astype('category')

nls97r.dtypes

nls97r.columns = newcols
nls97r.dtypes
nls97r['personid'].columns
