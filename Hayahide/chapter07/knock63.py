#-*- coding: utf-8 -*-
import plyvel
import json
import sys

tag_db = plyvel.DB('tag_db.ldb', create_if_missing=True)

for line in open('artist.json', 'r'):
    json_data = json.loads(line)
    if 'name' in json_data and 'tags' in json_data:
        js = json.dumps(json_data['tags'])
        tag_db.put(json_data['name'].encode('utf-8'), js.encode('utf-8'))

query = ' '.join(sys.argv[1:])

artist_tags = tag_db.get(query.encode('utf-8'))
if artist_tags:
    print(json.loads(artist_tags.decode()))
else:
    print('"' + query + '" does not exist in this database.')

