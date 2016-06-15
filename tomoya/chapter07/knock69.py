#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from pymongo import MongoClient

print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>検索結果</title>")
print("<style>")
print("table{border-collapse:collapse;\ntable-layout: fixed;}")
print("td{border:solid 1px;\npadding: 2em;}")
print("</style>")
print("</head>")
print("<body>")
print('<form action="knock69.py" method="post">')
print('<p>アーティスト名<input type="text" name="name"></p>')
print('<p>別名<input type="text" name="aliases.name"></p>')
print('<p>タグ<input type="text" name="tags.value"></p>')
print('<p>活動場所<input type="text" name="area"></p>')
print('<p><input type="submit" value="検索"></p>')
print("</form>")
print("<table>")
print("<caption>検索結果</caption>")
print("<tr>")
print("<td>アーティスト名</td>")
print("<td>別名</td>")
print("<td>タグ</td>")
print("<td>活動場所</td>")
print("<td>活動開始</td>")
print("<td>活動終了</td>")
print("</tr>")

f = cgi.FieldStorage()
attributes = ['name', 'aliases.name', 'tags.value', 'area']
txt = list()
for i, attr in enumerate(attributes):
    txt.append(f.getfirst(attr, ''))
client = MongoClient()
db = client.knock64_database
collection = db.knock64_collection
find_dict = dict()
for attr, txt in zip(attributes, txt):
    if txt != '':
        find_dict[attr] = txt
data_list = ['name', 'aliases', 'tags', 'area', 'begin', 'end']
data_dict = {'aliases': 'name', 'tags': 'value'}
time = ['年', '月', '日']
for data in collection.find(find_dict, {'gid': 0, 'id': 0, '_id': 0}).sort([('rating.count', -1)]):
    print("<tr>")
    for x in data_list:
        if x in data_dict.keys() and x in data.keys():
            print("<td>")
            for y in data[x]:
                print("{} ".format(y[data_dict[x]]))
            print("</td>")
        elif x not in data.keys():
            print("<td></td>")
        elif x in ['begin', 'end']:
            a = zip(map(str, sorted(data[x].values(), reverse=True)), time)
            print("<td>")
            for t in a:
                print("".join(t), end="")
            print("</td>")
        else:
            print("<td>{}</td>".format(data[x]))
    print("</tr>")
print("</body>")
print("</html>")
