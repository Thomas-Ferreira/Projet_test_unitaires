import unittest
from unittest.mock import Mock
from scrapper import Scrapper
import requests

class TestScrapperMethods(unittest.TestCase):

    def setUp(self):
        self.scrapper_1 = Scrapper()
        self.test_dict = self.scrapper_1.navigate()

    def test_navigate(self):
       self.assertIsInstance(self.test_dict, dict)

class TestApiMethods(unittest.TestCase):

    URL='http://127.0.0.1:5000/'

    def test_read(self):
        response = requests.get(self.URL+'read')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()