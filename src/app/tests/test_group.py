import requests
import json
import unittest

class GroupTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(GroupTest, self).__init__(*args, **kwargs)
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

    def test_create_group(self):
        url = 'http://localhost/slice-server/api/0.0/groups'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        body = {'name':'group42'}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        url = 'http://localhost/slice-server/api/0.0/groups/' + str(r.json()['id'])
        r = requests.delete(url, headers=h)
        assert r.status_code == 204

    def test_list_groups(self):
        url = 'http://localhost/slice-server/api/0.0/groups'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_group_by_name(self):
        url = 'http://localhost/slice-server/api/0.0/groups?name=admin'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_group_by_id(self):
        url = 'http://localhost/slice-server/api/0.0/groups/1'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_users_of_group(self):
        url = 'http://localhost/slice-server/api/0.0/groups/1/users'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_add_user_to_group(self):
        url = 'http://localhost/slice-server/api/0.0/groups/1/users/1'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token}
        r = requests.post(url, headers=h)
        assert r.status_code == 200
        r = requests.delete(url, headers=h)
        assert r.status_code == 204

if __name__ == '__main__':
    unittest.main()
