#[1]
#reading in data and setting index as well as importing needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.0f}'.format


covidtotals = pd.read_csv("data/covidtotalswithmissings.csv")
covidtotals.set_index("iso_code", inplace=True)

#[]
# cumulative columns and demographic columns
totvars = ['location','total_cases','total_deaths','total_cases_pm',
  'total_deaths_pm']
demovars = ['population','pop_density','median_age','gdp_per_capita',
  'hosp_beds']

#[]
# checking the absolute frequencies of missing values by column and also on a row bases for the demographic variables

covidtotals[demovars].isnull().sum(axis=0)

missdemovar = covidtotals[demovars].isnull().sum(axis=1)

missdemovar.value_counts()

covidtotals.loc[missdemovar>=3, ['location'] + demovars].head(10).T

#[]
#checking the absolute frequencies of missing values by column and also on a row bases for the cumulative variables

covidtotals[totvars].isnull().sum(axis=0)
covidtotals[totvars].isnull().sum(axis=1)
misstotvar = covidtotals[totvars].isnull().sum(axis=1)
misstotvar.value_counts()
covidtotals.loc[misstotvar>0].T

#[]
#due to the nature of the missing values these will be computed (putting in 0 would be correct but doing the following transformation keeps in line with the logic of the metric
covidtotals['total_deaths_pm'].fillna(covidtotals.total_deaths/(covidtotals.population/1000000), inplace=True)
covidtotals['total_cases_pm'].fillna(covidtotals.total_cases/(covidtotals.population/1000000),inplace=True)
covidtotals[totvars].isnull().sum(axis = 0)
