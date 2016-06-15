import plyvel
import json
import pickle
import sys
tag_db=plyvel.DB('./tagsldb/',create_if_missing=True)
for line in open("artist.json","r"):
    data=json.loads(line)
    if "tags" in data:
        tag=pickle.dumps(data["tags"])
        tag_db.put(data["name"].encode('utf-8'),tag)

print(pickle.loads(tag_db.get(sys.argv[1].encode('utf-8'))))
tag_db.close()
