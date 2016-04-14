#!-*-coding:utf-8-*-

import json

f = open("jawiki-country.json", 'r')
for line in f:
    dict = json.loads(line)
    if dict["title"] == u"イギリス":
        print(dict["text"])









