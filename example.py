import json, pprint, requests, textwrap

host = 'http://localhost:8998'
data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
print(r.json())

print(r.headers['location'])


