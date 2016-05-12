# -*- coding: utf-8 -*-

import json
import re

text = ""
template = {}

for line in open("jawiki-country.json", "r"):
    data = json.loads(line)
    if data["title"] == "イギリス":
        text += data["text"]

target = 0
for line in text.split("\n"):
    if re.search("{{基礎情報", line):
        target = 1
    if target == 1:
        if re.search("\|.+ = .+", line):
            line = line.strip("|").replace("'", "")
            ans = line.split(" = ")
            template[ans[0]] = ans[1]
        if re.match("}}", line):
            break

for key, value in sorted(template.items()):
    print("{}：{}".format(key, value))
