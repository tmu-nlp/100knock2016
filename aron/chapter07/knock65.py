# knock65.py
# coding = utf-8
import pymongo
client = pymongo.MongoClient()
db = client.artistdb
collection = db["artist"]
data = collection.find({"name": "Queen"})

for item in data:
    print(item)