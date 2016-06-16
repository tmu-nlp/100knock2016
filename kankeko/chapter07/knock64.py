import json
from pymongo import MongoClient, ASCENDING
import pprint


with open('artist.json') as f:
    client = MongoClient()
    db = client.artist_db
    collection = db.artist_col
        #for line in f:
        #    data = json.loads(line)
        #    collection.insert(data)
collection.create_index([("name", ASCENDING)])
collection.create_index([("aliases.name", ASCENDING)])
collection.create_index([("tags.value", ASCENDING)])
collection.create_index([("rating.value", ASCENDING)])
for index in collection.list_indexes():
    pprint.pprint(index)
