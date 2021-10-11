import pandas as pd
import numpy as np

#[1]
# reading in data and setting appropriate index
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)
landtemps = pd.read_csv("data/landtemps2019avgs.csv")

#[2]
# getting the quantiles to create categorical labels and then group by them to run aggregate functions between each
landtemps.elevation.quantile(np.arange(.2,1.1,.2))

landtemps['elevation_group'] = np.where(landtemps.elevation>landtemps.elevation.quantile(0.8), 'high', 'low')
landtemps.elevation_group = landtemps.elevation_group.astype('category')
landtemps.groupby(['elevation_group'])['elevation'].agg(['sum','min','max'])

#[3]
# nesting the np where functions to create 3 labels and then run another series of aggregate functions

landtemps['elevation_group'] = np.where(landtemps['elevation']>landtemps['elevation'].quantile(.80),'high',
    np.where(landtemps['elevation']>landtemps['elevation'].median(),'medium','Low') ) # the function is evaluated in order so the values that also fit in the medium category won't be labeled as medium (the first condition that is true is used)

landtemps['elevation_group'] = landtemps['elevation_group'].astype('category')

landtemps.groupby(['elevation_group'])['elevation'].agg(['sum','max','min','mean'])

#[4]
# using np select to conduct more complex categorization

cond_list = [(nls97.gpaoverall < 2) & (nls97.highestdegree == '0. None'), nls97.highestdegree=='0. None', nls97.gpaoverall<2]

choice_list = ['1. Low GPA and No Diploma', '2. No Diploma', '3. Low GPA']

nls97['hsachieve'] = np.select(cond_list,choice_list, '4. Did Okay') # last values reserved as an "else" category
nls97[['hsachieve','gpaoverall','highestdegree']].head()
nls97.hsachieve.value_counts().sort_index()

#[5]
# using filter to take college enrollment columns and see whether or not an observations has done so at a point with apply and any

nls97.filter(like='colenr').loc[[100292,100583,100139],:].T
nls97.filter(like='colenr').loc[[100292,100583,100139],:].apply(lambda x : x.str[0:1] == '3').T

nls97['baenrollment'] = nls97.filter(like='colenr').apply(lambda x : x.str[0:1] == '3').any(axis=1)

nls97.loc[[100292,100583,100139],['baenrollment']].T

nls97['baenrollment'].value_counts()

#[6]
#function for assigning each observation a category in accordance with their sleep habits and a few other variables
def getsleepdeprivedreason(row):
  sleepdeprivedreason = "Unknown"
  if (row.nightlyhrssleep>=6): #determines whether obs. is Sleep Deprived or not
    sleepdeprivedreason = "Not Sleep Deprived"
  elif (row.nightlyhrssleep>0): #using elif allows us to not have to check the value again if it already matched in the prev. if statement
    if (row.weeksworked16+row.weeksworked17 < 80): #if deprived of sleep and it doesn't seem to stem from work then this
      if (row.childathome>2): #due to children
        sleepdeprivedreason = "Child Rearing"
      else: # don't have the information
        sleepdeprivedreason = "Other Reasons"
    else: #if hours are more than 80 then
      if (row.wageincome>=62000 or row.highestgradecompleted>=16): # characteristics associated with more work responsibilities
        sleepdeprivedreason = "Work Pressure"
      else: #obs. stressed about income
        sleepdeprivedreason = "Income Pressure"
  else: # the survery is null or 0
    sleepdeprivedreason = "Unknown"
  return sleepdeprivedreason

nls97['sleepdeprivedreason'] = nls97.apply(getsleepdeprivedreason,axis=1)
nls97.sleepdeprivedreason = nls97.sleepdeprivedreason.astype('category')
nls97.sleepdeprivedreason.value_counts()
