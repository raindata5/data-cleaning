import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#[]
#
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])

#[]
#
corr = covidtotals.corr()
corr[['total_cases','total_deaths','total_cases_pm','total_deaths_pm']]

