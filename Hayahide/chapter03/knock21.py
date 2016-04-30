#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")

for line in f:
    uk = json.loads(line)
    if uk["title"] == u"イギリス":
        break
f.close()

for word in uk["text"].split("\n"):
    if re.search("Category", word):
        print word


