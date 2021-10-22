import pandas as pd
import numpy as np
from datetime import datetime

#[1]
#
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 220)
pd.options.display.float_format = '{:,.0f}'.format
covidcases = pd.read_csv("data/covidcases720.csv")
nls97 = pd.read_csv("data/nls97c.csv")
nls97.set_index("personid", inplace=True)

#[2]
# inspecting the potential columns we can use to create datetime values

nls97[['birthmonth','birthyear']].head()
nls97[['birthmonth','birthyear']].isnull().sum()
nls97.birthmonth.value_counts().sort_index()
nls97.birthyear.value_counts().sort_index()

#[2]
# using fillna to impute the mean of the birthmonth column to the missing value

nls97.birthmonth.fillna(int(nls97.birthmonth.mean()), inplace=True) #changing to int data type to remove decimals
nls97.birthmonth.value_counts().sort_index()

#[3]
# using to_datetime function to place need values in a dictionary and create a datetime column

nls97['birthdate'] = pd.to_datetime(dict(year=nls97.birthyear, month=nls97.birthmonth, day=15)) #check pd.to_Datetime documentation again
nls97.birthdate.describe(datetime_is_numeric=True)
nls97[['birthmonth','birthyear','birthdate']].head()
nls97[['birthmonth','birthyear','birthdate']].isnull().sum()

#[4]
# creating an age variable


def calc_age(startdate, enddate):
  age = enddate.year - startdate.year
  if (enddate.month<startdate.month or (enddate.month==startdate.month and enddate.day<startdate.day)):
    age = age -1
  return age


rundate = pd.to_datetime('2021-10-02')
nls97["age"] = nls97.apply(lambda x: calc_age(x.birthdate, rundate), axis=1)
nls97.loc[100061:100583, ['age','birthdate']]


#[5]
#using to_datetime to format a column's values

nls97.dtypes
covidcases.iloc[:, 0:6].sample(2, random_state=10).T
covidcases['casedate'] = pd.to_datetime(covidcases.casedate, format='%Y-%m-%d')
nls97.dtypes

#[6]
# get summary statistics for the casedate colum
covidcases.casedate.describe(datetime_is_numeric=True)

#[7]
# creating a column that shows the days since the first date with a covid case

firstcase = covidcases.loc[covidcases.new_cases>0,['location','casedate']]. #first getting the days with at least one case and then sorting it by the region and earliest of these days
  sort_values(['location','casedate']).drop_duplicates(['location'], keep='first').rename(columns={'casedate':'firstcasedate'}) # sorted we can can drop every duplicates in locations but the first occurence found in the data
#a similar method using groupby and then using the aggregate function min would have helped to get similar results



# merging the 2 dfs and subtracting the first case date from each current case date
# this way we can see some countries who started reporting data long before they had an cases
covidcases = pd.merge(covidcases, firstcase, left_on=['location'], right_on=['location'], how="left")
covidcases['dayssincefirstcase'] = covidcases.casedate - covidcases.firstcasedate
covidcases.dayssincefirstcase.describe()


