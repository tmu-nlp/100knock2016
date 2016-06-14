from pymongo import MongoClient
client = MongoClient()
db = client.knock64_database
collection = db.knock64_collection
count = 0
for data in collection.find({'area': 'Japan'}):
    count += 1
print(count)
