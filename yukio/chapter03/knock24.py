# -*- coding: utf-8 -*-

import json
import re

text = ""

for line in open("jawiki-country.json", "r"):
    data = json.loads(line)
    if data["title"] == "イギリス":
        text += data["text"]

for line in text.split("\n"):
    for media_file in re.findall("[file, File, ファイル]:(.*\.[a-zA-Z]+)\|", line):
        print(media_file)
