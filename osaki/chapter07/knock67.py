from pymongo import MongoClient
import sys

client=MongoClient()
db=client.artist_db
collection=db.artist_collection

for item in collection.find({"aliases.name":sys.argv[1]}):
    print(item)
