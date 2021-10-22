#[1]
#
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
import pandas as pd
import os
import sys
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index('personid', inplace=True)

#[2]
# modifying my cwd to access the folder with the helper functions
sys.path.append(os.getcwd() + "/helperfunctions")
import basicdescriptives as bd

#[3]
# statistics on different columns
bd.get_tots(nls97[['satverbal','satmath']]).T
bd.get_tots(nls97.filter(like="weeksworked"))

#[4]
# information on null values in df

missings_on_cols, missing_on_rows = bd.get_missings(nls97[['weeksworked16','weeksworked17']], True)

#[5]
# transforming object columns to category to carry out function and create file of
# freq. of different categories in data
nls97.loc[:, nls97.dtypes == 'object'] = nls97.select_dtypes(['object']).apply(lambda x: x.astype('category'))

bd.make_freqs(nls97, "views/nlsfreqs.txt")

#[6]
# getting information on different categories in the data
bd.get_cnts(nls97, ['maritalstatus','gender','colenroct00'])

bd.get_cnts(nls97, ['maritalstatus','gender','colenroct00'], "colenroct00.str[0:1]=='1'")




















