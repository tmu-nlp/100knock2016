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
    word_list += re.findall(u"File:(.*\....)\||ファイル:(.*\....)\|", word)

for line in word_list:
    print line[0] if len(line[0]) > len(line[1]) else line[1]

f.close()
