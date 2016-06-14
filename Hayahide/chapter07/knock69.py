#以下、cgi-bin内に入れて使わないと動かない。

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from pymongo import MongoClient

client = MongoClient()
db = client.artist
db_collection = db.artist_collection

print('Content-Type: text/html\n\n')
print('<html><body>')

form = cgi.FieldStorage()
artist = str(form.getvalue('artist', ''))
aliase = str(form.getvalue('aliase', ''))
tag = str(form.getvalue('tag', ''))
answer_set = []
flag = False

if len(artist) > 0:
    artist_names = db_collection.find({'name': artist})
    for line in artist_names:
        answer_set.append(line)
    flag = True

if len(aliase) > 0:
    aliase_names = db_collection.find({'aliases.name': aliase})
    for line in aliase_names:
        answer_set.append(line)
    flag = True

if len(tag) > 0:
    tag_names = db_collection.find({'tags.value': tag})
    for line in tag_names:
        answer_set.append(line)
    flag = True

if flag:
    for line in answer_set:
        for key, value in line.items():
            print('<b>{}: {}</b><br>'.format(key, value))
        print('<br>')
else:
    print('<h3>Your queries does not exist in this database.</h3>')

print('</body></html>')
