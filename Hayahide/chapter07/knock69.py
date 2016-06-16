#以下、cgi-bin内に入れて使わないと動きません。
#ラジオボタンで選ばれた情報でクエリを検索します。

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from pymongo import MongoClient

client = MongoClient()
db = client.artist
db_collection = db.artist_collection

print('Content-Type: text/html; charset=UTF-8\n\n')
print('<html><body>')

form = cgi.FieldStorage()
query = str(form.getvalue('query', ''))
select = str(form.getvalue('select', ''))
answer = []
flag = False

if select == 'artist':
    artist_names = db_collection.find({'name': query})
    for line in artist_names:
        answer.append(line)
    flag = True

if select == 'aliase':
    aliase_names = db_collection.find({'aliases.name': query})
    for line in aliase_names:
        answer.append(line)
    flag = True

if select == 'tag':
    tag_names = db_collection.find({'tags.value': query})
    for line in tag_names:
        answer.append(line)
    flag = True

if flag:
    for line in answer:
        for key, value in line.items():
            print('<b>{}: {}</b><br>'.format(key, value))
        print('<br>')
else:
    print('<h3>Your query does not exist in this database.</h3>')

print('</body></html>')
