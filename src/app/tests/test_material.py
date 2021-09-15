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

    def test_create_patch_delete(self):
        url = 'http://localhost/slice-server/api/0.0/materials'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        body = {
            'supplier': 'str',
            'name': 'str',
            'general_type': 'str',
            'specific_type': 'str',
            'am_process': 'str'
        }
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        id_material = str(r.json()['id'])
        url = 'http://localhost/slice-server/api/0.0/materials/' + id_material
        body = {
            'supplier': 'foo',
            'name': 'foo',
            'ultimate_tensible_strength_min': 3.14
        }
        r = requests.patch(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        r = requests.delete(url, headers=h)
        assert r.status_code == 204

if __name__ == '__main__':
    unittest.main()
