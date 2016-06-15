from pymongo import MongoClient

client=MongoClient()
db=client.artist_db
collection=db.artist_collection

print(collection.find_one({"name":"Queen"}))
