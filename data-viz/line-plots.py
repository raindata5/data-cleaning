import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

#[1]
# reading in data and setting respective indexes

pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])

#[2]
# inspecting the data which is panel data
coviddaily.info()
coviddaily.head()
coviddaily.sample(2,random_state=2).T

#[3]
# group by to create aggregates based on each day and summing up the totals in each group

coviddailytotals = coviddaily.loc[coviddaily.casedate.between('2020-02-01','2020-07-12')].groupby(['casedate'])[['new_cases','new_deaths']].sum().reset_index()
coviddailytotals.sample(8,random_state=1)

#[4]
# plotting both deaths and cases each on separate plot
#

fig = plt.figure()
plt.suptitle("New Covid Cases and Deaths By Day Worldwide in 2020")
ax1 = plt.subplot(2,1,1)
ax1.plot(coviddailytotals.casedate, coviddailytotals.new_cases)
ax1.xaxis.set_major_formatter(DateFormatter("%b")) #makes the xaxis contain the month names of each label
ax1.set_xlabel("New Cases")

ax2= plt.subplot(2,1,2)
ax2.plot(coviddailytotals.casedate,coviddailytotals.new_deaths)
ax2.xaxis.set_major_formatter(DateFormatter("%b"))
ax2.set_xlabel("New Deaths")
plt.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()

#[5]
# group by to create aggregates based on each day-region and summing up the totals in each group

regiontotals = coviddaily.loc[coviddaily.casedate.between('2020-02-01','2020-07-12')].groupby(['casedate','region'])[['new_cases','new_deaths']].sum().reset_index()

regiontotals.sample(8,random_state=1)

#[6]
# plotting news cases by specific regions on the same plot
regiontotals.region.unique() # distinct regions

showregions = ['East Asia','Southern Africa','North America',
  'Western Europe']

for r in range(len(showregions)):
    df = regiontotals.loc[regiontotals.region==showregions[r]]
    plt.plot(df.casedate, df.new_cases,label=showregions[r])

plt.title("New Covid Cases By Day and Region in 2020")
plt.gca().get_xaxis().set_major_formatter(DateFormatter("%b")) #check
plt.ylabel("New Cases")
plt.legend()
plt.show()

#[7]
# going to inspect the region southern africa

af = regiontotals.loc[regiontotals.region=='Southern Africa', #getting all the cases for southern africa
  ['casedate','new_cases']].rename(columns={'new_cases':'afcases'}) #to prevent confusion when joining the two columns later this will be renamed here

sa = coviddaily.loc[coviddaily.location=='South Africa', #getting all the cases for south africa
  ['casedate','new_cases']].rename(columns={'new_cases':'sacases'}) #column will be renamed here as well

af = pd.merge(af, sa, left_on=['casedate'], right_on=['casedate'], how="left") #doing left join on the 2 df's

#af.sacases.fillna(0, inplace=True) if there were any nulls present

#[8]
# looking at how data on cases for souther africa and south africa stack up
af['afcases_nosa'] = af.afcases-af.sacases #getting the difference between south africa and all the cases in southern africa
af_apr_rise = af.loc[af.casedate.between('2020-04-01','2020-07-12')] # targeting certain section of the data where the new_cases begins to rise

fig = plt.figure()
ax = plt.subplot()
ax.stackplot(af_apr_rise.casedate, af_apr_rise.sacases, af_apr_rise.afcases_nosa,labels= ['South Africa','Other in Southern Africa']) #looking at data stacked directly on top of each other
ax.xaxis.set_major_formatter(DateFormatter('%m-%d'))
plt.title("New Covid Cases in Southern Africa")
plt.tight_layout()
plt.legend(loc="upper left")
plt.show()
