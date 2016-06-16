# knock68.py
# coding = utf-8

import pymongo, sys
client = pymongo.MongoClient()
db = client.artistdb
collection = db["artist"]
# alias = sys.argv[1].strip()
data = collection.find({"tags.value":"dance"}, sort=[('rating.count', pymongo.DESCENDING)], limit=10)

for item in data:
    print(item)