from pymongo import MongoClient

client = MongoClient()
db = client.artist
db_collection = db.artist_collection

collections = db_collection.find({'name': 'Queen'})

for line in collections:
    print(line)

# mongo's interactive_shell
#   use artist
#   db.artist_collection.find({'name': 'Queen'})
