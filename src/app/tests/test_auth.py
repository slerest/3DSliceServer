import requests
import json
import unittest

class AuthTest(unittest.TestCase):

    def test_login(self):
        url = 'http://localhost/slice-server/api/0.0/auth/login'
        body = {
            'username':'admin',
            'password': 'secret'
        }
        h = {"Accept": "application/json"}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200

    def test_refresh(self):
        url = 'http://localhost/slice-server/api/0.0/auth/login'
        body = {
            'username':'admin',
            'password': 'secret'
        }
        h = {"Accept": "application/json"}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        token = r.json()['token']

        url = 'http://localhost/slice-server/api/0.0/auth/refresh'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
