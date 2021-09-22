import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 85)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

#[1]
#will separate the col's required for analysis and get descriptive statistics on them
regresson= ['pop_density','median_age','gdp_per_capita']

covidanalysis = covidtotals.loc[:,['total_cases_pm'] + regresson].dropna() #will drop any rows that have null values since our model will work better without them
covidanalysis.describe()

#[2]
# creating a linear regression model using OLS

def getlm(df):
    Y = df.total_cases_pm
    X = df[['pop_density','median_age','gdp_per_capita']]
    X = sm.add_constant(X)
    return sm.OLS(Y, X).fit()


lm = getlm(covidanalysis)
lm.summary()
#model uses the simple SE formula when we probably should use the robust SE formula
#also we could conclude that population density doesn't have a high impact on total_cases_pm based on the t stat and even the p-value
#[3]
#checking to see which observations seem to have a larger than ordinary effect on the LRM
# obs. with a cook's d value higher than .5 should be inspected
influence = lm.get_influence().summary_frame()
influence.loc[influence.cooks_d > 0.5,['cooks_d']]
influence.loc[influence.cooks_d > 0.5]

#[4]
#showing an influence plot
fig, ax = plt.subplots(figsize=(10,6))
sm.graphics.influence_plot(lm,ax=ax,criterion='cooks')
plt.show()

#[5]
# using the summary frame we got from the lm to index our original datframe and get rid of those obs. with signficant influence
ca_minus_outliers = covidanalysis.loc[influence.cooks_d < 0.5]

lm2 = getlm(ca_minus_outliers)
lm2.summary()
# the r-squared does go down and also in addition to the pop. density  it could also be concluded that the median age coefficient is zero
# this makes sense since qatar had a low medium age with a bunch of cases so the model was trying to account for that
