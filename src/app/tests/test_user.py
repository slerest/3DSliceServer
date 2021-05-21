
import requests
import json
import unittest

class UserTest(unittest.TestCase):

    '''
    def test_create_user(self):
        url = 'http://localhost/slice-server/api/0.0/users'
        h = {"Accept": "application/json"}
        body = {
            'username':'slerest',
            'email':'slerest@gmail.com'
        }
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
    '''

    def test_list_users(self):
        url = 'http://localhost/slice-server/api/0.0/users'
        h = {"Accept": "application/json"}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_user_by_email(self):
        url = 'http://localhost/slice-server/api/0.0/users?email=admin@admin.fr'
        h = {"Accept": "application/json"}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_user_by_username(self):
        url = 'http://localhost/slice-server/api/0.0/users?username=admin'
        h = {"Accept": "application/json"}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_user_by_id(self):
        url = 'http://localhost/slice-server/api/0.0/users/1'
        h = {"Accept": "application/json"}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
