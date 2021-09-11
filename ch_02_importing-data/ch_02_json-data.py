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
# checking for differences in dictionaries, and pprint them to get an understanding of why they have their structure
Counter([len(item) for item in candidatenews]) #loops through each dictionary and counts the number of keys then counter does it's job

pprint.pprint(next(item for item in candidatenews if len(item)<9)) #next will iterate just one item from a list
                                                                    #the list comprehension has no need for brackets inside the next function
pprint.pprint(next(item for item in candidatenews if len(item)>9))

pprint.pprint([item for item in candidatenews if len(item)==2][:10])
# going to remove those that dictionaries that have 2 keys or less
candidatenews = [item for item in candidatenews if len(item)>2]
len(candidatenews)

#[]
# extracting those articles with politico as a source
politico = [item for item in candidatenews if item['source'] == 'Politico']
len(politico)
pprint.pprint(politico[:2])

#[]
# inspecting the most common sources
sources = [item.get('source') for item in candidatenews]
len(sources)
sources[:10]

pprint.pprint(Counter(sources).most_common(10))


#[]
# will update thehill to include a space
for sdict in candidatenews :
    sdict.update((k,'The Hill') for k,v in sdict.items() #update function used to modify the key and value pair , no brackets needed for dictionary comprehension
    if k == "source" and v == "TheHill") #sdict.items to get the key and the value

sources = [item.get('source') for item in candidatenews]
pprint.pprint(Counter(sources).most_common(10))

#[]
# convert dictionary to dataframe
candidatenewsdf = pd.DataFrame(candidatenews)
candidatenewsdf.info()

#[]
# change tha name of column and convert to datetime since dates in dictionaries are just strings
candidatenewsdf.rename({'date':'story_date'},axis=1,inplace=True)
candidatenewsdf['story_date'] = candidatenewsdf['story_date'].astype('datetime64[ns]')
candidatenewsdf.shape
candidatenewsdf['source'].value_counts()
