import pandas as pd


########### Python 3.6 #############
import requests

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e6a8d45d-f346-413e-9aa3-98a08eff6376',
}

params ={
    # Query parameter
    'q': 'go to mumbai'
}

try:
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63?subscription-key=391d7db47c6d40a2ba262e8b90420db4&timezoneOffset=0', params=params)
    print(r.json())

except Exception as e:  
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
    
# importing the requests library
import requests
import json


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


# extracting latitude, longitude and formatted address 
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
	%(latitude, longitude,formatted_address))
