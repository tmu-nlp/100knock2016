import json
import plyvel
import pickle
import sys

artist_object_DB = plyvel.DB("artist__object_DB.ldb", create_if_missing = True)

for line in open("artist.json", "r"):
    data = json.loads(line)
    if "name" in data and "tags" in data:
        tags = pickle.dumps(data["tags"]) #シリアライズ(直列化)
        artist_object_DB.put(data["name"].encode("utf-8"), tags)

if artist_object_DB.get(str(sys.argv[1]).encode("utf-8")):
    ans = artist_object_DB.get(str(sys.argv[1]).encode("utf-8"))
    tag_list = pickle.loads(ans)
    for tag in tag_list:
        print("tag:{}\tcount:{}".format(tag["value"], tag["count"]))
else:
    print("{} does not exist".format(str(sys.argv[1])))


artist_object_DB.close()
