import requests
import json
import unittest

def login_admin():
    url = 'http://localhost/slice-server/api/0.0/auth/login'
    body = {
        'username':'admin',
        'password': 'secret'
    }
    h = {"Accept": "application/json"}
    r = requests.post(url, headers=h, data=json.dumps(body))
    assert r.status_code == 200
    return r.json()['token']

def login_regular(id_user):
    url = 'http://localhost/slice-server/api/0.0/auth/login'
    body = {
        'username':'regular_' + str(id_user),
        'password': 'secret'
    }
    h = {"Accept": "application/json"}
    r = requests.post(url, headers=h, data=json.dumps(body))
    assert r.status_code == 200
    return r.json()['token']

class PermissionTest(unittest.TestCase):

    def test_regular_no_authorized_read_all(self):
        url = 'http://localhost/slice-server/api/0.0/parts'
        token = login_regular(4)
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + token}
        r = requests.get(url, headers=h)
        assert r.status_code == 401
    
    def test_regular_no_authorized_read(self):
        url = 'http://localhost/slice-server/api/0.0/parts/1'
        token = login_regular(4)
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + token}
        r = requests.get(url, headers=h)
        assert r.status_code == 401

    def test_regular_authorized_read(self):
        url = 'http://localhost/slice-server/api/0.0/parts/1'
        token = login_regular(1)
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + token}
        r = requests.get(url, headers=h)
        assert r.status_code == 401

if __name__ == '__main__':
    unittest.main()
