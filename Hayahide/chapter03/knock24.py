#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")
word_list = []

for line in f:
    uk = json.loads(line)
    if uk["title"] == u"イギリス":
        break
f.close()

for word in uk["text"].split("\n"):
    if re.search(r"\.jpg.+|\.JPG.+|\.svg.+", word):
        word_list += re.findall(".+\.jpg|.+\.JPG|.+\.svg", word)

for line in word_list:
    print word_list.pop(0)
            
f.close()
