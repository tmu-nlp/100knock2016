# mongo
# use artist_db
# db.artist_col.find({$or:[{"name":"Oasis"},{"name":"Queen"}]}).pretty()

from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.artist_db
collection = db.artist_col

pprint.pprint(collection.find({"name": "Oasis"}))
