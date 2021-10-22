#[1]
#

import pandas as pd
import os
import sys
import pprint

#[2]
#
sys.path.append(os.getcwd() + "/helper-functions")
import respondentclass as rpc
import importlib
importlib.reload(rpc)

#[3]
# reading in data and converting to a list of dictionaries
nls97 = pd.read_csv("data/nls97f.csv")
nls97list = nls97.to_dict('records')
nls97.shape
len(nls97list)
pprint.pprint(nls97list[0:1])

#[4]
# iterates through each observation and instantiates the respondent
# class and also called it's methods into a dictionary
analysislist = []
for respdict in nls97list:
  resp = rpc.Respondent(respdict)
  newdict = dict(originalid=respdict['originalid'],
    childnum=resp.child_num(),
    avgweeksworked=resp.avgweeksworked(),
    age=resp.ageby('20201015'),
    baenrollment=resp.baenrollment())
  analysislist.append(newdict)


#[5]
# placing the date in a df
len(analysislist)
resp.respondentcnt
pprint.pprint(analysislist[0:2])
analysis = pd.DataFrame(analysislist)
analysis.head(2)
