#[1]
#
import pandas as pd
import json
import os
import sys
import pprint
import requests
#import importlib
#importlib.reload(ci)

#[2]
#
sys.path.append(os.getcwd() + "/helper-functions")
import collectionitem as ci

#[3]
# using get request on the api
response = requests.get("https://openaccess-api.clevelandart.org/api/artworks/?african_american_artists")
camcollections = json.loads(response.text)
camcollections = camcollections['data']

#[4]
# iterates through each observation and instantiates the Collectionitem
# class and also called it's methods into a dictionary
analysislist = []
for colldict in camcollections:
  coll = ci.Collectionitem(colldict)
  newdict = dict(id=colldict['id'],
    title=colldict['title'],
    type=colldict['type'],
    creationdate=colldict['creation_date'],
    ncreators=coll.ncreators(),
    ncitations=coll.ncitations(),
    birthyearsall=coll.birthyearsall(),
    birthyear=coll.birthyearcreator1())
  analysislist.append(newdict)

#[5]
# create dataframe from list of dictionaries
len(camcollections)
len(analysislist)
pprint.pprint(analysislist[0:1])
analysis = pd.DataFrame(analysislist)
analysis.birthyearsall.value_counts().head()
analysis.head(2)
ci.Collectionitem.collectionitemcnt
