import pymongo

client = pymongo.MongoClient()
db = client.MusicBrainz_DB
collection = db.artist_collection

for line in collection.find({"tags.value": "dance"}, {"name": 1, "rating.count": 1, "_id": 0}).sort("rating.count", -1).limit(10):
    print("{}\t{}".format(line["name"], line["rating"]["count"]))
