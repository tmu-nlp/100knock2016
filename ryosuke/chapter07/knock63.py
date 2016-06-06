import sys
import json
import pickle
import plyvel


print('Create DB')
name2tag_db = plyvel.DB('name2tag_db.ldb', create_if_missing=True)
for line in open('artist.json'):
    d = json.loads(line)
    if 'name' in d and 'tags' in d:
        name = d['name'].encode('utf-8')
        tags = pickle.dumps(d['tags'])
        name2tag_db.put(name, tags)

print('Done')
for line in iter(sys.stdin.readline, '\n'):
    name = line.rstrip('\n').encode('utf-8')
    tags = name2tag_db.get(name)
    if tags is not None:
        tags = pickle.loads(tags)
    print(tags)
