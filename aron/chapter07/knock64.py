# knock64.py
# coding = utf-8
import pymongo, json
client = pymongo.MongoClient()
db = client.artistdb
collection = db["artist"]

with open("artist.json") as jsonfile:
	for line in jsonfile:
		jdata = json.loads(line.strip())
		collection.insert(jdata)
		
collection.create_index([("name", pymongo.ASCENDING)])
collection.create_index([("aliases.name", pymongo.ASCENDING)])
collection.create_index([("tags.value", pymongo.ASCENDING)])
collection.create_index([("rating.value", pymongo.ASCENDING)])