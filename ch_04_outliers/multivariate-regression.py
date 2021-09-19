import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 85)
pd.options.display.float_format = '{:,.0f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

#[]
#
regresson= ['pop_density','median_age','gdp_per_capita']

covidanalysis = covidtotals.loc[:,['total_cases_pm'] + regresson].dropna()
covidanalysis.describe()
