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
#
nls97[1000:1004:2].T
nls97.head(3).T
nls97[:3].T

#[]
#
nls97.tail(3).T
nls97[-3:].T

#[]
#
nls97.loc[[195884,195891,195970]].T
nls97.loc[195884:195970].T #when using the : the slicing is automatically assumed to be by rows
