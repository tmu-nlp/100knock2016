#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")

for line in f:
    dic = json.loads(line)
    if dic["title"] == u"イギリス":
        word = dic["text"].split()
        for text in word:
            print text

f.close()
