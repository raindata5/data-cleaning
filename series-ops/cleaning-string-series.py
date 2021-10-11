import pandas as pd
import numpy as np

#[1]
#
pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97c.csv")
nls97.set_index("personid", inplace=True)

#[2]
# simplifying the responses for the govprovidejobs column to make it a simple yes or no as to whether the government should provide jobs

nls97.govprovidejobs.value_counts(dropna=False)
pd.Series(np.where(nls97.govprovidejobs.str.contains("not"),'No','Yes')).value_counts(dropna=False) #these
nls97['govprovidejobsnotprob'] = np.where(nls97.govprovidejobs.isnull(), np.nan, np.where(nls97.govprovidejobs.str.contains("not"),'No','Yes')) #mjust account for nulls with np.where or they will go into else categorhy of function
pd.crosstab(nls97.govprovidejobs,nls97.govprovidejobsnotprob) #method of verifying the transformation

#[3]
# correcting data with a leading or trailing space and then simplifying the responses to yes or no for marital status

nls97.maritalstatus.value_counts(dropna=False)

nls97.loc[100061:100583,'maritalstatus'] = 'Married ' # simulation of trailing space
nls97.maritalstatus.head()
nls97.maritalstatus.value_counts()

nls97.maritalstatus.str.startswith(" ").any()
nls97.maritalstatus.str.endswith(" ").any()

 nls97['evermarried'] = np.where(nls97.maritalstatus.isnull(),np.nan, np.where(nls97.maritalstatus.str.strip()=='Never-married', 'no', 'yes'))
pd.crosstab(nls97.maritalstatus,nls97.evermarried)

#[4]
#simplifying the responses to yes or no for whether the observation has gotten their bachelor's degree

nls97['gotba'] = np.where(nls97.highestdegree.isnull(), np.nan, np.where(nls97.highestdegree.str[0:1].isin(['4','5','6','7']),"Yes","No"))
pd.crosstab(nls97.highestdegree, nls97.gotba)

#[5]
# using regex to extract numbers and then transform the values

pd.concat([nls97.weeklyhrstv.head(),nls97.weeklyhrstv.str.findall(r"\d+").head()], axis=1) #regex to find multiple numbers in a text

#functions takes the values to go ahead and bring them closer to the middle of the range of values and if there
# is just one value we will add or subtract from it
def getnum(numlist):
  highval = 0
  if (type(numlist) is list): #testing if a list was returned other the value would correspond to np.nan
    lastval = int(numlist[-1])
    if (numlist[0]=='40'):
      highval = 45
    elif (lastval==2):
      highval = 1
    else:
      highval = lastval - 5
  else:
    highval = np.nan
  return highval

nls97['weeklyhrstvnum'] = nls97.weeklyhrstv.str.findall(r"\d+").apply(getnum)
pd.crosstab(nls97.weeklyhrstv, nls97.weeklyhrstvnum)

#[6]
# replacing the values to ones that would be able to be sorted

comphrsold = ['None','Less than 1 hour a week',
  '1 to 3 hours a week','4 to 6 hours a week',
  '7 to 9 hours a week','10 hours or more a week']
comphrsnew = ['A. None','B. Less than 1 hour a week',
  'C. 1 to 3 hours a week','D. 4 to 6 hours a week',
  'E. 7 to 9 hours a week','F. 10 hours or more a week']
nls97.weeklyhrscomputer.value_counts().sort_index()
nls97.weeklyhrscomputer.replace(comphrsold, comphrsnew, inplace=True)
nls97.weeklyhrscomputer.value_counts().sort_index()
