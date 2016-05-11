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
    if re.search(r"==.*==", word):
        count = word.count("=") / 2 - 1
        print (word.replace("=", ""))
        print (" Level: " + str(int(count)))
