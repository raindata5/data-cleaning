import pandas as pd
import numpy as np
pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.2f}'.format


nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

#[1]
#inspecting specific portions of the data that are important to the analysis

nls97[['wageincome','highestgradecompleted','highestdegree']].head(3).T

nls97.loc[:, "weeksworked12":"weeksworked17"].head(3).T
nls97.loc[:, "colenroct09":"colenrfeb14"].head(3).T

#[2]
#the wageincome variable corresponds to wages during 2016
nls97.loc[(nls97.weeksworked16==0) & nls97.wageincome>0, ['weeksworked16','wageincome']] #there are some discrepancies here
nls97.filter(like="colenr").apply(lambda x: x.str[0:1]=='3').head(2).T #this and the following line of code allows us to see whether an individual was ever enrolled in a 4-year degree
nls97.filter(like="colenr").apply(lambda x: x.str[0:1]=='3').any(axis=1).head(2)

#[3]
#this allows us to check for anyone who was enrolled in a graduated program despite not having any indication of having taken a 4-year college course
bachskip = nls97.loc[(nls97.filter(like="colenr").apply(lambda x : x.str[:1]=='4').any(axis=1)) & ~(nls97.filter(like="colenr").apply(lambda x : x.str[:1]=='3').any(axis=1)),"colenrfeb97":"colenroct17"]
# we can see a couple of individuals  fit this criteria
bachskip.shape

#[4]
#
degrees = nls97.highestdegree.value_counts(sort=False).sort_index().index[-4:]
degrees = list(degrees)
for y,row in enumerate(degrees):
    degrees[y] = row[0:1]

#[5]
# checking those that reported their highest degree being 4 or higher which coressponds to bachelor's and higher and where yet there college enrollment status
#throughout the years indicates that they were never enrolled in a 4 year program
fouryeardegreeskip = nls97.loc[nls97.highestdegree.str[0:1].isin(degrees) & ~nls97.filter(like="colenr").apply(lambda x: x.str[0:1]=='3').any(axis=1), "colenrfeb97":"colenroct17"]
# a couple of individuals shows post-grad enrollment w/o bachelor's enrollment2
len(fouryeardegreeskip)
fouryeardegreeskip.head(3).T

#[6]
# we are going to show those individuals with high wages (defined by a wage 3 standard deviations above the mean)
highwages = nls97.loc[nls97.wageincome > nls97.wageincome.mean()+(nls97.wageincome.std()*3),['wageincome']]
highwages



#[7]
#this serves to show those that have a mean weeks worked composed of years 2012-2016 which is either lower than 5% of the weeks worked on record for 2017(last recorded year)
#or higher than 2 times the recorded weeks worked in 2017

workchanges = nls97.loc[~nls97.loc[:,"weeksworked12":"weeksworked16"].mean(axis=1).between(nls97.weeksworked17*0.5,nls97.weeksworked17*2)& ~nls97.weeksworked17.isnull(),
"weeksworked12":"weeksworked17"]
#there are many individuals which indicate sharp changes in weeks worked
len(workchanges)

workchanges.head(7).T


#[8]
#now we can see the highest grade completed with the corresponding degree
ltgrade12 = nls97.loc[nls97.highestgradecompleted<12, ['highestgradecompleted','highestdegree']]
#now we can see the abs. freq. amonsgt the grades completed and degrees
pd.crosstab(ltgrade12.highestgradecompleted, ltgrade12.highestdegree)
