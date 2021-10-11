#[1]
#
import pandas as pd
import numpy as np

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

#[2]
# defining our own function to get the iqr and to be used in the agg function on a groupby object
def iqr(x):
    return x.quantile(0.75) - x.quantile(0.25)

aggdict = {'weeksworked06':['count','mean',iqr], 'childathome': ['count','mean',iqr]}

nls97.groupby(['highestdegree']).agg(aggdict) # iqr by highest degree

#[3]
# defining our own function to be used on each group paired with apply
# with apply in each group a column/series is sent one by one to the function
def get_tots(x) :
    out = {}
    out['qrl'] = x.quantile(0.25)
    out['med'] = x.median()
    out['qr3'] = x.quantile(0.75)
    out['count'] = x.count()
    return pd.Series(out)

nls97.groupby(['highestdegree'])['weeksworked06'].apply(get_tots)

#[4]
# One method of getting a group value associated with each row (in the case of visualization for example)
nls97.groupby(['highestdegree'])['weeksworked06'].apply(get_tots).reset_index()

#[5]
# method for getting the aggregations positioned as columns (creates columns from 2nd-level index)
data = nls97.groupby(['highestdegree'])['weeksworked06'].apply(get_tots).unstack()

data.info()
