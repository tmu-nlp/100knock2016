#-*- coding: utf-8 -*-
import json
import re

f = open("jawiki-country.json", "r")
ans = {}

for line in f:
    uk = json.loads(line)
    if uk["title"] == u"イギリス":
        break
f.close()

flag = 0
for line in uk["text"].split("\n"):
    if re.search(u"基礎情報", line):
        flag = 1
    elif re.match("}}", line):
        flag = 0
    if flag and re.search(r".+ = .+", line):
        line = line.replace("'", "")
        word = line.lstrip("|").split(" = ")
        ans[word[0]] = word[1]

for title, text in ans.items():
    print (title, text)

