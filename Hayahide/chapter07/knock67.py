import sys
from pymongo import MongoClient

client = MongoClient()
db = client.artist
db_collection = db.artist_collection

query = sys.argv[1]
collections = db_collection.find({'aliases.name': query})

for line in collections:
    print(line)
