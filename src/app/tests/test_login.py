import requests
import json
import unittest

class LoginTest(unittest.TestCase):

    def test_login(self):
        url = 'http://localhost/slice-server/login'
        body = {
            'username':'admin',
            'password': 'secret'
        }
        h = {"Accept": "application/json"}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        print(r.status_code)
        print(r.text)
