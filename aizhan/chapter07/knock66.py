# mongo
# use artist_db
# db.artist_col.count({"area":"Japan"})

from pymongo import MongoClient

client = MongoClient()
db = client.artist_db
collection = db.artist_col

print(collection.count({'area': 'Japan'}))
