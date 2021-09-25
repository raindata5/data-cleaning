import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# getting statistics on each different degree type
def viewtots(x):
    stat_dict = {}
    stat_dict['min'] = x.min()
    stat_dict['qr1'] = x.quantile(.25)
    stat_dict['med'] = x.median()
    stat_dict['qr3'] = x.quantile(0.75)
    stat_dict['max'] = x.max()
    stat_dict['count']= x.count,x.shape
    return pd.Series(stat_dict) #placing the dictionary in a df

#using group by and apply to get stats on different degrees
nls97.groupby(['highestdegree'])['weeksworked17'].apply(viewtots).unstack()

#[3]
# getting the distributions on weeks worked by degree attained or lack thereof
myplt = sns.boxplot('highestdegree','weeksworked17', data=nls97,
  order=sorted(nls97.highestdegree.dropna().unique()))
myplt.set_title("Boxplots of Weeks Worked by Highest Degree")
myplt.set_xlabel('Highest Degree Attained')
myplt.set_ylabel('Weeks Worked 2017')
myplt.set_xticklabels(myplt.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.tight_layout()
plt.show()

#[4]
# getting statistics on each distinct regions
covidtotals.groupby(['region'])['total_cases_pm'].apply(viewtots).unstack()

#[5]
# plotting the cases per million by each region
sns.boxplot('total_cases_pm', 'region', data=covidtotals)
sns.swarmplot(y="region", x="total_cases_pm", data=covidtotals, size=2, color=".3", linewidth=0)
plt.title("Boxplots of Total Cases Per Million by Region")
plt.xlabel("Cases Per Million")
plt.ylabel("Region")
plt.tight_layout()
plt.show()


#[6]
#inspecting the most extreme cases
covidtotals.loc[covidtotals.total_cases_pm>=14000,['location','total_cases_pm']]

#[7]
# replotting the cases per million by each region but without the high extreme values
sns.boxplot('total_cases_pm', 'region', data=covidtotals.loc[covidtotals.total_cases_pm<14000])
sns.swarmplot(y="region", x="total_cases_pm", data=covidtotals.loc[covidtotals.total_cases_pm<14000], size=3, color=".3", linewidth=0)
plt.title("Total Cases Without Extreme Values")
plt.xlabel("Cases Per Million")
plt.ylabel("Region")
plt.tight_layout()
plt.show()
