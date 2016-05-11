#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
s=""
t=""
c=0
f=open("jawiki-country.json","r")
for line in f.readlines():
    data=json.loads(line)
    if data["title"]==u"イギリス":
        s=data["text"]

for line in s.split("\n"):
    if line.startswith("="):
        print(line.strip("=")),
        print(str((len(line)-len(line.strip("=")))/2-1))
