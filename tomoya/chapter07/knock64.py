# -*- coding:utf-8 -*-
import gzip
import json
from pymongo import MongoClient

client = MongoClient()
db = client.knock64_database
collection = db.knock64_collection
for line in gzip.open('artist.json.gz'):
    post = json.loads(line.decode('utf-8'))
    collection.insert(post)
collection.create_index([('name', 1)])
collection.create_index([('aliases.name', 1)])
collection.create_index([('tags.value', 1)])
collection.create_index([('rating.value', 1)])
