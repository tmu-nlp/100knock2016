# db.artist.find({name: 'Queen'})
from pymongo import MongoClient


client = MongoClient()
db = client['100knock']
collection = db['artist']

for data in collection.find({'name': 'Queen'}):
    print(data)
