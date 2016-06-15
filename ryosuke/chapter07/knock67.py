import sys
from pymongo import MongoClient


client = MongoClient()
db = client['100knock']
collection = db['artist']

for line in iter(sys.stdin.readline, '\n'):
    query = line.rstrip('\n')
    for data in collection.find({'aliases.name': query}):
        print(data)
