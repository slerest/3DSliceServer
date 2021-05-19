import requests
import json


import unittest

class PartTest(unittest.TestCase):

    def test_list_parts(self):
        url = 'http://localhost/slice-server/api/0.0/parts'
        h = {"Accept": "application/json"}
        r = requests.get(url, headers=h)
        assert r.status_code == 200

    def test_full_part(self):
         # CREATE PART
        url = 'http://localhost/slice-server/api/0.0/parts'
        body = {
            'name':'a good name',
            'unit': 'mm',
            'format': 'stl'
        }
        h = {"Accept": "application/json"}
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200

        # UPLOAD FILE TO PART
        id_part = str(r.json()['id'])
        url='http://localhost/slice-server/api/0.0/parts/upload-file/' + id_part
        f = open('file.stl','rb')
        files={'file_part': f}
        r=requests.post(url, files=files)
        assert r.status_code == 200
        f.close()

        # GET THIS PART
        url = 'http://localhost/slice-server/api/0.0/parts/' + id_part
        r = requests.get(url, headers=h)
        assert r.status_code == 200

        # DELETE THE PART
        url = 'http://localhost/slice-server/api/0.0/parts/' + id_part
        r = requests.delete(url, headers=h)
        assert r.status_code == 204


if __name__ == '__main__':
    unittest.main()
