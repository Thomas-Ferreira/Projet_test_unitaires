import unittest
from unittest.mock import Mock
from scrapper import Scrapper
from pymongo import MongoClient
from bson import ObjectId
import requests

class TestScrapperMethods(unittest.TestCase):

    def setUp(self):
        self.scrapper_1 = Scrapper()
        self.test_dict = self.scrapper_1.navigate()

    def test_navigate(self):
       self.assertIsInstance(self.test_dict, dict)

class TestApiMethods(unittest.TestCase):

    URL='http://127.0.0.1:5000/'

    client = MongoClient("mongodb+srv://user1:root@cluster0.iw7et.mongodb.net/ProjetTestUnitaires?retryWrites=true&w=majority")
    collection = client.ProjetTestUnitaires
    db = collection.TestUnit

    data_create = {
        "marque": "testMarque",
        "titre": "testTitre",
        "prix": "testPrix"
    }

    new_data = {
        "marque": "New_Marque",
        "titre": "New_Titre",
        "prix": "New_Prix"
    }

    def test_create(self):
        response = requests.post(self.URL+'create', json=self.data_create)
        self.assertEqual(response.status_code, 200)

    def test_read(self):
        response = requests.get(self.URL+'read')
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        data_update = self.db.find_one(self.data_create)
        id = data_update["_id"]
        response = requests.put(self.URL+'/update/'+str(ObjectId(id)), json=self.new_data)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        data_delete = self.db.find_one(self.new_data)
        id = data_delete["_id"]
        response = requests.delete(self.URL+'delete/'+str(ObjectId(id)))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()