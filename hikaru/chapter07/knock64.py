# -*- coding:utf-8 -*-
import gzip
import json
import pymongo
from pymongo import MongoClient

client = MongoClient()
artist_db = client.artist #データベース作成
collection = artist_db.artist_collection

for line in gzip.open("artist.json.gz"):
    my_dict = json.loads(line.decode('utf-8'))
    #collection.insert_one(my_dict).inserted_id
    collection.insert(my_dict)
collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
    
