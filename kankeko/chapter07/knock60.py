import plyvel
import json

#with open("ファイル名") as fw:
def get_artist_DB():
    db = plyvel.DB('./db', create_if_missing=True)
    for line in open("artist.json"):
        data = json.loads(line)
        if "name" in data and "area" in data:
            print(data["name"])
            db.put(data["name"].encode("utf-8"),data["area"].encode("utf-8")        )


if __name__ == "__main__":
    get_artist_DB()
