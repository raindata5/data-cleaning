import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

#[1]
#reading in the data and setting the index
landtemps = pd.read_csv("data/landtemps2019avgs.csv")
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])
covidtotals.set_index("iso_code", inplace=True)

#[2]
# taking a sample of the data with the particular columns that are of interest
landtemps[['station','country','latabs','elevation','avgtemp']].sample(10, random_state=1)


#[3]
# taking descriptive statistics to get an idea of the distribution
landtemps.describe()
landtemps.avgtemp.skew()
landtemps.avgtemp.kurtosis()

#[4]
# plotting the histogram to visualize the distribution

plt.hist(landtemps.avgtemp)
plt.axvline(landtemps.avgtemp.mean(), color='yellow', linestyle='dashed', linewidth=2 )
plt.title("Histogram of Average Temperatures (Celsius)")
plt.xlabel("Average Temperature")
plt.ylabel("Frequency")
plt.show()

#[5]
#visualizing the distribution again but with a qqplot

sm.qqplot(landtemps[['avgtemp']].sort_values(['avgtemp']), line='s')
plt.title("QQ Plot of Average Temperatures")
plt.show()

#[6]
#will do a similar analysis on the covid dataset
#making a list for the regions that are covered in our data

showregions = ['Oceania / Aus','East Asia','Southern Africa',
  'Western Europe']

def getcases(regions):
    return covidtotals.loc[covidtotals.region==regions,'total_cases_pm']

#[7]
#plotting a stacked histogram to see the distributions by region
plt.hist([getcases(r) for r in showregions], color=['blue','mediumslateblue','plum','mediumvioletred'], label=showregions, stacked=True)
plt.title("Stacked Histogram of Cases Per Million for Selected Regions")
plt.xlabel("Cases Per Million")
plt.ylabel("Frequency")
plt.xticks(np.arange(0, 22500, step=2500))
plt.legend()
plt.show()


#[8]
#plotting the distribution of each region

fig, axes = plt.subplots(2,2)
fig.suptitle("Histograms of Covid Cases Per Million by Selected Regions")
axes = axes.ravel()

for j,ax in enumerate(axes):
    ax.hist(covidtotals.loc[covidtotals.region==showregions[j]].total_cases_pm, bins = 5)
    ax.set_title(showregions[j], fontsize=10)
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

plt.tight_layout()
fig.subplots_adjust(top=.88)
plt.show()
