import pymongo

client = pymongo.MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection

for line in collection.find({"name": "Queen"}):
    for key, value in sorted(line.items()):
        print("{}:{}".format(key, value))
    print()

#mongo
#use MusicBrainz_DB
#collection = db["artist_collection"]
#collection.find({"name": "Queen"})
