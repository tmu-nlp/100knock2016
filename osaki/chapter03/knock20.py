#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

f=open("jawiki-country.json","r")
for line in f.readlines():
    data=json.loads(line)
    if data["title"]==u"イギリス":
        print (data["text"])
        break
f.close()
