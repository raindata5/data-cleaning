import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format


landtemps = pd.read_csv("data/landtemps2019avgs.csv")
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])
covidtotals.set_index("iso_code", inplace=True)

#[]
#
landtemps[['station','country','latabs','elevation','avgtemp']].sample(10, random_state=1)


#[]
#
landtemps.describe()
landtemps.avgtemp.skew()
landtemps.avgtemp.kurtosis()

#[]
#

plt.hist(landtemps.avgtemp)
plt.axvline(landtemps.avgtemp.mean(), color='yellow', linestyle='dashed', linewidth=2 )
plt.title("Histogram of Average Temperatures (Celsius)")
plt.xlabel("Average Temperature")
plt.ylabel("Frequency")
plt.show()

#[]
#

sm.qqplot(landtemps[['avgtemp']].sort_values(['avgtemp']), line='s')
plt.title("QQ Plot of Average Temperatures")
plt.show()

#[]
#will do a similar analysis on the covid dataset

showregions = ['Oceania / Aus','East Asia','Southern Africa',
  'Western Europe']

def getcases(regions):
    return covidtotals.loc[covidtotals.region==regions,'total_cases_pm']

#[]
#
plt.hist([getcases(r) for r in showregions], color=['blue','mediumslateblue','plum','mediumvioletred'], label=showregions, stacked=True)
plt.title("Stacked Histogram of Cases Per Million for Selected Regions")
plt.xlabel("Cases Per Million")
plt.ylabel("Frequency")
plt.xticks(np.arange(0, 22500, step=2500))
plt.legend()
plt.show()


#[]
#complete check

fig, axes = plt.subplots(2,2)
fig.suptitle("Histograms of Covid Cases Per Million by Selected Regions")
axes = axes.ravel() #check

for j,ax in enumerate(axes):
    ax.hist(covidtotals.loc[covidtotals.region==showregions[j]].total_cases_pm, bins = 5)
    ax.set_title(showregions[j], fontsize=10)
    for tick in ax.get_xticklabels(): #check
        tick.set_rotation(45)

plt.tight_layout()
fig.subplots_adjust(top=.88)
plt.show()
