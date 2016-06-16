# -*- coding:utf-8 -*-
import gzip
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
artist_db = client.artist #データベース作成
collection = artist_db.artist_collection

for line in collection.find({'area': 'Japan'}):
    print (line['name'])