# knock66.py
# coding = utf-8
import pymongo
client = pymongo.MongoClient()
db = client.artistdb
collection = db["artist"]
data = collection.find({"area": "Japan"})

print(data.count())