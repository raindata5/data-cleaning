import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

#[1]
#reading in data and setting indexes
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])
covidtotals.set_index("iso_code", inplace=True)

#[2]
#checking summary statistics and also plotting a boxplot to get an idea of the distribution
nls97.satverbal.describe()
nls97.info()

plt.boxplot(nls97.satverbal.dropna(),labels = ['SAT verbal'])

plt.annotate('outlier threshold',xy=(1.05,780),xytext=(1.15,780),size=7,arrowprops=dict(facecolor='black',headwidth=2, width=0.5, shrink=0.02))

plt.annotate('3rd quartile', xy=(1.08,570), xytext=(1.15,570), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.annotate('median', xy=(1.08,500), xytext=(1.15,500), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.annotate('1st quartile', xy=(1.08,430), xytext=(1.15,430), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.annotate('outlier threshold', xy=(1.05,220), xytext=(1.15,220), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.title("Boxplot of SAT Verbal Score")
plt.show()


#[3]
# summary stats on 2 consecutive years to see if there is anything odd

weeksworked = nls97.loc[:, ['highestdegree','weeksworked16','weeksworked17']]
weeksworked.describe()

#[4]
#looking at distribution of both years for weeks worked

plt.boxplot([weeksworked.weeksworked16.dropna(), weeksworked.weeksworked17.dropna()],labels=['Weeks Worked 2016','Weeks Worked 2017'])
plt.title("Boxplots of Weeks Worked")
plt.tight_layout()
plt.show()



#[5]
# gathering the aggregation variables

totvars = ['total_cases','total_deaths','total_cases_pm','total_deaths_pm']
totvarslabels = ['cases','deaths','cases per million','deaths per million']
covidtotalsonly = covidtotals[totvars]
covidtotalsonly.describe()


#[6]
#plotting distributions for deaths pm and cases pm but these are on different scales so
#they will be placed on their own plots
fig, ax = plt.subplots()
plt.title("Boxplots of Covid Cases and Deaths Per Million")
ax.boxplot([covidtotalsonly.total_cases_pm, covidtotalsonly.total_deaths_pm],labels=['cases per million','deaths per million'])
plt.tight_layout()
plt.show()

#[7]
#checking the distributions of each variable on it' s own plot

fig, axes = plt.subplots(2,2)
fig.suptitle("Boxplots of Covid Cases and Deaths")
axes = axes.ravel() #allows us to iterate through the axes project

for i,ax in enumerate(axes) :
    ax.boxplot(covidtotals[totvars[i]], labels=[totvarslabels[i]])



plt.tight_layout()
plt.show()

