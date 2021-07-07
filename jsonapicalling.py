from urllib.request import urlopen

import json

url = "https://www.boredapi.com/api/activity"

response = urlopen(url)

data_json = json.loads(response.read())

print(data_json)


#for i in data_json['activity']:
   # print()
    #print(i)

for j in data_json['type']:
    print(j) 