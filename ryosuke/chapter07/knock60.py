import json
import plyvel

name2area_db = plyvel.DB('./name2area_db.ldb', create_if_missing=True)
for line in open('artist.json'):
    d = json.loads(line)
    if 'name' in d and 'area' in d:
        name2area_db.put(d['name'].encode('utf-8'), d['area'].encode('utf-8'))
