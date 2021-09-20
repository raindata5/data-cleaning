import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 85)
pd.options.display.float_format = '{:,.0f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

#[1]
#will separate the col's required for analysis and get descriptive statistics on them
regresson= ['pop_density','median_age','gdp_per_capita']

covidanalysis = covidtotals.loc[:,['total_cases_pm'] + regresson].dropna() #will drop any rows that have null values
covidanalysis.describe()

#[2]
#

def getlm(df):
    Y = df.total_cases_pm
    X = df[['pop_density','median_age','gdp_per_capita']]
    X = sm.add_constant(X)
    return sm.OLS(Y, X).fit()


lm = getlm(covidanalysis)
lm.summary()

#[]
#
influence = lm.get_influence().summary_frame()
influence.loc[influence.cooks_d > 0.5,['cooks_d']]
influence.loc[influence.cooks_d > 0.5]

#[]
#
fig, ax = plt.subplots(figsize=(10,6))
sm.graphics.influence_plot(lm,ax=ax,criterion='cooks')
plt.show()

#[]
#
ca_minus_outliers = covidanalysis.loc[influence.cooks_d < 0.5]

lm2 = getlm(ca_minus_outliers)
lm2.summary()

