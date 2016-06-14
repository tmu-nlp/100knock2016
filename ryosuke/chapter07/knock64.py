import json
from pymongo import MongoClient
from pymongo import ASCENDING


client = MongoClient()
db = client['100knock']
collection = db['artist']

for line in open('artist.json'):
    d = json.loads(line)
    collection.insert_one(d)

collection.create_index([("name", ASCENDING)])
collection.create_index([("aliases.name", ASCENDING)])
collection.create_index([("tags.value", ASCENDING)])
collection.create_index([("rating.value", ASCENDING)])
