#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
from pymongo import MongoClient

html2 = '''Content-Type: text/html
<html>
<head>
  <title>アーティスト検索</title>
  <style type="text/css">
<!--
pre {
  border-width: 1px;
  border-style: dotted;
  border-color: #009999;
  margin: 1em;
  padding: 1em;
}
-->
  </style>
</head>
<body>
<h1>結果</h1>
<pre>%s</pre>
</body>
</html>
'''

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
with open('output.txt', 'w') as fp:
    for data in collection.find(find_dict, {'gid': 0, 'id': 0, '_id': 0}).sort([('rating.count', -1)]):
        for key, value in sorted(data.items()):
            print('{}\t{}'.format(key, value), file=fp)
        print(file=fp)
fp = open('output.txt', 'r').read()
print(html2 % cgi.escape(fp))
