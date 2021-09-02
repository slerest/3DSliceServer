import requests
import json
import unittest
import trimesh
from pprint import pprint
import os

class PartTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(PartTest, self).__init__(*args, **kwargs)
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

    def test_list_parts(self):
        url = 'http://localhost/slice-server/api/0.0/parts'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_list_parts_regular(self):
        url = 'http://localhost/slice-server/api/0.0/parts'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_regular}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_modify_part(self):
        # CREATE PART
        url = 'http://localhost/slice-server/api/0.0/parts'
        body = {
            'name':'coucou',
            'unit': 'mm',
            'format': 'stl'
        }
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200

        # MODIFY PART
        url = 'http://localhost/slice-server/api/0.0/parts/' + str(r.json()['id'])
        body = {
            'name':'WOWOWO',
            'unit': 'mm',
            'format': 'stl'
        }
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.put(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200

        # MODIFY PART
        r = requests.get(url, headers=h)
        assert r.status_code == 200

        # DELETE THE PART
        r = requests.delete(url, headers=h)
        assert r.status_code == 204

    def test_create_part(self):
        # CREATE PART
        url = 'http://localhost/slice-server/api/0.0/parts'
        body = {
            'name':'a_good_name',
            'unit': 'mm',
            'format': 'stl'
        }
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200
        # DELETE THE PART
        id_part = str(r.json()['id'])
        url = 'http://localhost/slice-server/api/0.0/parts/' + id_part
        r = requests.delete(url, headers=h)
        assert r.status_code == 204

    def test_full_part(self):
        # CREATE PART
        url = 'http://localhost/slice-server/api/0.0/parts'
        body = {
            'name':'a_good_name',
            'unit': 'mm',
            'format': 'stl'
        }
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200

        # UPLOAD FILE TO PART
        id_part = str(r.json()['id'])
        url='http://localhost/slice-server/api/0.0/parts/file/' + id_part
        f = open('FredTheCowboy.stl','rb')
        files={'file_part': f}
        r = requests.post(url, files=files)
        assert r.status_code == 200
        f.close()

        # GET THIS PART
        url = 'http://localhost/slice-server/api/0.0/parts/' + id_part
        r = requests.get(url, headers=h)
        assert r.status_code == 200

        # DOWNLOAD PART
        url = 'http://localhost/slice-server/api/0.0/parts/file/' + id_part
        r = requests.get(url, headers=h)
        f = open('./foo.stl', 'wb')
        f.write(r.content)
        f.close()
        assert r.status_code == 200

        mesh = trimesh.load('./foo.stl')

        # DELETE THE PART
        url = 'http://localhost/slice-server/api/0.0/parts/' + id_part
        r = requests.delete(url, headers=h)
        assert r.status_code == 204

        # DELETE LOCAL FILE
        os.remove('./foo.stl')

    def test_get_part_no_permission(self):
        url = 'http://localhost/slice-server/api/0.0/parts'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_regular}
        r = requests.get(url, headers=h)
        assert r.status_code == 403

if __name__ == '__main__':
    unittest.main()
