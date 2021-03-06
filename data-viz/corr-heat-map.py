import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#[1]
#
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])

#[2]
# getting a correlation matrix to see which variables are most correlated
corr = covidtotals.corr()
corr[['total_cases','total_deaths','total_cases_pm','total_deaths_pm']]

#[3]
# scatter plots with regression line

fig, axes = plt.subplots(1,2,sharey=True)
sns.regplot(x=covidtotals.median_age, y=covidtotals.total_cases_pm, ax=axes[0])
sns.regplot(x=covidtotals.gdp_per_capita, y=covidtotals.total_cases_pm, ax= axes[1])
axes[0].set_xlabel("Median Age")
axes[0].set_ylabel("Cases Per Million")
axes[1].set_xlabel("GDP Per Capita")
# axes[1].set_xticklabels(axes[1].get_xticklabels(),rotation=45) not sure why doesn't work
axes[1].set_ylabel("")
plt.suptitle("Scatter Plots of Age and GDP with Cases Per Million")
plt.tight_layout()
fig.subplots_adjust(top=0.92)
plt.show()

#[4]
# creating a correlation heat map
sns.heatmap(corr,xticklabels=corr.columns, yticklabels=corr.columns, cmap='coolwarm')
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()
