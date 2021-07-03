import requests
import json
import unittest

class UserTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(UserTest, self).__init__(*args, **kwargs)
        # get token
        url = 'http://localhost/slice-server/api/0.0/auth/login'
        body = {
            'username':'admin',
            'password': 'secret'
        }
        h = {"Accept": "application/json"}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        self.token = r.json()['token']

    def test_create_user(self):
        url = 'http://localhost/slice-server/api/0.0/users'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        body = {
            'username':'user2',
            'email':'user2@gmail.com',
            'password':'ohohoho'
        }
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200

    def test_list_users(self):
        url = 'http://localhost/slice-server/api/0.0/users'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_user_by_email(self):
        url = 'http://localhost/slice-server/api/0.0/users?email=admin@admin.fr'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_user_by_username(self):
        url = 'http://localhost/slice-server/api/0.0/users?username=admin'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_user_by_id(self):
        url = 'http://localhost/slice-server/api/0.0/users/1'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_groups_of_user(self):
        url = 'http://localhost/slice-server/api/0.0/users/2/groups'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_permissions(self):
        url = 'http://localhost/slice-server/api/0.0/users/2/permission'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
