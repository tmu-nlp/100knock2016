import sys
from pymongo import MongoClient
from pymongo import ASCENDING
import json

client=MongoClient()
db=client.artist_db
collection=db.artist_collection

for line in open(sys.argv[1]):
    data=json.loads(line)
    collection.insert_one(data)

collection.create_index([("name",ASCENDING)])
collection.create_index([("aliases.name",ASCENDING)])
collection.create_index([("tags.value",ASCENDING)])
collection.create_index([("rating.value",ASCENDING)])
