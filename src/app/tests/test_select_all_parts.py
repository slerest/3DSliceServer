import requests
import json

url = 'http://localhost/slice-server/api/0.0/parts'
h = {"Accept": "application/json"}

r = requests.get(url, headers=h)
print(r.status_code)
print(r.json())
