import pandas as pd

#[1]
#

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97c.csv")
nls97.set_index("personid", inplace=True)

#[2]
#
nls97.info()

schoolrecordlist = ['satverbal','satmath','gpaoverall','gpaenglish',
  'gpamath','gpascience','highestdegree','highestgradecompleted']

demolist = ['maritalstatus','childathome','childnotathome',
  'wageincome','weeklyhrscomputer','weeklyhrstv','nightlyhrssleep']

school_record = nls97.loc[:,schoolrecordlist]

demo = nls97.loc[:,demolist]

school_record.shape
demo.shape

#[3]
#looking at homany nulls are present by column and the absolute frequencies for null values by observations

school_record.isnull().sum(axis=0)
school_record.isnull().sum(axis=1).value_counts().sort_index()

school_record.loc[school_record.isnull().sum(axis=1)>=7].head(5).T # observing some examples of rows with 7 null values or mmore to see  what to do with them

#[4]
# dropping rows that have less than 2 non-null values

school_record = school_record.dropna(thresh=2) # removing rows with less than 2 values
school_record.shape
school_record.isnull().sum(axis=1).value_counts().sort_index()

#[5]
# imputing missing values in the gpaoverall column with the mean of the column
int(school_record.gpaoverall.mean())

school_record.gpaoverall.isnull().sum()

school_record.gpaoverall.fillna(school_record.gpaoverall.mean(), inplace=True)
school_record.gpaoverall.isnull().sum()

#[6]
# using forward fill to impute the values immediately prior to the null in the data
# this probably wouldn't be the best case here since the across observations is independent and also
# forward fill works better when there are less outliers amongst other considerations
demo.wageincome.head().T
demo.wageincome.isnull().sum()
demo.wageincome.fillna(method='ffill', inplace=True)

demo.wageincome.head().T
demo.wageincome.isnull().sum()

#[7]
# imputing the mean weeks worked by group (highest-degree-earned)

nls97[['highestdegree','weeksworked17']].head()
workbydegree = nls97.groupby(['highestdegree'])['weeksworked17'].mean().reset_index().\
    rename(columns={'weeksworked17':'meanweeksworked17'}) #resetting the index to get the highest degree back in the dataframe's columns

# example of what not to do when merging the index is lost
nls971 = nls97.copy()
nls971.merge(workbydegree, how='left', left_on=['highestdegree'], right_on=['highestdegree']).set_index('personid') # on merge index is lost so must place it back in the dataframe first

# resetting the index
nls97 = nls97.reset_index().merge(workbydegree, how='left', left_on=['highestdegree'], right_on=['highestdegree']).set_index('personid')

nls97.weeksworked17.fillna(nls97.meanweeksworked17, inplace=True)

#[8]
# inspecting the data to see how values were imputed
nls97.loc[:, ['highestdegree','weeksworked17','meanweeksworked17']].head()
