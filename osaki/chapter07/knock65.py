from pymongo import MongoClient

client=MongoClient()
db=client.artist_db
collection=db.artist_collection

for item in collection.find({"name":"Queen"}):
    print(item)
