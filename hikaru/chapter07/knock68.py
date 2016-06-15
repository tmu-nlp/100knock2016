# -*- coding:utf-8 -*-
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
artist_db = client.artist #データベース作成
collection = artist_db.artist_collection

rating_list = list()
'''
for line in collection.find():
    if 'tags' in line and 'dance' == line['tags'][0]['value']:
        if 'rating' in line:
            rating_list.append([line, int(line['rating']['count'])])
'''
for line in collection.find({"tags.value": "dance"}):
    if 'rating' in line:
        rating_list.append([line, int(line['rating']['count'])])

for top10, count in sorted(rating_list, key=lambda x: -x[1])[:10]:
    print (top10['name'])