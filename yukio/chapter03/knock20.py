# -*- coding: utf-8 -*-

import json

text = ""

for line in open("jawiki-country.json", "r"):
    data = json.loads(line)
    if data["title"] == "イギリス":
        text += data["text"]

print(text)
