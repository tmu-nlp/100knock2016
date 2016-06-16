# -*- coding: utf-8 -*-

# mongo
# use artist_db
# db.artist_col.find({"tags.value":"dance"}).sort({"rating.count": -1}).limit(10).pretty()

from pymongo import DESCENDING  #RYOSUKE
from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.artist_db
collection = db.artist_col

for data in collection.find({'tags.value': 'dance'}, sort=[('rating.count', DESCENDING)], limit=10):
    print(data['rating']['count'], data['name'])
