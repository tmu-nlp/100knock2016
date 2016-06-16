from pymongo import MongoClient
import sys
client = MongoClient()
db = client.knock64_database
collection = db.knock64_collection
for data in collection.find({'aliases.name': sys.argv[1]}):
    for key in data.keys():
        print('{}: {}'.format(key, data[key]))
