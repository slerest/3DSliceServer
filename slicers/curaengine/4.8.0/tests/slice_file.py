#import unittest
import requests

'''
class TestPostFile(unittest.TestCase):

    def test_post_file(self):
        with open("./slice_file.py", "rb") as f:
            body = {"definition_file": 'a_definition_file.json', "stl_file": f}
            response = requests.post("http://localhost/curaengine/4.8.0/api", files=f)
            print(response)

if __name__ == '__main__':
    unittest.main()
'''


with open("./slice_file.py", "rb") as f:
    body = {"definition_file": 'a_definition_file.json'}
    f_dict = {'file.stl': f}
    h = {"accept: application/json", "Content-Type: multipart/form-data"}
    response = requests.post("http://localhost/curaengine/api/4.8.0/slices", files=f_dict, data=body)
    print(response.text)
