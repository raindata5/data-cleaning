#[1]
#
import pandas as pd

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

#[2]
# reviewing data structure
nls97.iloc[:,0:8].info()

#[3]
# looking at the value counts for multiple variables
 catvars = ['gender','maritalstatus','highestdegree']

for col in catvars :
    print(col,nls97[col].value_counts().sort_index(), sep= '\n\n', end='\n\n\n' )

#[4]
# summary statistics for various variables

cont_vars= ['satmath','satverbal','weeksworked06','gpaoverall',
  'childathome']

nls97[cont_vars].describe()


#[5]
#getting the mean satmath score conditioned on gender

nls97.groupby('gender')['satmath'].mean()

#[6]
# getting the mean satmath score conditioned on gender and degree
nls97.groupby(['gender','highestdegree'])['satmath'].mean()

#[7]
# getting the mean satmath and satverbal score conditioned on gender and degree
nls97.groupby(['gender','highestdegree'])[['satmath','satverbal']].mean()

#[8]
# running multiple agg functions on overall gpa conditioned on gender and degree
nls97.groupby(['gender','highestdegree'])['gpaoverall'].agg(['count','mean','max','std'])

#[9]
# using a dictionary with agg to produce multiple aggregations for different columns and even aggregations aren't the same across columns

aggdict = {'weeksworked06':['count', 'mean', 'max','std'], 'childathome':['count', 'mean', 'max', 'std']}
nls97.groupby(['highestdegree']).agg(aggdict)
nls97.groupby(['maritalstatus']).agg(aggdict)

aggdict1 = {'weeksworked06':['count', 'mean', 'max','sum','std'], 'childathome':['count', 'mean', 'max', 'std']} # don't have to specify the same aggregations nor the same amount of agg

nls97.groupby(['highestdegree']).agg(aggdict1)
