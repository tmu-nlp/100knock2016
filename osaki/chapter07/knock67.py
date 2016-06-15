from pymongo import MongoClient
import sys

client=MongoClient()
db=client.artist_db
collection=db.artist_collection

print(collection.find_one({"aliases.name":sys.argv[1]}))
