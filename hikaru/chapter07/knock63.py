import gzip
import json
import plyvel

my_db2 = plyvel.DB('plyveldb', create_if_missing=True)  # なければつくる
for line in gzip.open("artist.json.gz"):
    my_dict = json.loads(line.decode('utf-8'))
    name = my_dict['name']
    tags = my_dict['tags'] if 'tags' in my_dict.keys() else [1]
    js = json.dumps(tags)
    my_db2.put(name.encode('utf-8'), js.encode())

print (my_db2.get('Oasis'.encode('utf-8')))
my_db2.close()

