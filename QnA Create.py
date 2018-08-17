import http.client, urllib.parse, json, time

###################### generate a QnA knowledge Base ###########################################
# Replace this with a valid subscription key.
subscriptionKey = '2e3bdd54d74a499db467e62040a2b8ca'

# Represents the various elements used to create HTTP request path
# for QnA Maker operations.
host = 'westus.api.cognitive.microsoft.com'
service = '/qnamaker/v4.0'
method = '/knowledgebases/create'

def pretty_print(content):
  # Note: We convert content to and from an object so we can pretty-print it.
  return json.dumps(json.loads(content), indent=4)

def create_kb(path, content):
  print('Calling ' + host + path + '.')
  headers = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Content-Type': 'application/json',
    'Content-Length': len (content)
  }
  conn = http.client.HTTPSConnection(host)
  conn.request ("POST", path, content, headers)
  response = conn.getresponse ()
  # /knowledgebases/create returns an HTTP header named Location that contains a URL
  # to check the status of the operation in creating the knowledge base.
  return response.getheader('Location'), response.read ()

def check_status(path):
  print('Calling ' + host + path + '.')
  headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
  conn = http.client.HTTPSConnection(host)
  conn.request("GET", path, None, headers)
  response = conn.getresponse ()
  # If the operation is not finished, /operations returns an HTTP header named Retry-After
  # that contains the number of seconds to wait before we query the operation again.
  return response.getheader('Retry-After'), response.read ()

req = {
  "name": "My KB",
  "qnaList": [
    {
      "id": 0,
      "answer": "Hello. How May I Help You ?",
      "source": "Custom Editorial",
      "questions": [
        "Hi"
      ],
      "metadata": [
        {
          "name": "category",
          "value": "api"
        }
      ]
    }
  ],
  "urls": [
    "https://pizzaonline.dominos.co.in/faq"
  ],
  "files": []
}

# Builds the path URL.
path = service + method
# Convert the request to a string.
content = json.dumps(req)
# Retrieve the operation ID to check status, and JSON result
operation, result = create_kb(path, content)
# Print request response in JSON with presentable formatting
print(pretty_print(result))

done = False
while False == done:
  path = service + operation
  # Gets the status of the operation.
  wait, status = check_status(path)
  # Print status checks in JSON with presentable formatting
  print(pretty_print(status))

  # Convert the JSON response into an object and get the value of the operationState field.
  state = json.loads(status)['operationState']
  # If the operation isn't finished, wait and query again.
  if state == 'Running' or state == 'NotStarted':
    print('Waiting ' + wait + ' seconds...')
    time.sleep(int(wait))
  else:
    done = True # request has been processed, if successful, knowledge base is created
    
########################################### test QnA maker ###########################################


host = "https://my-qna.azurewebsites.net/qnamaker"

# NOTE: Replace this with a valid endpoint key.
# This is not your subscription key.
# To get your endpoint keys, call the GET /endpointkeys method.
endpoint_key = "af78bfae-6430-4975-ae85-c46c2ac614a2"

# NOTE: Replace this with a valid knowledge base ID.
# Make sure you have published the knowledge base with the
# POST /knowledgebases/{knowledge base ID} method.
kb = "aac4c7b2-0138-4395-bf63-8ba96112dcbc"

method = "/knowledgebases/"+kb+"/generateAnswer"

question = {
    'question': 'Is the customer charged for the SMS?',
    'top': 3
}


def get_answers (path, content):
    print ('Calling ' + host + path + '.')
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
print (pretty_print(result))