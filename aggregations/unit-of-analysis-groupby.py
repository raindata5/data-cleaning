#[1]
#
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 50)
pd.options.display.float_format = '{:,.2f}'.format

coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])
ltbrazil = pd.read_csv("data/ltbrazil.csv")

#[2]
# between a certain range of dates, we get the sum of new_cases and deaths on each day while also defining as_index=False

coviddailytotals = coviddaily.loc[coviddaily.casedate.between('2020-02-01','2020-07-12')].groupby(['casedate'], as_index=False)[['new_cases','new_deaths']].sum()

coviddailytotals.head(10)

#[3]
# dropping rows with no temperature

ltbrazil = ltbrazil.dropna(subset=['temperature'])
ltbrazil.iloc[0:10,0:11]

#[4]
# getting the mean temp for each station along with other agg methods while also defining as_index=False

ltbrazil_avg = ltbrazil.groupby(['station'], as_index=False).agg({'latabs':'first','elevation':'first','temperature':'mean'})
ltbrazil_avg.head()
