#[1]
#
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
coviddaily = pd.read_csv("data/coviddaily720.csv", parse_dates=["casedate"])

#[1]
# initializing groupby object
countrytots = coviddaily.groupby(['location']) #can use dropna=False is necessary
type(countrytots)

#[2]
# finding the first and last value in each group
countrytots.first().iloc[0:5, 0:5]
countrytots.last().iloc[0:5, 0:5]
type(countrytots.last())

#[3]
# using get_group to find the data for a particular group
countrytots.get_group('Zimbabwe').iloc[0:5, 0:5]

#[4]
# iterating through the groupby object to show it throws out a name and the data of the group
for name, group in countrytots:
    if (name in ['Malta', 'Kuwait']):
        print(name, '\n', group.iloc[0:5, 0:5], )

#[5]
# aggreation functions
countrytots.size()
countrytots.count()

#[6]
# checking stats across the groups
countrytots.new_cases.describe().head()

countrytots.new_cases.sum().head()
