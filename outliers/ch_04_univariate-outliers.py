#[1]
#reading in data and setting index as well as importing needed libraries
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

#[2]
#summary statistics with a focus just on the cumulative variables
covidtotalsonly = covidtotals.loc[:,totvars]
covidtotalsonly.describe()

#[3]
#looking to find out he distribution of the data
covidtotalsonly.quantile(np.arange(0.0,1.1,0.1))
covidtotalsonly.skew() # in a normal distribution the skew would be about 0 and the kurtosis 3
covidtotalsonly.kurtosis() #indicates the thickness of the tails

#[4]
#running this hypothesis test with the null that the distribution is normal and the alternative that it isn't
# will loop through each variable and place the associated statistic that is calculated and the p-value in a dictionary
def test_for_normality(variable,dataframe):
  stat, p = scistat.shapiro(dataframe[variable])
  return (stat,p)

norm_dict = {}
for row in totvars[1:]:
  norm_dict[row] = test_for_normality(row,covidtotals)

# test_for_normality("total_cases", covidtotalsonly)
# test_for_normality("total_deaths", covidtotalsonly)
# test_for_normality("total_cases_pm", covidtotalsonly)
# test_for_normality("total_deaths_pm", covidtotalsonly)
norm_dict
#[5]
#this plot visualizes the predicted values of a distribution if it were to be normal by the trendline
sm.qqplot(covidtotalsonly[['total_cases']].sort_values(['total_cases']),line='s')
plt.title("QQ Plot of Total Cases")

sm.qqplot(covidtotals[['total_cases_pm']].sort_values(['total_cases_pm']), line='s')
plt.title(r"QQ Plot of Total Cases Per Million")
plt.show()


#[6]
# we will classify the extreme values based 1.5 times iqr
#note: this criteria assumes that data distribution is relatively normal
thirdq, firstq = covidtotalsonly.total_cases.quantile(.75), covidtotalsonly.total_cases.quantile(.25)
quartilerange = 1.5 * (thirdq - firstq)
highoutlier, lowoutlier = quartilerange + thirdq, firstq - quartilerange
print(lowoutlier,highoutlier, sep=' <----> ')

#{7]
#going to separathe the extreme values and then export them to their own excel file

def get_outliers():
  dfout = pd.DataFrame(columns = covidtotals.columns, data=None) #initializes a dataframe with no values but all orig. columns from df
  for col in covidtotalsonly.columns[1:]: # just going to loop through the numeric columns
    thirdq, firstq = covidtotalsonly[col].quantile(0.75), covidtotalsonly[col].quantile(0.25)
    quartilerange = 1.5*(thirdq-firstq)
    highoutlier, lowoutlier = quartilerange + thirdq, firstq - quartilerange
    df = covidtotals.loc[(covidtotals[col] > highoutlier) | (covidtotals[col] < lowoutlier)] # for each columns we will isolate the extreme values
    df = df.assign(varname = col, threshlow= lowoutlier, threshhigh= highoutlier) # creates 3 new columns that corresponds to a label and the high outlier , and then the low outlier for that label respectively
    dfout = pd.concat([dfout,df]) # just a simple concatenation of the df's
  return dfout

outliers = get_outliers()
outliers.varname.value_counts() #shows the number of extreme values for each column
outliers.to_excel('views/extreme-value-cases.xlsx')
#[8]
#seeing what caracterizes those countries with an extreme level of total cases per million
outliers.loc[outliers.varname == 'total_cases_pm', ['location','total_cases_pm',
'pop_density','gdp_per_capita']].sort_values(['total_cases_pm'], ascending=True)
covidtotals[['pop_density','gdp_per_capita']].quantile([0.25,0.5,0.75]) #compare with the values from orig.dataset

#[9]
#checking out the distribution for total cases

plt.hist(covidtotalsonly['total_cases'], bins=7)
plt.title("Total Covid Cases ")
plt.ticklabel_format(useOffset=False,style='plain')
plt.xlabel('Cases')
plt.ylabel("Number of Countries")
plt.show()
# plt.hist(covidtotalsonly['total_cases']/1000, bins=7)
# plt.title("Total Covid Cases (thousands)")
# plt.xlabel('Cases')
# plt.ylabel("Number of Countries")
# plt.show()

#[10]
#since the distribution for total_cases is skewed i'm going to transform these and take the natural log of the value
covid_log =covidtotalsonly.copy()

for col in covidtotalsonly.columns[1:]:
  covid_log[col] = np.log1p(covid_log[col])

plt.hist(covid_log['total_cases'])
plt.title("Total Covid Cases (ln scale)")
plt.xlabel('Cases')
plt.ylabel("Number of Countries")
plt.show()
#shows how log transformations help
covid_log.skew()
covid_log.kurtosis()
