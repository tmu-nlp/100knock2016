import pymongo

client = pymongo.MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection

print(collection.find({"area": "Japan"}).count())

#mongo
#use MusicBrainz_DB
#collection = db["artist_collection"]
#collection.find({"area": "Japan"}).count()
