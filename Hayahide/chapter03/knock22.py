#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")

for line in f:
    uk = json.loads(line)
    if uk["title"] == u"イギリス":
        break
f.close()        

category = []
for word in uk["text"].split("\n"):
    category += re.findall("\[\[Category:(.*)\]\]", word)

for line in category:
    print (line)
