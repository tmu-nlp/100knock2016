import json
import gzip
from pymongo import MongoClient, ASCENDING

client = MongoClient()
db = client.artist
db_collection = db.artist_collection

for line in gzip.open('artist.json.gz'):
    db_collection.insert_one(json.loads(line.decode('utf-8')))
print('Insertion was finished.')

db_collection.create_index([('name', ASCENDING)])
print('index "name" was created.')
db_collection.create_index([('aliases.name', ASCENDING)])
print('index "aliases.name" was created.')
db_collection.create_index([('tags.value', ASCENDING)])
print('index "tags.value" was created.')
db_collection.create_index([('rating.value', ASCENDING)])
print('The index "rating.value" was created.')
