# knock67.py
# coding = utf-8
import pymongo, sys
client = pymongo.MongoClient()
db = client.artistdb
collection = db["artist"]
alias = sys.argv[1].strip()
data = collection.find({"aliases.name":alias})

for line in data:
	for key, value in line.items():
		print(key, value)