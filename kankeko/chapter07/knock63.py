import plyvel
import json
import pickle


tags_db = plyvel.DB('./tags_db', create_if_missing=True)
def get_artist_tags_DB():
    tags_list = []
    for line in open("artist.json"):
        data = json.loads(line)
        if "tags" in data:
            tags_db.put(data["name"].encode("utf-8"), pickle.dumps([str(tag).encode("utf-8") for tag in data["tags"]]))

def get_artist_tags(name):
    artist_tags = pickle.loads(tags_db.get(name.encode("utf-8")))
    return artist_tags

if __name__ == "__main__":
    get_artist_tags_DB()
    for tag_dict in get_artist_tags("Oasis"):
        print(tag_dict.decode("utf-8"))
