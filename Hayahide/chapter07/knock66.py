from pymongo import MongoClient

client = MongoClient()
db = client.artist
db_collection = db.artist_collection

print(db_collection.find({'area': 'Japan'}).count())
