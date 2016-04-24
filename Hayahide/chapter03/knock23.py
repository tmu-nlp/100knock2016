#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")

for line in f:
    dic = json.loads(line)
    if dic["title"] == u"イギリス":
        for word in dic["text"].split():
            if re.search(r"==.*==", word):
                count = word.count("=") / 2 - 1
                print word.replace("=", "")
                print count

f.close()

