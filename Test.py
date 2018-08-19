# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time, pandas as pd, requests

# NOTE: Replace this with a valid host name.
host = "my-qna.azurewebsites.net"

# NOTE: Replace this with a valid endpoint key.
# This is not your subscription key.
# To get your endpoint keys, call the GET /endpointkeys method.
endpoint_key = "af78bfae-6430-4975-ae85-c46c2ac614a2"

# NOTE: Replace this with a valid knowledge base ID.
# Make sure you have published the knowledge base with the
# POST /knowledgebases/{knowledge base ID} method.
kb = "aac4c7b2-0138-4395-bf63-8ba96112dcbc"

method = "/qnamaker/knowledgebases/aac4c7b2-0138-4395-bf63-8ba96112dcbc/generateAnswer"

question = {
    'question': 'validity gift card ',
    'top': 1
}

def pretty_print (content):
# Note: We convert content to and from an object so we can pretty-print it.
    return json.dumps(json.loads(content), indent=4)

def get_answers (path, content):
    print ('Calling ' + host + path )
    headers = {
        'Authorization': 'EndpointKey ' + endpoint_key,
        'Content-Type': 'application/json',
        'Content-Length': len (content)
    }
    conn = http.client.HTTPSConnection(host)
    conn.request ("POST", path, content, headers)
    response = conn.getresponse ()
    return response.read ()

# Convert the request to a string.
content = json.dumps(question)
result = get_answers (method, content)
temp = json.loads(result)
temp1 = temp.values()
score = 0
for t in temp1:
    score = t[0]['score']
print(pretty_print(result))

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e6a8d45d-f346-413e-9aa3-98a08eff6376',
}

params ={
    # Query parameter
    'q': question['question']
}

try:
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63?subscription-key=391d7db47c6d40a2ba262e8b90420db4&timezoneOffset=0', params=params)
    print(r.json())

except Exception as e:  
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
    
# importing the requests library



header= {
       'Host': 'westus.api.cognitive.microsoft.com',
'Content-Type': 'application/json',
'Ocp-Apim-Subscription-Key': '391d7db47c6d40a2ba262e8b90420db4'
        }
# api-endpoint

# sending get request and saving the response as response object
r = requests.post(r"https://westus.api.cognitive.microsoft.com/luis/api/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63/versions/0.1/intents",json.dumps(header),json.dumps({"Name": 'hello'}))
r.status_code
# extracting data in json format
data = r.json()

