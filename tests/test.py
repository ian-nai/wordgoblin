import unittest
from src.wordgoblin.main import wordgoblin

class TestClient(unittest.TestCase):

    sample_letters = "arn"
    test_list = ['aran', 'ran', 'garn']
    

    import importlib.resources
    import os

    dict_path = os.path.join(os.path.dirname(__file__), 'data')
    dict_filename = dict_path + "/test_dict.json"
    
        
    def test_dict_oneArg(self):
        assert wordgoblin.check_dict(TestClient.sample_letters) == ['arn', 'arna', 'nar', 'narr', 'narra', 'raanan', 'ran', 'rana', 'rann']

    def test_dict_wordSize(self):
        assert wordgoblin.check_dict(TestClient.sample_letters, 3) == ['arn', 'nar', 'ran']

    def test_dict_customDict(self):
        assert wordgoblin.check_dict(TestClient.sample_letters, TestClient.dict_filename) == ['ran', 'aran']

    def test_dict_customDict_wordSize(self):
        assert wordgoblin.check_dict(TestClient.sample_letters, TestClient.dict_filename, 4) == ['aran']

    def test_list_twoArgs(self):
        assert wordgoblin.check_list(TestClient.sample_letters, TestClient.test_list) == ['aran', 'ran']

    def test_list_wordSize(self):
        assert wordgoblin.check_list(TestClient.sample_letters, TestClient.test_list, 4) == ['aran']


if __name__ == "__main__":
     unittest.main()