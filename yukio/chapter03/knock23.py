# -*- coding: utf-8 -*-

import json
import re

text = ""

for line in open("jawiki-country.json", "r"):
    data = json.loads(line)
    if data["title"] == "イギリス":
        text += data["text"]

for line in text.split("\n"):
    for section in re.findall("^(=+.*?=+)$", line):
        level = int(section.count("=") / 2 - 1)
        section = section.replace("=", "")
        print("{} {}".format(section, level))
