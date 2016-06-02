import json
from pymongo import MongoClient, ASCENDING

client = MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection

for line in open("artist.json", "r"):
    data = json.loads(line)
    collection.insert_one(data)

collection.create_index([("name", ASCENDING)])
collection.create_index([("aliases.name", ASCENDING)])
collection.create_index([("tags.value", ASCENDING)])
collection.create_index([("rating.value", ASCENDING)])
