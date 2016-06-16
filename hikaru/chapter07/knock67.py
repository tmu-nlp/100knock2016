# -*- coding:utf-8 -*-
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
artist_db = client.artist #データベース作成
collection = artist_db.artist_collection

aliases = "OASIS"
for line in collection.find({'aliases.name': aliases}):
    print (line)