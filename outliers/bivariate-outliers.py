import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

#[2]
totvars = ['location','total_cases','total_deaths','total_cases_pm',
  'total_deaths_pm']
demovars = ['population','pop_density','median_age','gdp_per_capita',
  'hosp_beds']

#[3]
#checking out the correlation of the variables in the data
covidtotals.corr(method="pearson") #pearson is also default argument

covidtotalsonly = covidtotals.loc[:, totvars]

#[4]
#using the qcut cmd to create categorical bins for the total_cases, and total_deaths columns
covidtotalsonly['total_cases_q'] = pd.qcut(covidtotalsonly['total_cases'],labels = ['very low','low','medium',
  'high','very high'], q=5, precision=0)

covidtotalsonly['total_deaths_q'] = pd.qcut(covidtotalsonly['total_deaths'],labels=['very low','low','medium',
    'high','very high'], q=5, precision=0)
#now can we see the frequencies of the pairs of the previous categorical columns
pd.crosstab(covidtotalsonly.total_cases_q,
  covidtotalsonly.total_deaths_q)

#[5]
# checkig out the countries that seem to break from the expected values
covidtotals.loc[(covidtotalsonly.total_cases_q=="very high") & (covidtotalsonly.total_deaths_q=="medium")].T
covidtotals.loc[(covidtotalsonly.total_cases_q=="low") & (covidtotalsonly.total_deaths_q=="high")].T

#[6]
#plotting a linear regression model to see the association between total_cases and total_deaths
# also included a 95% confidence interval for the regression line (i.e. how confident we can be that the reg. line of general pattern in the populations...
# which is represented in the data will be found in this shading based on the SE of the predicted values)
ax = sns.regplot(x="total_cases", y="total_deaths", data=covidtotals)
ax.set(xlabel="Cases", ylabel="Deaths", title="Total Covid Cases and Deaths by Country")
plt.show()

#[7]
#inspecting the values that are far away from the regression line
covidtotals.loc[(covidtotals.total_cases<300000) & (covidtotals.total_deaths>20000)].T
covidtotals.loc[(covidtotals.total_cases>300000) & (covidtotals.total_deaths<10000)].T

#[8]
#repeating the process for the per million columns
ax = sns.regplot(x="total_cases_pm", y="total_deaths_pm", data=covidtotals)
ax.set(xlabel="Cases Per Million", ylabel="Deaths Per Million", title="Total Covid Cases per Million and Deaths per Million by Country")
plt.show()

covidtotals.loc[(covidtotals.total_cases_pm<7500) & (covidtotals.total_deaths_pm>250),['location','total_cases_pm','total_deaths_pm']]

covidtotals.loc[(covidtotals.total_cases_pm>5000) & (covidtotals.total_deaths_pm<=50),['location','total_cases_pm','total_deaths_pm']]
