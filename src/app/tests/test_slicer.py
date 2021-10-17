import requests
import json
import unittest
import trimesh
from pprint import pprint
import os

class SlicerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(SlicerTest, self).__init__(*args, **kwargs)
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

    def test_list_slicers(self):
        url = 'http://localhost/slice-server/api/0.0/slicers'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_get_slicer_by_id(self):
        url = 'http://localhost/slice-server/api/0.0/slicers/1453'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_create_patch_delete(self):
        url = 'http://localhost/slice-server/api/0.0/slicers'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        body = {
            'name': 'slicer',
            'version': '0.5'
        }
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        id_machine = str(r.json()['id'])
        url = 'http://localhost/slice-server/api/0.0/slicers/' + id_machine
        body = {
            'name': 'another name',
            'version': '1.0'
        }
        r = requests.patch(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        r = requests.delete(url, headers=h)
        assert r.status_code == 204

if __name__ == '__main__':
    unittest.main()
