from pymongo import MongoClient

client = MongoClient()
db = client.artist
db_collection = db.artist_collection

for line in db_collection.find({'tags.value': 'dance'}).sort('rating.count', -1).limit(10):
    print(line['name'] + '\t' + str(line['rating']['count']))
