#[1]
#
import pandas as pd
import os
import sys
nls97 = pd.read_csv("data/nls97f.csv")
nls97.set_index('personid', inplace=True)

#[2]
# modifying my cwd to access the folder with the helper functions
sys.path.append(os.getcwd() + "/helper-functions")
import basicdescriptives as bd

#[3]
# to use this code the module must be imported in with an alias
# import importlib
# importlib.reload(bd)



#[4]
# basic information on the data set
dfinfo = bd.get_first_look(nls97)
bd.display_dict(dfinfo)

#[5]
# basic information on the data set with originalid presumed to be the key
dfinfo = bd.get_first_look(nls97,3,'originalid')
bd.display_dict(dfinfo)

#[6]
# specifying different parts of the dictionary
dfinfo['nrows']
dfinfo['dtypes']
dfinfo['nrows'] == dfinfo['uniqueids']
