# -*- coding:utf-8 -*-
import gzip
import json
import plyvel
import pickle
import os.path
import sys

my_db = plyvel.DB('knock63.ldb', create_if_missing=True)
if not os.path.isdir('./knock63.ldb'):
    for line in gzip.open('artist.json.gz'):
        line_dict = json.loads(line.decode('utf-8'))
        name = line_dict['name']
        tag = line_dict['tags'] if 'tags' in line_dict.keys() else []
        my_db.put(name.encode('utf-8'), pickle.dumps(tag))  

tags = my_db.get(sys.argv[1].encode('utf-8'))
if tags != None:
    tag_list = pickle.loads(tags)
    for tag in tag_list:
        print('{}, {}'.format(tag['value'], tag['count']))
my_db.close()
