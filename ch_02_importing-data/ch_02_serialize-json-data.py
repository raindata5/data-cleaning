import pandas as pd
import json
import pprint
import requests
import msgpack

pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 8)

response = requests.get("https://openaccess-api.clevelandart.org/api/artworks/?african_american_artists")

camcollections = json.loads(response.text)
len(camcollections['data'])

pprint.pprint(camcollections['data'][0])

#[]
# load because it was read first
with open('views/camcollections.json','w') as f:
    json.dump(camcollections,f)

with open('views/camcollections.json','r') as f :
    camcollections = json.load(f)

pprint.pprint(camcollections['data'][0]['creators'])

#[]
#
with open('views/camcollections.msgpack','wb') as file:
    packed = msgpack.packb(camcollections)
    file.write(packed)

#[]
#
with open('views/camcollections.msgpack','rb') as data_file:
    msgbytes = data_file.read()

camcollections = msgpack.unpackb(msgbytes)
pprint.pprint(camcollections['data'][0]['creators'])
