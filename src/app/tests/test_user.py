
import requests
import json
import unittest

class UserTest(unittest.TestCase):

    def test_list_users(self):
        url = 'http://localhost/slice-server/api/0.0/users'
        h = {"Accept": "application/json"}
        r = requests.get(url, headers=h)
        print(r.status_code)
        print(r.text)
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
