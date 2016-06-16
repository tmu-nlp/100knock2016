#!/usr/bin/env python

from pymongo import MongoClient
import pymongo
import cgi

print ("Content-Type: text/html\n\n")
print ("<html>")
print ("<head>")
print ('<meta charset="utf-8">')
print ("</head>")
print ("<body>")

f = cgi.FieldStorage()
searchword_list = ["name", "aliases.name", "tags.value", "area"]
result_list = list()
for searchword in searchword_list:
    result_list.append(f.getfirst(searchword, ''))
find_dict = dict()

client = MongoClient('localhost', 27017)
artist_db = client.artist #データベース作成
collection = artist_db.artist_collection

for word, result in zip(searchword_list, result_list):
    if result != '':
        find_dict[word] = result

for line in collection.find(find_dict).sort([('rating.value', pymongo.DESCENDING)]):
    print ("<h1>")
    print ("わーーーーーーーーー")
    print ("</h1>")
    print ("<h1>")
    print ("アーティスト:{}".format(line["name"]))
    print ("</h1>")
    print ("<h1>")
    if "aliases" in line:
        print ("別名:{}".format(line["aliases"][0]["name"]))
    else:
        print ("別名はないよ")
    print ("</h1>")
    print ("<h1>")
    if "tags" in line:
        print ("ジャンル:{}".format(line['tags'][0]['value']))
    else:
        print ("ジャンルは決まってないよ")
    print ("</h1>")
    print ("<h1>")
    print ("エリア:{}".format(line["area"]))
    print ("</h1>")


print ("</body>")
print ("</html>")
#外部から読み込みたい時はこれやるよ chmod 755 cgi-bin/knock69.cgi
#python -m http.server --cgi でサーバを立ち上げるよ
#http://localhost:8000につなぐよ search.htmlを開くよ
