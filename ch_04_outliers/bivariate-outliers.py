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

#[]
#
covidtotals.corr(method="pearson") #pearson is also default argument

covidtotalsonly = covidtotals.loc[:, totvars]

#[]
#
covidtotalsonly['total_cases_q'] = pd.qcut(covidtotalsonly['total_cases'],labels = ['very low','low','medium',
  'high','very high'], q=5, precision=0)

covidtotalsonly['total_deaths_q'] = pd.qcut(covidtotalsonly['total_deaths'],labels=['very low','low','medium',
    'high','very high'], q=5, precision=0)

pd.crosstab(covidtotalsonly.total_cases_q,
  covidtotalsonly.total_deaths_q)

#[]
#
covidtotals.loc[(covidtotalsonly.total_cases_q=="very high") & (covidtotalsonly.total_deaths_q=="medium")].T
covidtotals.loc[(covidtotalsonly.total_cases_q=="low") & (covidtotalsonly.total_deaths_q=="high")].T


ax = sns.regplot(x="total_cases_pm", y="total_deaths_pm", data=covidtotals)
ax.set(xlabel="Cases Per Million", ylabel="Deaths Per Million", title="Total Covid Cases per Million and Deaths per Million by Country")
plt.show()

covidtotals.loc[(covidtotals.total_cases<300000) & (covidtotals.total_deaths>20000)].T


covidtotals.loc[(covidtotals.total_cases>300000) & (covidtotals.total_deaths<10000)].T
