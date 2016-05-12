# -*- coding: utf-8 -*-

import json
import re

text = ""

for line in open("jawiki-country.json", "r"):
    data = json.loads(line)
    if data["title"] == "イギリス":
        text += data["text"]

for line in text.split("\n"):
    for category in re.findall("\[\[Category:(.+)\]\]", line):
        print(category)
