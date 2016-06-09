from pymongo import MongoClient
client = MongoClient()
db = client.knock64_database
collection = db.knock64_collection
for data in collection.find({'name': 'Queen'}):
    print(data)
