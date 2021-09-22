import pandas as pd
import numpy as np

pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format

nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

#[]
#
nls97[1000:1004].T

#[]
#the 2 allows us to increment by 2s
nls97[1000:1004:2].T
nls97.head(3).T
nls97[:3].T

#[]
# these 2 lines of code return the same results
nls97.tail(3).T
nls97[-3:].T

#[]
#using both loc and iloc for retrieving data based on index labels and row positions
nls97.loc[[195884,195891,195970]].T
nls97.loc[195884:195970].T #when using the : the slicing is automatically assumed to be by rows
nls97.iloc[[0]].T
nls97.iloc[[0,1,2]].T
nls97.iloc[0:3].T
nls97.iloc[[-3,-2,-1]].T
nls97.iloc[-3:].T

#[]
#taking a closer look at those that sleep 4 hours or less which makes up 5 percent of the respondents to that question
nls97.nightlyhrssleep.quantile(.05)
nls97.nightlyhrssleep.count()
lowsleepbool = nls97.nightlyhrssleep <= 4
lowsleep = nls97[lowsleepbool]
lowsleep.shape

#[]
lowsleep.childathome.describe()
# about 75% of those getting low sleep have 3 children at home or less  but about 25% have more than 3
lowsleep3pluschildren = nls97.loc[(nls97.nightlyhrssleep <= 4) & (nls97.childathome >= 3),['nightlyhrssleep','childathome']]
lowsleep3pluschildren
