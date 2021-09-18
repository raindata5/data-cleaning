#[1]
#reading in data and setting index as well as importing needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format


covidtotals = pd.read_csv('data/covidtotals.csv',parse_dates=['lastdate'])
covidtotals.info()
covidtotals.set_index('iso_code',inplace=True)

#[2]
#taking a look at the structure of the data
covidtotals.shape
covidtotals.sample(2, random_state=3).T
covidtotals.dtypes

#[3]
# taking summary statistics of the data and also looking at the different percentiles of the data
covidtotals.describe()
totvars = ['location','total_cases','total_deaths',
  'total_cases_pm','total_deaths_pm']
#for a few of the variables the mean is higher than the median hinting at a skew to the right
#high postive skew further illustrated by leap between 90th and 100th percentile
covidtotals[totvars].quantile(np.arange(0.0,1.1,0.1))

#[4]
#a view of the distribution of the total cases
plt.hist(covidtotals['total_cases'], bins=12)
plt.title('Total Covid Cases')
plt.xlabel('Cases')
plt.ylabel('Number of Countries')
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()
