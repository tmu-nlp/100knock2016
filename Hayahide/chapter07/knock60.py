import plyvel
import json

artist_db = plyvel.DB('artist_db.ldb', create_if_missing=True)

for line in open('artist.json', 'r'):
    json_data = json.loads(line)
    if 'name' in json_data and 'area' in json_data:
        artist_db.put(json_data['name'].encode('utf-8'), json_data['area'].encode('utf-8'))
