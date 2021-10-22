
#[1]
#
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
covidcases = pd.read_csv("data/covidcases720.csv")

#[2]
# list for the desired columns
cotidiano_vars = ['casedate','new_cases','new_deaths']
agg_vars = ['location','total_cases','total_deaths']

demo_vars = ['population','population_density','median_age',
  'gdp_per_capita','hospital_beds_per_thousand','region']

covidcases[cotidiano_vars + agg_vars + demo_vars].head(5).T

#[3]
# covid cases for each day
daily_covid = covidcases[['location']+cotidiano_vars]
daily_covid.shape
daily_covid.head()

#[4]
# sorting by locations and date to keep the most updated data entry for each country

daily_covid.location.nunique()

covid_reduce = daily_covid.sort_values(['location','casedate']).drop_duplicates(['location'] ,keep='last').rename(columns={'casedate':'final_date'})

covid_reduce.shape
covid_reduce.head().T

#[5]
# getting aggregate values (and the last value depending on the column) for each country and then renaming some of the columns which now hold new informations

total_covid = covidcases.groupby(['location'],as_index=False).agg({'new_cases':'sum','new_deaths':'sum','median_age':'last',\
    'gdp_per_capita':'last','region':'last','casedate':'last',\
    'population':'last'}).\
    rename(columns={'new_cases':'total_cases',\
    'new_deaths':'total_deaths','casedate':'lastdate'})

total_covid.head(3).T
