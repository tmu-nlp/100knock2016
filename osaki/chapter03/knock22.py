#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
s=""
t=""
f=open("jawiki-country.json","r")
for line in f.readlines():
    data=json.loads(line)
    if data["title"]==u"イギリス":
        s=data["text"]

for line in s.split("\n"):
    if "Category:" in line:
        print(line.split(":")[1].strip("]"))
