import pandas as pd
import http.client
import json
import numpy
import re

data = pd.read_excel(r"C:\Users\jinal.hitesh.thakkar\OneDrive - Accenture\LUIS Data1.xlsx")

data.columns
intent = data[data['Intent'].notnull()]['Intent']

header= {
       'Host': 'westus.api.cognitive.microsoft.com',
'Content-Type': 'application/json',
'Ocp-Apim-Subscription-Key': '391d7db47c6d40a2ba262e8b90420db4'
        }

config_open = open(r"C:\Users\jinal.hitesh.thakkar\LUIS\config.json")
config_load = json.load(config_open)
entities = data[data['Entities'].notnull()]['Entities']


for i in intent:
    conn = http.client.HTTPSConnection("westus.api.cognitive.microsoft.com")
    conn.request("POST", "https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63/versions/0.1/intents",json.dumps({"Name": i}), header)
    response = conn.getresponse()
    print(i+"    "+str(response.code))

for e in entities:
    conn = http.client.HTTPSConnection("westus.api.cognitive.microsoft.com")
    conn.request("POST", "https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63/versions/0.1/entities",json.dumps({"Name": e}), header)
    response = conn.getresponse()
    print(e+"    "+str(response.code))


####################################################################################################
#    try:
#    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
#    conn.request("POST", "/luis/v1.0/prog/apps/bac225d4-73f5-4485-993d-08a9db2b7b63/compositeentities?%s" % params, "{body}", headers)
#    response = conn.getresponse()
#    data = response.read()
#    print(data)
#    conn.close()
#except Exception as e:
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
entities = data[data['Entities'].notnull()]['Entities']
utterances = data[data['Utterances'].notnull()]['Utterances'] 
data = pd.read_excel(r"C:\Users\jinal.hitesh.thakkar\OneDrive - Accenture\LUIS Data1.xlsx")

for u in utterances:
   r = list()
   send = dict()
   intent_send = data[data['Utterances'] == u]['Intent'].item().strip()
   for e in entities:
       if (str(e).lower() in str(u).lower()):
           for occ in re.finditer(str(e).lower(), str(u).lower()):
               print(e,occ.start(), occ.end())
               r.append({'entityName':e.strip(), 'startCharIndex':occ.start(), 'endCharIndex':occ.end()})
   send = {'text': u,  'intentName':intent_send, 'entityLabels': []}
   send['entityLabels'] = r
   conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
   conn.request("POST", "https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63/versions/0.1/example", json.dumps(send), header)
   response = conn.getresponse()
   print(u+ " "+ str(response.code))
   conn.close()

conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn.request("POST", "https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63/versions/0.1/train" )
response = conn.getresponse()
print(u+ " "+ str(response.code))
conn.close()
   