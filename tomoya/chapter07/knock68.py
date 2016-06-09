from pymongo import MongoClient

client = MongoClient()
db = client.knock64_database
collection = db.knock64_collection
for data in collection.find({'tags.value': 'dance'}).sort('rating.count', -1).limit(10):
    print(data)
