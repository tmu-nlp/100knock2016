from pymongo import MongoClient
from pymongo import DESCENDING


client = MongoClient()
db = client['100knock']
collection = db['artist']

for data in collection.find({'tags.value': 'dance'}, sort=[('rating.count', DESCENDING)], limit=10):
    print(data['rating']['count'], data['name'])
