import requests
import json
import unittest
import trimesh
from pprint import pprint
import os

class MaterialTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MaterialTest, self).__init__(*args, **kwargs)
        # get token
        url = 'http://localhost/slice-server/api/0.0/auth/login'
        body = {
            'username':'admin',
            'password': 'secret'
        }
        h = {"Accept": "application/json"}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        self.token_admin = r.json()['token']
        body = {
            'username':'regular_1',
            'password': 'secret'
        }
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        self.token_regular = r.json()['token']

    def test_list_materials(self):
        url = 'http://localhost/slice-server/api/0.0/materials'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_material_by_id(self):
        url = 'http://localhost/slice-server/api/0.0/materials/1453'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
