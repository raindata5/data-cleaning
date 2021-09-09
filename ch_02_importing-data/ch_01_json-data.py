import pandas as pd
import numpy as np
import json
import pprint
from collections import Counter

pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 8)


#[]
#loading in data with json library, looking at shape, and looking at some of the data

with open('data/allcandidatenewssample.json') as f :
    candidatenews = json.load(f)

len(candidatenews)

pprint.pprint(candidatenews[0:2])
pprint.pprint(candidatenews[0]['source'])

#[]
# checking for differences in dictionaries
Counter([len(item) for item in candidatenews]) #loops through each dictionary and counts the #of keys then counter does it's job

pprint.pprint(next(item for item in candidatenews if len(item)<9))

pprint.pprint(next(item for item in candidatenews if len(item)>9))

pprint.pprint([item for item in candidatenews if len(item)==2][:10])

candidatenews = [item for item in candidatenews if len(item)>2]
len(candidatenews)

#[]
#
politico = [item for item in candidatenews if item['source'] == 'Politico']
len(politico)
pprint.pprint(politico[:2])

#[]
#
sources = [item['source'] for item in candidatenews]
len(sources)
sources[:10]

pprint.pprint(Counter(sources).most_common(10))

#[]
#

for sdict in candidatenews :
    sdict.update((k,'The Hill') for k,v in sdict.items()
    if k == "source" and v == "TheHill") #sdict.items to get the key and the value

sources = [item['source'] for item in candidatenews]
pprint.pprint(Counter(sources).most_common(10))

#[]
#

candidatenewsdf = pd.DataFrame(candidatenews)
candidatenewsdf.info()
