import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

#[1]
# reading in data and setting respective indexes
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])
covidtotals.set_index("iso_code", inplace=True)


#[]
#

sns.violinplot( y = nls97.satverbal, color='wheat',orient='v') #resolving back to horizontal plot ,so must specify y
plt.title("Violin Plot of SAT Verbal Score")
plt.ylabel("SAT Verbal")
plt.text(0.08, 780, 'outlier threshold', horizontalalignment='center', size='x-small')
plt.text(0.065, nls97.satverbal.quantile(0.75), '3rd quartile', horizontalalignment='center', size='x-small')
plt.text(0.05, nls97.satverbal.median(), 'Median', horizontalalignment='center', size='x-small')
plt.text(0.065, nls97.satverbal.quantile(0.25), '1st quartile', horizontalalignment='center', size='x-small')
plt.text(0.08, 210, 'outlier threshold', horizontalalignment='center', size='x-small')
plt.text(-0.4, 500, 'frequency', horizontalalignment='center', size='x-small')
plt.show()


#[]
#
nls97.loc[:,['weeksworked16','weeksworked17']].describe()

#[]
#

myplt = sns.violinplot(data=nls97.loc[:, ['weeksworked16','weeksworked17']])
myplt.set_title("Violin Plots of Weeks Worked")
myplt.set_xticklabels(["Weeks Worked 2016","Weeks Worked 2017"])
plt.show()

#[]
#
# while these category labels are of great importance to help create the plot we will reduce them
nls97["maritalstatusreduce"] = nls97.maritalstatus.replace(['Married','Never-married','Divorced','Separated','Widowed'],['Married','Never Married','Not Married','Not Married','Not Married'])
sns.violinplot(nls97.gender, nls97.wageincome, hue=nls97.maritalstatusreduce,scale='count') #double-check the scale
plt.title("Violin Plots of Wage Income by Gender and Marital Status")
plt.xlabel('Gender')
plt.ylabel('Wage Income 2017')
plt.legend(title="", loc="upper center", framealpha=0, fontsize=8)
plt.tight_layout()
plt.show()

#[]
#
# nls97 = nls97.sort_values('highestdegree')
# alternative to getting categories to be sorted on plot
myplt = sns.violinplot(nls97.highestdegree, nls97.weeksworked17, data=nls97, order=sorted(nls97.highestdegree.dropna().unique()))
myplt.set_xticklabels(myplt.get_xticklabels(), rotation=45, horizontalalignment= 'right')
myplt.set_title("Violin Plots of Weeks Worked by Highest Degree")
myplt.set_xlabel('Highest Degree Attained')
myplt.set_ylabel('Weeks Worked 2017')
plt.tight_layout()
plt.show()


#[]
#
