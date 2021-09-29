import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 35)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

#[1]
# experimetning with sample statistics on the gpaoverall series

gpaoverall = nls97.gpaoverall
gpaoverall.mean()
gpaoverall.describe()
gpaoverall.quantile(np.arange(0.1,1.1,0.1))


#[2]
# checking out a specific subset of the data
gpaoverall.loc[gpaoverall.between(3,3.5)].head(5)
gpaoverall.loc[gpaoverall.between(3,3.5)].sum()


#[3]
# doing 3 aggregate functions over a series

gpaoverall.loc[(gpaoverall<2) | (gpaoverall>4)].sample(5, random_state=2)
gpaoverall.loc[gpaoverall>gpaoverall.quantile(0.99)].agg(['count','min','max']) # agg over the whole series

#[4]
# testing for particular conditions across the data
(gpaoverall>4).any() #checking to see if at least 1 fits this criteria
(gpaoverall>=0).all() #repeating but for all
(gpaoverall>=0).sum()
(gpaoverall==0).sum()
gpaoverall.isnull().sum()


nls97.loc[nls97.wageincome > nls97.wageincome.quantile(0.75),'gpaoverall'].mean()
nls97.loc[nls97.wageincome < nls97.wageincome.quantile(0.25),'gpaoverall'].mean()

#[5]
# summary statistics across categorical data
nls97.maritalstatus.describe()
nls97.maritalstatus.value_counts()
