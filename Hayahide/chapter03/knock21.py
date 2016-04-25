#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")

for line in f:
    dic = json.loads(line)
    if dic["title"] == u"イギリス":
        for word in dic["text"].split():
            if re.search("Category", word):
                print word

f.close()

