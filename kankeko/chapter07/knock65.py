# mongo
# use artist_db
# db.artist_col.find({"name":"Queen"}).pretty()

from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.artist_db
collection = db.artist_col

findQueen = collection.find({'name': 'Queen'})

for doc in findQueen:
    pprint.pprint(doc)
