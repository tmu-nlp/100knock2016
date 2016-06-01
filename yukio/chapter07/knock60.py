import json
import plyvel

artist_DB = plyvel.DB("artist_DB.ldb", create_if_missing = True)

for line in open("artist.json", "r"):
    data = json.loads(line)
    if "name" in data and "area" in data:
        artist_DB.put(data["name"].encode("utf-8"), data["area"].encode("utf-8"))

artist_DB.close()
