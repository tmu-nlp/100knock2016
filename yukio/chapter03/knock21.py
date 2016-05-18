# -*- coding: utf-8 -*-

import json
import re

text = ""

for line in open("jawiki-country.json", "r"):
    data = json.loads(line)
    if data["title"] == "イギリス":
        text += data["text"]

pattern = re.compile("Category")
for line in text.split("\n"):
    if pattern.search(line) != None:
        print(line)
    
