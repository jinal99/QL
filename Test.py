import http.client, urllib.parse, json, pandas as pd, requests

host = "my-qna.azurewebsites.net"
endpoint_key = "af78bfae-6430-4975-ae85-c46c2ac614a2"
kb = "aac4c7b2-0138-4395-bf63-8ba96112dcbc"
method = "/qnamaker/knowledgebases/aac4c7b2-0138-4395-bf63-8ba96112dcbc/generateAnswer"
#question1: 30 minute delivery
#question: otp undelivered
question = {
    'question': 'otp undelivered',
    'top': 1
}

def display_answer(result):
    load_result = json.loads(result)
    values_result = load_result.values()
    for t in values_result:
        return t[0]['answer']
    
def get_score(result):
    load_result = json.loads(result)
    values_result = load_result.values()
    for t in values_result:
        score = t[0]['score']
        return score

def get_predicted_question(result):
    load_result = json.loads(result)
    values_result = load_result.values()
    for t in values_result:
        temp = t[0]['questions']
        for l in temp:
            return l

def get_intent(result):
    temp1 = result['topScoringIntent']
    return temp1['intent']       
    
def pretty_print (content):
    return json.dumps(json.loads(content), indent=4)

def get_answers (path, content):
    
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
print('\n')
json.loads(result)
print("Predicted Question:"+get_predicted_question(result))
print("Actual question: "+question['question'])
print('\n')
print("Answer: "+display_answer(result))
print('\n')
score  = get_score(result)
print("Confidence score: "+str(score))
print('\n')
if score < 50:
    print('Since confidence score less than 50, calling LUIS.....')
    headers = {
        'Ocp-Apim-Subscription-Key': 'e6a8d45d-f346-413e-9aa3-98a08eff6376',
    }
    
    params ={
        'q': question['question']
    }
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/bac225d4-73f5-4485-993d-08a9db2b7b63?subscription-key=391d7db47c6d40a2ba262e8b90420db4&timezoneOffset=0', params=params)
    print("New Question: "+get_intent(r.json()))
    new_intent = get_intent(r.json())
    
    question = {
        'question': new_intent,
        'top': 1
    }
    
    content = json.dumps(question)
    result = get_answers (method, content)
    print('\n')
    json.loads(result)
    print("Predicted Question:"+get_predicted_question(result))
    print("Actual question: "+question['question'])
    print('\n')
    print("Answer: "+display_answer(result))
    print('\n')
    print("Confidence score: "+str(get_score(result)))


   
    


