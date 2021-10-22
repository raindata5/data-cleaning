import pandas as pd
import requests
import numpy as np
import json as json
import pprint


#[]
# send a get request to the api, and load in the data as a json object
response = requests.get("https://openaccess-api.clevelandart.org/api/artworks/?african_american_artists")

camcollections = json.loads(response.text)
print(len(camcollections['data']))
#here we specify the data key since it is what we need for the analysis rather the info object
pprint.pprint(camcollections['data'][0])

#[]
#muliple citations so this will break them apart and allow the other columns to be duplicated (citation ,page # , and url)
camcollectionsdf = pd.json_normalize(camcollections['data'],'citations',['accession_number','title','creation_date','collection','creators','type'])
camcollectionsdf.head(2).T

#[]
#
pd.json_normalize(camcollections['data'],'provenance',['accession_number','technique',['exhibitions','current']]).columns
#[]
# inspecting data to find method to getting only the initial creator and then doing so
creator = camcollectionsdf[:1].creators[0]
type(creator[0])
pprint.pprint(creator)

camcollectionsdf['birthyear'] = camcollectionsdf.creators.apply(lambda x: x[0]['birth_year'])

#would prefer to come back and do some more data integrity checks in the dictionary itself
