import requests
import json


import unittest

class PartTest(unittest.TestCase):

    def test_full_part(self):

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
        url='http://localhost/slice-server/api/0.0/parts/upload-file/' + str(r.json()['id'])
        f = open('file.stl','rb')
        files={'file_part': f}
        r=requests.post(url, files=files)
        assert r.status_code == 200
        f.close()

if __name__ == '__main__':
    unittest.main()
