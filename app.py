from flask import Flask, request
from bson import ObjectId
import json
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://user1:root@cluster0.iw7et.mongodb.net/ProjetTestUnitaires?retryWrites=true&w=majority")
collection = client.ProjetTestUnitaires
db = collection.TestUnit

@app.route('/create', methods=['POST'])
def create():
    _json = request.json
    marque = _json['marque']
    titre = _json['titre']
    prix = _json['prix']
    query = { 'marque' : marque, 'titre' : titre, 'prix' : prix } 

    db.insert(query)

    return '200 sucessful'

@app.route('/read', methods=['GET'])
def read():
    documents = db.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    query = {'_id':ObjectId(id)}
    db.delete_one(query)
    return '200 sucessful'

@app.route('/update/<id>', methods=['PUT'])
def update(id):
    _json = request.json
    marque = _json['marque']
    titre = _json['titre']
    prix = _json['prix']
    query = { "_id": ObjectId(id) }
    newvalues = {'$set': { 'marque' : marque, 'titre' : titre, 'prix' : prix } }

    db.update_one(query, newvalues)

    return '200 sucessful'

if __name__ == '__main__':
    app.run(debug=True)