import requests
import json
import unittest

class SliceTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(SliceTest, self).__init__(*args, **kwargs)
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

    def test_create_patch_delete(self):
        url = 'http://localhost/slice-server/api/0.0/slices'
        h = {"Accept": "application/json", 'Authorization': 'Bearer ' + self.token_admin}
        body = {
            'part_id': 1,
            'material_id': 1453,
            'slicer_id': 1453,
            'slice_spec': {
                'cura_definition_file_e0': 'test_f0',
                'cura_definition_file_e1': 'test_f1',
                'cura_parameters': [
                    {
                        'no_extruder': 0,
                        'key': 'test_key_0',
                        'value': 'test_value_0'
                    },
                    {
                        'no_extruder': 1,
                        'key': 'test_key_1',
                        'value': 'test_value_1'
                    }
                    ]
            },
            'comment': 'un commentaire'
        }
        r = requests.post(url, headers=h, data=json.dumps(body))
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
