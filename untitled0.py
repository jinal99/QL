# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace this with a valid subscription key.
subscriptionKey = '2e3bdd54d74a499db467e62040a2b8ca'

# Replace this with a valid knowledge base ID.
kb = 'aac4c7b2-0138-4395-bf63-8ba96112dcbc'

# Replace this with "test" or "prod".
env = 'test';

host = 'westus.api.cognitive.microsoft.com'
service = '/qnamaker/v4.0'
method = '/knowledgebases/{0}/{1}/qna/'.format(kb, env);

def pretty_print (content):
# Note: We convert content to and from an object so we can pretty-print it.
    return json.dumps(json.loads(content), indent=4)

def get_qna (path):
    print ('Calling ' + host + path + '.')
    headers = {
        'Ocp-Apim-Subscription-Key': subscriptionKey,
    }
    conn = http.client.HTTPSConnection(host)
    conn.request ("GET", path, '', headers)
    response = conn.getresponse ()
    return response.read ()

path = service + method
result = get_qna (path)
questions = json.loads(result)
question_bank = {}
for i in questions.values():
    temp_1 = i
    for t in temp_1:
        print(t['questions'][0] + "   "+ t['answer'] )
        question_bank[t['questions'][0]] = t['answer']        
print (pretty_print(result))