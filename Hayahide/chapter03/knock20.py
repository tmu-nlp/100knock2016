#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")

for line in f:
    uk = json.loads(line)
    if uk["title"] == u"イギリス":
        word = uk["text"].split("\n")
        for text in word:
            print text
f.close()
