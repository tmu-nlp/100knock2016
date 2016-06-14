#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from pymongo import MongoClient

print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>検索結果</title>")
print("<style>")
print("table{border-collapse:collapse;}")
print("td{border:solid 1px;\npadding: 0.5em;}")
print("</style>")
print("</head>")
print("<body>")
print("<table>")
print("<caption>検索結果</caption>")
print("<tr>")
print("<td>アーティスト名</td>")
print("<td>別名</td>")
print("<td>タグ</td>")
print("<td>活動場所</td>")
#print("<td>活動開始</td>")
#print("<td>活動終了</td>")
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
data_list = ['name', 'aliases', 'tags', 'area']
data_dict = {'aliases': 'name', 'tags': 'value'}
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
        else:
            print("<td>{}</td>".format(data[x]))
    print("</tr>")

print("</body>")
print("</html>")
