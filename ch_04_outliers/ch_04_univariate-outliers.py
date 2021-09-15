import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqline
import scipy.stats as scistat

pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)


totvars = ['location','total_cases','total_deaths','total_cases_pm',
  'total_deaths_pm']
demovars = ['population','pop_density','median_age','gdp_per_capita',
  'hosp_beds']

#[]
#

covidtotalsonly = covidtotals.loc[:,totvars]

covidtotalsonly.describe()

#[]
#
covidtotalsonly.quantile(np.arange(0.0,1.1,0.1))
covidtotalsonly.skew()
covidtotalsonly.kurtosis()

#[]
