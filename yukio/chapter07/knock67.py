import pymongo
import sys

client = pymongo.MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection

for line in collection.find({"aliases.name": sys.argv[1]}):
    for key, value in sorted(line.items()):
        print("{}:{}".format(key, value))
    print()
