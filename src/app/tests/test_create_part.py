import requests
import json

url = 'http://localhost/slice-server/api/0.0/parts'
body = {
    'name':'a good name',
    'unit': 'mm',
    'format': 'stl'
}

h = {"Accept": "application/json"}
r = requests.post(url, headers=h, data=json.dumps(body))
print(r.status_code)
print(r.text)
