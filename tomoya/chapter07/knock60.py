# -*- coding:utf-8 -*-
import gzip
import json
import plyvel

my_db = plyvel.DB('knock60.ldb', create_if_missing=True)
for line in gzip.open('artist.json.gz'):
    line_dict = json.loads(line.decode('utf-8'))
    name = line_dict['name']
    area = line_dict['area'] if 'area' in line_dict.keys() else 'Null'
    my_db.put(name.encode('utf-8'), area.encode('utf-8'))
print(my_db.get('Oasis'.encode('utf-8')))
my_db.close()
