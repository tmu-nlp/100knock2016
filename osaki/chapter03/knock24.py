#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
f=open("jawiki-country.json","r")
for line in f.readlines():
    data=json.loads(line)
    if data["title"]==u"イギリス":
        s=data["text"]

for line in s.split("\n"):
    if u"ファイル" in line or "File" in line:
        for t in line.split("|"):
            if "File" in t or u"ファイル" in t:
                print(t.split(":")[1])
